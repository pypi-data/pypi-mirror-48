"""
Python interface to the miniaudio library (https://github.com/dr-soft/miniaudio)

Author: Irmen de Jong (irmen@razorvine.net)
Software license: "MIT software license". See http://opensource.org/licenses/MIT
"""

__version__ = "1.5"


import sys
import os
import io
import array
import struct
import inspect
from enum import Enum
from typing import Generator, List, Tuple, Dict, Optional, Union, Any
from _miniaudio import ffi, lib
try:
    import numpy
except ImportError:
    numpy = None

lib.init_miniaudio()


class SampleFormat(Enum):
    """Sample format in memory"""
    UNKNOWN = lib.ma_format_unknown
    UNSIGNED8 = lib.ma_format_u8
    SIGNED16 = lib.ma_format_s16
    SIGNED24 = lib.ma_format_s24
    SIGNED32 = lib.ma_format_s32
    FLOAT32 = lib.ma_format_f32


class DeviceType(Enum):
    """Type of audio device"""
    PLAYBACK = lib.ma_device_type_playback
    CAPTURE = lib.ma_device_type_capture
    DUPLEX = lib.ma_device_type_duplex


class DitherMode(Enum):
    """How to dither when converting"""
    NONE = lib.ma_dither_mode_none
    RECTANGLE = lib.ma_dither_mode_rectangle
    TRIANGLE = lib.ma_dither_mode_triangle


class ChannelMixMode(Enum):
    """How to mix channels when converting"""
    RECTANGULAR = lib.ma_channel_mix_mode_rectangular
    SIMPLE = lib.ma_channel_mix_mode_simple
    CUSTOMWEIGHTS = lib.ma_channel_mix_mode_custom_weights
    PLANARBLEND = lib.ma_channel_mix_mode_planar_blend
    DEFAULT = lib.ma_channel_mix_mode_default


class SoundFileInfo:
    """Contains various properties of an audio file."""
    def __init__(self, name: str, file_format: str, nchannels: int, sample_rate: int,
                 sample_format: SampleFormat, duration: float, num_frames: int) -> None:
        self.name = name
        self.nchannels = nchannels
        self.sample_rate = sample_rate
        self.sample_format = sample_format
        self.sample_format_name = ffi.string(lib.ma_get_format_name(sample_format.value)).decode()
        self.sample_width, _ = _width_from_format(sample_format)
        self.num_frames = num_frames
        self.duration = duration
        self.file_format = file_format

    def __str__(self) -> str:
        return "['{name}': {nchannels} ch, {sample_rate} hz, {sample_format.name}, " \
               "{num_frames} frames={duration:.2f} sec.]".format(**vars(self))


class DecodedSoundFile(SoundFileInfo):
    """Contains various properties and also the raw PCM samples of a fully decoded audio file."""
    def __init__(self, name: str, nchannels: int, sample_rate: int,
                 sample_format: SampleFormat, samples: array.array) -> None:
        num_frames = len(samples) // nchannels
        duration = num_frames / sample_rate
        super().__init__(name, "", nchannels, sample_rate, sample_format, duration, num_frames)
        self.samples = samples


class MiniaudioError(Exception):
    """When a miniaudio specific error occurs."""
    pass


class DecodeError(MiniaudioError):
    """When something went wrong during decoding an audio file."""
    pass


def get_file_info(filename: str) -> SoundFileInfo:
    """Fetch some information about the audio file."""
    ext = os.path.splitext(filename)[1].lower()
    if ext in (".ogg", ".vorbis"):
        return vorbis_get_file_info(filename)
    elif ext == ".mp3":
        return mp3_get_file_info(filename)
    elif ext == ".flac":
        return flac_get_file_info(filename)
    elif ext == ".wav":
        return wav_get_file_info(filename)
    raise DecodeError("unsupported file format")


def read_file(filename: str) -> DecodedSoundFile:
    """Reads and decodes the whole audio file. Resulting sample format is 16 bits signed integer."""
    ext = os.path.splitext(filename)[1].lower()
    if ext in (".ogg", ".vorbis"):
        return vorbis_read_file(filename)
    elif ext == ".mp3":
        return mp3_read_file_s16(filename)
    elif ext == ".flac":
        return flac_read_file_s16(filename)
    elif ext == ".wav":
        return wav_read_file_s16(filename)
    raise DecodeError("unsupported file format")


def vorbis_get_file_info(filename: str) -> SoundFileInfo:
    """Fetch some information about the audio file (vorbis format)."""
    filenamebytes = _get_filename_bytes(filename)
    error = ffi.new("int *")
    vorbis = lib.stb_vorbis_open_filename(filenamebytes, error, ffi.NULL)
    if not vorbis:
        raise DecodeError("could not open/decode file")
    try:
        info = lib.stb_vorbis_get_info(vorbis)
        duration = lib.stb_vorbis_stream_length_in_seconds(vorbis)
        num_frames = lib.stb_vorbis_stream_length_in_samples(vorbis)
        return SoundFileInfo(filename, "vorbis", info.channels, info.sample_rate,
                             SampleFormat.SIGNED16, duration, num_frames)
    finally:
        lib.stb_vorbis_close(vorbis)


def vorbis_get_info(data: bytes) -> SoundFileInfo:
    """Fetch some information about the audio data (vorbis format)."""
    error = ffi.new("int *")
    vorbis = lib.stb_vorbis_open_memory(data, len(data), error, ffi.NULL)
    if not vorbis:
        raise DecodeError("could not open/decode data")
    try:
        info = lib.stb_vorbis_get_info(vorbis)
        duration = lib.stb_vorbis_stream_length_in_seconds(vorbis)
        num_frames = lib.stb_vorbis_stream_length_in_samples(vorbis)
        return SoundFileInfo("<memory>", "vorbis", info.channels, info.sample_rate,
                             SampleFormat.SIGNED16, duration, num_frames)
    finally:
        lib.stb_vorbis_close(vorbis)


def vorbis_read_file(filename: str) -> DecodedSoundFile:
    """Reads and decodes the whole vorbis audio file. Resulting sample format is 16 bits signed integer."""
    filenamebytes = _get_filename_bytes(filename)
    channels = ffi.new("int *")
    sample_rate = ffi.new("int *")
    output = ffi.new("short **")
    num_frames = lib.stb_vorbis_decode_filename(filenamebytes, channels, sample_rate, output)
    if num_frames <= 0:
        raise DecodeError("cannot load/decode file")
    try:
        buffer = ffi.buffer(output[0], num_frames * channels[0] * 2)
        samples = _create_int_array(2)
        samples.frombytes(buffer)
        return DecodedSoundFile(filename, channels[0], sample_rate[0], SampleFormat.SIGNED16, samples)
    finally:
        lib.free(output[0])


def vorbis_read(data: bytes) -> DecodedSoundFile:
    """Reads and decodes the whole vorbis audio data. Resulting sample format is 16 bits signed integer."""
    channels = ffi.new("int *")
    sample_rate = ffi.new("int *")
    output = ffi.new("short **")
    num_samples = lib.stb_vorbis_decode_memory(data, len(data), channels, sample_rate, output)
    if num_samples <= 0:
        raise DecodeError("cannot load/decode data")
    try:
        buffer = ffi.buffer(output[0], num_samples * channels[0] * 2)
        samples = _create_int_array(2)
        samples.frombytes(buffer)
        return DecodedSoundFile("<memory>", channels[0], sample_rate[0], SampleFormat.SIGNED16, samples)
    finally:
        lib.free(output[0])


def vorbis_stream_file(filename: str) -> Generator[array.array, None, None]:
    """Streams the ogg vorbis audio file as interleaved 16 bit signed integer sample arrays segments."""
    filenamebytes = _get_filename_bytes(filename)
    error = ffi.new("int *")
    vorbis = lib.stb_vorbis_open_filename(filenamebytes, error, ffi.NULL)
    if not vorbis:
        raise DecodeError("could not open/decode file")
    try:
        info = lib.stb_vorbis_get_info(vorbis)
        decode_buffer1 = ffi.new("short[]", 4096 * info.channels)
        decodebuf_ptr1 = ffi.cast("short *", decode_buffer1)
        decode_buffer2 = ffi.new("short[]", 4096 * info.channels)
        decodebuf_ptr2 = ffi.cast("short *", decode_buffer2)
        # note: we decode several frames to reduce the overhead of very small sample sizes a little
        while True:
            num_samples1 = lib.stb_vorbis_get_frame_short_interleaved(vorbis, info.channels, decodebuf_ptr1,
                                                                      4096 * info.channels)
            num_samples2 = lib.stb_vorbis_get_frame_short_interleaved(vorbis, info.channels, decodebuf_ptr2,
                                                                      4096 * info.channels)
            if num_samples1 + num_samples2 <= 0:
                break
            buffer = ffi.buffer(decode_buffer1, num_samples1 * 2 * info.channels)
            samples = _create_int_array(2)
            samples.frombytes(buffer)
            if num_samples2 > 0:
                buffer = ffi.buffer(decode_buffer2, num_samples2 * 2 * info.channels)
                samples.frombytes(buffer)
            yield samples
    finally:
        lib.stb_vorbis_close(vorbis)


def flac_get_file_info(filename: str) -> SoundFileInfo:
    """Fetch some information about the audio file (flac format)."""
    filenamebytes = _get_filename_bytes(filename)
    flac = lib.drflac_open_file(filenamebytes)
    if not flac:
        raise DecodeError("could not open/decode file")
    try:
        duration = flac.totalPCMFrameCount / flac.sampleRate
        sample_width = flac.bitsPerSample // 8
        return SoundFileInfo(filename, "flac", flac.channels, flac.sampleRate,
                             _format_from_width(sample_width), duration, flac.totalPCMFrameCount)
    finally:
        lib.drflac_close(flac)


def flac_get_info(data: bytes) -> SoundFileInfo:
    """Fetch some information about the audio data (flac format)."""
    flac = lib.drflac_open_memory(data, len(data))
    if not flac:
        raise DecodeError("could not open/decode data")
    try:
        duration = flac.totalPCMFrameCount / flac.sampleRate
        sample_width = flac.bitsPerSample // 8
        return SoundFileInfo("<memory>", "flac", flac.channels, flac.sampleRate,
                             _format_from_width(sample_width), duration, flac.totalPCMFrameCount)
    finally:
        lib.drflac_close(flac)


def flac_read_file_s32(filename: str) -> DecodedSoundFile:
    """Reads and decodes the whole flac audio file. Resulting sample format is 32 bits signed integer."""
    filenamebytes = _get_filename_bytes(filename)
    channels = ffi.new("unsigned int *")
    sample_rate = ffi.new("unsigned int *")
    num_frames = ffi.new("drflac_uint64 *")
    memory = lib.drflac_open_file_and_read_pcm_frames_s32(filenamebytes, channels, sample_rate, num_frames)
    if not memory:
        raise DecodeError("cannot load/decode file")
    try:
        samples = _create_int_array(4)
        buffer = ffi.buffer(memory, num_frames[0] * channels[0] * 4)
        samples.frombytes(buffer)
        return DecodedSoundFile(filename, channels[0], sample_rate[0], SampleFormat.SIGNED32, samples)
    finally:
        lib.drflac_free(memory)


def flac_read_file_s16(filename: str) -> DecodedSoundFile:
    """Reads and decodes the whole flac audio file. Resulting sample format is 16 bits signed integer."""
    filenamebytes = _get_filename_bytes(filename)
    channels = ffi.new("unsigned int *")
    sample_rate = ffi.new("unsigned int *")
    num_frames = ffi.new("drflac_uint64 *")
    memory = lib.drflac_open_file_and_read_pcm_frames_s16(filenamebytes, channels, sample_rate, num_frames)
    if not memory:
        raise DecodeError("cannot load/decode file")
    try:
        samples = _create_int_array(2)
        buffer = ffi.buffer(memory, num_frames[0] * channels[0] * 2)
        samples.frombytes(buffer)
        return DecodedSoundFile(filename, channels[0], sample_rate[0], SampleFormat.SIGNED16, samples)
    finally:
        lib.drflac_free(memory)


def flac_read_file_f32(filename: str) -> DecodedSoundFile:
    """Reads and decodes the whole flac audio file. Resulting sample format is 32 bits float."""
    filenamebytes = _get_filename_bytes(filename)
    channels = ffi.new("unsigned int *")
    sample_rate = ffi.new("unsigned int *")
    num_frames = ffi.new("drflac_uint64 *")
    memory = lib.drflac_open_file_and_read_pcm_frames_f32(filenamebytes, channels, sample_rate, num_frames)
    if not memory:
        raise DecodeError("cannot load/decode file")
    try:
        samples = array.array('f')
        buffer = ffi.buffer(memory, num_frames[0] * channels[0] * 4)
        samples.frombytes(buffer)
        return DecodedSoundFile(filename, channels[0], sample_rate[0], SampleFormat.FLOAT32, samples)
    finally:
        lib.drflac_free(memory)


def flac_read_s32(data: bytes) -> DecodedSoundFile:
    """Reads and decodes the whole flac audio data. Resulting sample format is 32 bits signed integer."""
    channels = ffi.new("unsigned int *")
    sample_rate = ffi.new("unsigned int *")
    num_frames = ffi.new("drflac_uint64 *")
    memory = lib.drflac_open_memory_and_read_pcm_frames_s32(data, len(data), channels, sample_rate, num_frames)
    if not memory:
        raise DecodeError("cannot load/decode data")
    try:
        samples = _create_int_array(4)
        buffer = ffi.buffer(memory, num_frames[0] * channels[0] * 4)
        samples.frombytes(buffer)
        return DecodedSoundFile("<memory>", channels[0], sample_rate[0], SampleFormat.SIGNED32, samples)
    finally:
        lib.drflac_free(memory)


def flac_read_s16(data: bytes) -> DecodedSoundFile:
    """Reads and decodes the whole flac audio data. Resulting sample format is 16 bits signed integer."""
    channels = ffi.new("unsigned int *")
    sample_rate = ffi.new("unsigned int *")
    num_frames = ffi.new("drflac_uint64 *")
    memory = lib.drflac_open_memory_and_read_pcm_frames_s16(data, len(data), channels, sample_rate, num_frames)
    if not memory:
        raise DecodeError("cannot load/decode data")
    try:
        samples = _create_int_array(2)
        buffer = ffi.buffer(memory, num_frames[0] * channels[0] * 2)
        samples.frombytes(buffer)
        return DecodedSoundFile("<memory>", channels[0], sample_rate[0], SampleFormat.SIGNED16, samples)
    finally:
        lib.drflac_free(memory)


def flac_read_f32(data: bytes) -> DecodedSoundFile:
    """Reads and decodes the whole flac audio file. Resulting sample format is 32 bits float."""
    channels = ffi.new("unsigned int *")
    sample_rate = ffi.new("unsigned int *")
    num_frames = ffi.new("drflac_uint64 *")
    memory = lib.drflac_open_memory_and_read_pcm_frames_f32(data, len(data), channels, sample_rate, num_frames)
    if not memory:
        raise DecodeError("cannot load/decode data")
    try:
        samples = array.array('f')
        buffer = ffi.buffer(memory, num_frames[0] * channels[0] * 4)
        samples.frombytes(buffer)
        return DecodedSoundFile("<memory>", channels[0], sample_rate[0], SampleFormat.FLOAT32, samples)
    finally:
        lib.drflac_free(memory)


def flac_stream_file(filename: str, frames_to_read: int = 1024) -> Generator[array.array, None, None]:
    """Streams the flac audio file as interleaved 16 bit signed integer sample arrays segments."""
    filenamebytes = _get_filename_bytes(filename)
    flac = lib.drflac_open_file(filenamebytes)
    if not flac:
        raise DecodeError("could not open/decode file")
    try:
        decodebuffer = ffi.new("drflac_int16[]", frames_to_read * flac.channels)
        buf_ptr = ffi.cast("drflac_int16 *", decodebuffer)
        while True:
            num_samples = lib.drflac_read_pcm_frames_s16(flac, frames_to_read, buf_ptr)
            if num_samples <= 0:
                break
            buffer = ffi.buffer(decodebuffer, num_samples * 2 * flac.channels)
            samples = _create_int_array(2)
            samples.frombytes(buffer)
            yield samples
    finally:
        lib.drflac_close(flac)


def mp3_get_file_info(filename: str) -> SoundFileInfo:
    """Fetch some information about the audio file (mp3 format)."""
    filenamebytes = _get_filename_bytes(filename)
    config = ffi.new("drmp3_config *")
    config.outputChannels = 0
    config.outputSampleRate = 0
    mp3 = ffi.new("drmp3 *")
    if not lib.drmp3_init_file(mp3, filenamebytes, config):
        raise DecodeError("could not open/decode file")
    try:
        num_frames = lib.drmp3_get_pcm_frame_count(mp3)
        duration = num_frames / mp3.sampleRate
        return SoundFileInfo(filename, "mp3", mp3.channels, mp3.sampleRate,
                             SampleFormat.SIGNED16, duration, num_frames)
    finally:
        lib.drmp3_uninit(mp3)


def mp3_get_info(data: bytes) -> SoundFileInfo:
    """Fetch some information about the audio data (mp3 format)."""
    config = ffi.new("drmp3_config *")
    config.outputChannels = 0
    config.outputSampleRate = 0
    mp3 = ffi.new("drmp3 *")
    if not lib.drmp3_init_memory(mp3, data, len(data), config):
        raise DecodeError("could not open/decode data")
    try:
        num_frames = lib.drmp3_get_pcm_frame_count(mp3)
        duration = num_frames / mp3.sampleRate
        return SoundFileInfo("<memory>", "mp3", mp3.channels, mp3.sampleRate,
                             SampleFormat.SIGNED16, duration, num_frames)
    finally:
        lib.drmp3_uninit(mp3)


def mp3_read_file_f32(filename: str, want_nchannels: int = 0, want_sample_rate: int = 0) -> DecodedSoundFile:
    """Reads and decodes the whole mp3 audio file. Resulting sample format is 32 bits float."""
    filenamebytes = _get_filename_bytes(filename)
    config = ffi.new("drmp3_config *")
    config.outputChannels = want_nchannels
    config.outputSampleRate = want_sample_rate
    num_frames = ffi.new("drmp3_uint64 *")
    memory = lib.drmp3_open_file_and_read_f32(filenamebytes, config, num_frames)
    if not memory:
        raise DecodeError("cannot load/decode file")
    try:
        samples = array.array('f')
        buffer = ffi.buffer(memory, num_frames[0] * config.outputChannels * 4)
        samples.frombytes(buffer)
        return DecodedSoundFile(filename, config.outputChannels, config.outputSampleRate,
                                SampleFormat.FLOAT32, samples)
    finally:
        lib.drmp3_free(memory)


def mp3_read_file_s16(filename: str, want_nchannels: int = 0, want_sample_rate: int = 0) -> DecodedSoundFile:
    """Reads and decodes the whole mp3 audio file. Resulting sample format is 16 bits signed integer."""
    filenamebytes = _get_filename_bytes(filename)
    config = ffi.new("drmp3_config *")
    config.outputChannels = want_nchannels
    config.outputSampleRate = want_sample_rate
    num_frames = ffi.new("drmp3_uint64 *")
    memory = lib.drmp3_open_file_and_read_s16(filenamebytes, config, num_frames)
    if not memory:
        raise DecodeError("cannot load/decode file")
    try:
        samples = _create_int_array(2)
        buffer = ffi.buffer(memory, num_frames[0] * config.outputChannels * 2)
        samples.frombytes(buffer)
        return DecodedSoundFile(filename, config.outputChannels, config.outputSampleRate,
                                SampleFormat.SIGNED16, samples)
    finally:
        lib.drmp3_free(memory)


def mp3_read_f32(data: bytes, want_nchannels: int = 0, want_sample_rate: int = 0) -> DecodedSoundFile:
    """Reads and decodes the whole mp3 audio data. Resulting sample format is 32 bits float."""
    config = ffi.new("drmp3_config *")
    config.outputChannels = want_nchannels
    config.outputSampleRate = want_sample_rate
    num_frames = ffi.new("drmp3_uint64 *")
    memory = lib.drmp3_open_memory_and_read_f32(data, len(data), config, num_frames)
    if not memory:
        raise DecodeError("cannot load/decode data")
    try:
        samples = array.array('f')
        buffer = ffi.buffer(memory, num_frames[0] * config.outputChannels * 4)
        samples.frombytes(buffer)
        return DecodedSoundFile("<memory>", config.outputChannels, config.outputSampleRate,
                                SampleFormat.FLOAT32, samples)
    finally:
        lib.drmp3_free(memory)


def mp3_read_s16(data: bytes, want_nchannels: int = 0, want_sample_rate: int = 0) -> DecodedSoundFile:
    """Reads and decodes the whole mp3 audio data. Resulting sample format is 16 bits signed integer."""
    config = ffi.new("drmp3_config *")
    config.outputChannels = want_nchannels
    config.outputSampleRate = want_sample_rate
    num_frames = ffi.new("drmp3_uint64 *")
    memory = lib.drmp3_open_memory_and_read_s16(data, len(data), config, num_frames)
    if not memory:
        raise DecodeError("cannot load/decode data")
    try:
        samples = _create_int_array(2)
        buffer = ffi.buffer(memory, num_frames[0] * config.outputChannels * 2)
        samples.frombytes(buffer)
        return DecodedSoundFile("<memory>", config.outputChannels, config.outputSampleRate,
                                SampleFormat.SIGNED16, samples)
    finally:
        lib.drmp3_free(memory)


def mp3_stream_file(filename: str, frames_to_read: int = 1024,
                    want_nchannels: int = 0, want_sample_rate: int = 0) -> Generator[array.array, None, None]:
    """Streams the mp3 audio file as interleaved 16 bit signed integer sample arrays segments."""
    filenamebytes = _get_filename_bytes(filename)
    config = ffi.new("drmp3_config *")
    config.outputChannels = want_nchannels
    config.outputSampleRate = want_sample_rate
    mp3 = ffi.new("drmp3 *")
    if not lib.drmp3_init_file(mp3, filenamebytes, config):
        raise DecodeError("could not open/decode file")
    try:
        decodebuffer = ffi.new("drmp3_int16[]", frames_to_read * mp3.channels)
        buf_ptr = ffi.cast("drmp3_int16 *", decodebuffer)
        while True:
            num_samples = lib.drmp3_read_pcm_frames_s16(mp3, frames_to_read, buf_ptr)
            if num_samples <= 0:
                break
            buffer = ffi.buffer(decodebuffer, num_samples * 2 * mp3.channels)
            samples = _create_int_array(2)
            samples.frombytes(buffer)
            yield samples
    finally:
        lib.drmp3_uninit(mp3)


def wav_get_file_info(filename: str) -> SoundFileInfo:
    """Fetch some information about the audio file (wav format)."""
    filenamebytes = _get_filename_bytes(filename)
    wav = lib.drwav_open_file(filenamebytes)
    if not wav:
        raise DecodeError("could not open/decode file")
    try:
        duration = wav.totalPCMFrameCount / wav.sampleRate
        sample_width = wav.bitsPerSample // 8
        # XXX what about floating point format?
        return SoundFileInfo(filename, "wav", wav.channels, wav.sampleRate,
                             _format_from_width(sample_width), duration, wav.totalPCMFrameCount)
    finally:
        lib.drwav_close(wav)


def wav_get_info(data: bytes) -> SoundFileInfo:
    """Fetch some information about the audio data (wav format)."""
    wav = lib.drwav_open_memory(data, len(data))
    if not wav:
        raise DecodeError("could not open/decode data")
    try:
        duration = wav.totalPCMFrameCount / wav.sampleRate
        sample_width = wav.bitsPerSample // 8
        # XXX what about floating point format?
        return SoundFileInfo("<memory>", "wav", wav.channels, wav.sampleRate,
                             _format_from_width(sample_width), duration, wav.totalPCMFrameCount)
    finally:
        lib.drwav_close(wav)


def wav_read_file_s32(filename: str) -> DecodedSoundFile:
    """Reads and decodes the whole wav audio file. Resulting sample format is 32 bits signed integer."""
    filenamebytes = _get_filename_bytes(filename)
    channels = ffi.new("unsigned int *")
    sample_rate = ffi.new("unsigned int *")
    num_frames = ffi.new("drwav_uint64 *")
    memory = lib.drwav_open_file_and_read_pcm_frames_s32(filenamebytes, channels, sample_rate, num_frames)
    if not memory:
        raise DecodeError("cannot load/decode file")
    try:
        samples = _create_int_array(4)
        buffer = ffi.buffer(memory, num_frames[0] * channels[0] * 4)
        samples.frombytes(buffer)
        return DecodedSoundFile(filename, channels[0], sample_rate[0], SampleFormat.SIGNED32, samples)
    finally:
        lib.drwav_free(memory)


def wav_read_file_s16(filename: str) -> DecodedSoundFile:
    """Reads and decodes the whole wav audio file. Resulting sample format is 16 bits signed integer."""
    filenamebytes = _get_filename_bytes(filename)
    channels = ffi.new("unsigned int *")
    sample_rate = ffi.new("unsigned int *")
    num_frames = ffi.new("drwav_uint64 *")
    memory = lib.drwav_open_file_and_read_pcm_frames_s16(filenamebytes, channels, sample_rate, num_frames)
    if not memory:
        raise DecodeError("cannot load/decode file")
    try:
        samples = _create_int_array(2)
        buffer = ffi.buffer(memory, num_frames[0] * channels[0] * 2)
        samples.frombytes(buffer)
        return DecodedSoundFile(filename, channels[0], sample_rate[0], SampleFormat.SIGNED16, samples)
    finally:
        lib.drwav_free(memory)


def wav_read_file_f32(filename: str) -> DecodedSoundFile:
    """Reads and decodes the whole wav audio file. Resulting sample format is 32 bits float."""
    filenamebytes = _get_filename_bytes(filename)
    channels = ffi.new("unsigned int *")
    sample_rate = ffi.new("unsigned int *")
    num_frames = ffi.new("drwav_uint64 *")
    memory = lib.drwav_open_file_and_read_pcm_frames_f32(filenamebytes, channels, sample_rate, num_frames)
    if not memory:
        raise DecodeError("cannot load/decode file")
    try:
        samples = array.array('f')
        buffer = ffi.buffer(memory, num_frames[0] * channels[0] * 4)
        samples.frombytes(buffer)
        return DecodedSoundFile(filename, channels[0], sample_rate[0], SampleFormat.FLOAT32, samples)
    finally:
        lib.drwav_free(memory)


def wav_read_s32(data: bytes) -> DecodedSoundFile:
    """Reads and decodes the whole wav audio data. Resulting sample format is 32 bits signed integer."""
    channels = ffi.new("unsigned int *")
    sample_rate = ffi.new("unsigned int *")
    num_frames = ffi.new("drwav_uint64 *")
    memory = lib.drwav_open_memory_and_read_pcm_frames_s32(data, len(data), channels, sample_rate, num_frames)
    if not memory:
        raise DecodeError("cannot load/decode data")
    try:
        samples = _create_int_array(4)
        buffer = ffi.buffer(memory, num_frames[0] * channels[0] * 4)
        samples.frombytes(buffer)
        return DecodedSoundFile("<memory>", channels[0], sample_rate[0], SampleFormat.SIGNED32, samples)
    finally:
        lib.drwav_free(memory)


def wav_read_s16(data: bytes) -> DecodedSoundFile:
    """Reads and decodes the whole wav audio data. Resulting sample format is 16 bits signed integer."""
    channels = ffi.new("unsigned int *")
    sample_rate = ffi.new("unsigned int *")
    num_frames = ffi.new("drwav_uint64 *")
    memory = lib.drwav_open_memory_and_read_pcm_frames_s16(data, len(data), channels, sample_rate, num_frames)
    if not memory:
        raise DecodeError("cannot load/decode data")
    try:
        samples = _create_int_array(2)
        buffer = ffi.buffer(memory, num_frames[0] * channels[0] * 2)
        samples.frombytes(buffer)
        return DecodedSoundFile("<memory>", channels[0], sample_rate[0], SampleFormat.SIGNED16, samples)
    finally:
        lib.drwav_free(memory)


def wav_read_f32(data: bytes) -> DecodedSoundFile:
    """Reads and decodes the whole wav audio data. Resulting sample format is 32 bits float."""
    channels = ffi.new("unsigned int *")
    sample_rate = ffi.new("unsigned int *")
    num_frames = ffi.new("drwav_uint64 *")
    memory = lib.drwav_open_memory_and_read_pcm_frames_f32(data, len(data), channels, sample_rate, num_frames)
    if not memory:
        raise DecodeError("cannot load/decode data")
    try:
        samples = array.array('f')
        buffer = ffi.buffer(memory, num_frames[0] * channels[0] * 4)
        samples.frombytes(buffer)
        return DecodedSoundFile("<memory>", channels[0], sample_rate[0], SampleFormat.FLOAT32, samples)
    finally:
        lib.drwav_free(memory)


def wav_stream_file(filename: str, frames_to_read: int = 1024) -> Generator[array.array, None, None]:
    """Streams the WAV audio file as interleaved 16 bit signed integer sample arrays segments."""
    filenamebytes = _get_filename_bytes(filename)
    wav = lib.drwav_open_file(filenamebytes)
    if not wav:
        raise DecodeError("could not open/decode file")
    try:
        decodebuffer = ffi.new("drwav_int16[]", frames_to_read * wav.channels)
        buf_ptr = ffi.cast("drwav_int16 *", decodebuffer)
        while True:
            num_samples = lib.drwav_read_pcm_frames_s16(wav, frames_to_read, buf_ptr)
            if num_samples <= 0:
                break
            buffer = ffi.buffer(decodebuffer, num_samples * 2 * wav.channels)
            samples = _create_int_array(2)
            samples.frombytes(buffer)
            yield samples
    finally:
        lib.drwav_close(wav)


def wav_write_file(filename: str, sound: DecodedSoundFile) -> None:
    """Writes the pcm sound to a WAV file"""
    fmt = ffi.new("drwav_data_format*")
    fmt.container = lib.drwav_container_riff
    fmt.format = lib.DR_WAVE_FORMAT_PCM
    fmt.channels = sound.nchannels
    fmt.sampleRate = sound.sample_rate
    fmt.bitsPerSample = sound.sample_width * 8
    # what about floating point format?
    filename_bytes = filename.encode(sys.getfilesystemencoding())
    pwav = lib.drwav_open_file_write_sequential(filename_bytes, fmt, sound.num_frames * sound.nchannels)
    if pwav == ffi.NULL:
        raise IOError("can't open file for writing")
    try:
        lib.drwav_write_pcm_frames(pwav, sound.num_frames, sound.samples.tobytes())
    finally:
        lib.drwav_close(pwav)


def _create_int_array(itemsize: int) -> array.array:
    for typecode in "bhilq":
        a = array.array(typecode)
        if a.itemsize == itemsize:
            return a
    raise ValueError("cannot create array")


def _get_filename_bytes(filename: str) -> bytes:
    filename2 = os.path.expanduser(filename)
    if not os.path.isfile(filename2):
        raise FileNotFoundError(filename)
    return filename2.encode(sys.getfilesystemencoding())


class Devices:
    """Query the audio playback and record devices that miniaudio provides"""
    def __init__(self) -> None:
        self._context = ffi.new("ma_context*")
        result = lib.ma_context_init(ffi.NULL, 0, ffi.NULL, self._context)
        if result != lib.MA_SUCCESS:
            raise MiniaudioError("cannot init context", result)
        self.backend = ffi.string(lib.ma_get_backend_name(self._context[0].backend)).decode()

    def get_playbacks(self) -> List[Dict[str, Any]]:
        """Get a list of playback devices and some details about them"""
        playback_infos = ffi.new("ma_device_info**")
        playback_count = ffi.new("ma_uint32*")
        result = lib.ma_context_get_devices(self._context, playback_infos, playback_count, ffi.NULL,  ffi.NULL)
        if result != lib.MA_SUCCESS:
            raise MiniaudioError("cannot get device infos", result)
        devs = []
        for i in range(playback_count[0]):
            ma_device_info = playback_infos[0][i]
            dev_id = ffi.new("ma_device_id *", ma_device_info.id)  # copy the id memory
            info = {
                "name": ffi.string(ma_device_info.name).decode(),
                "type": DeviceType.PLAYBACK,
                "id": dev_id
            }
            info.update(self._get_info(DeviceType.PLAYBACK, ma_device_info))
            devs.append(info)
        return devs

    def get_captures(self) -> List[Dict[str, Any]]:
        """Get a list of capture devices and some details about them"""
        capture_infos = ffi.new("ma_device_info**")
        capture_count = ffi.new("ma_uint32*")
        result = lib.ma_context_get_devices(self._context, ffi.NULL,  ffi.NULL, capture_infos, capture_count)
        if result != lib.MA_SUCCESS:
            raise MiniaudioError("cannot get device infos", result)
        devs = []
        for i in range(capture_count[0]):
            ma_device_info = capture_infos[0][i]
            dev_id = ffi.new("ma_device_id *", ma_device_info.id)  # copy the id memory
            info = {
                "name": ffi.string(ma_device_info.name).decode(),
                "type": DeviceType.CAPTURE,
                "id": dev_id
            }
            info.update(self._get_info(DeviceType.CAPTURE, ma_device_info))
            devs.append(info)
        return devs

    def _get_info(self, device_type: DeviceType, device_info: ffi.CData) -> Dict[str, Any]:
        # obtain detailed info about the device
        lib.ma_context_get_device_info(self._context, device_type.value, ffi.addressof(device_info.id),
                                       0, ffi.addressof(device_info))
        formats = set(device_info.formats[0:device_info.formatCount])
        return {
            "formats": {f: ffi.string(lib.ma_get_format_name(f)).decode() for f in formats},
            "minChannels": device_info.minChannels,
            "maxChannels": device_info.maxChannels,
            "minSampleRate": device_info.minSampleRate,
            "maxSampleRate": device_info.maxSampleRate
        }

    def __del__(self):
        lib.ma_context_uninit(self._context)


def _width_from_format(sampleformat: SampleFormat) -> Tuple[int, array.array]:
    if sampleformat == SampleFormat.FLOAT32:
        return 4, array.array('f')
    elif sampleformat == SampleFormat.UNSIGNED8:
        return 1, _create_int_array(1)
    elif sampleformat == SampleFormat.SIGNED16:
        return 2, _create_int_array(2)
    elif sampleformat == SampleFormat.SIGNED32:
        return 4, _create_int_array(4)
    else:
        raise ValueError("unsupported sample format", sampleformat)


def _format_from_width(sample_width: int, is_float: bool = False) -> SampleFormat:
    if is_float:
        return SampleFormat.FLOAT32
    elif sample_width == 1:
        return SampleFormat.UNSIGNED8
    elif sample_width == 2:
        return SampleFormat.SIGNED16
    elif sample_width == 3:
        return SampleFormat.SIGNED24
    elif sample_width == 4:
        return SampleFormat.SIGNED32
    else:
        raise ValueError("unsupported sample width", sample_width)


def decode_file(filename: str, output_format: SampleFormat = SampleFormat.SIGNED16,
                nchannels: int = 2, sample_rate: int = 44100) -> DecodedSoundFile:
    """Convenience function to decode any supported audio file to raw PCM samples in your chosen format."""
    sample_width, samples = _width_from_format(output_format)
    filenamebytes = _get_filename_bytes(filename)
    frames = ffi.new("ma_uint64 *")
    data = ffi.new("void **")
    decoder_config = lib.ma_decoder_config_init(output_format.value, nchannels, sample_rate)
    result = lib.ma_decode_file(filenamebytes, ffi.addressof(decoder_config), frames, data)
    if result != lib.MA_SUCCESS:
        raise DecodeError("failed to decode file", result)
    buffer = ffi.buffer(data[0], frames[0] * nchannels * sample_width)
    samples.frombytes(buffer)
    return DecodedSoundFile(filename, nchannels, sample_rate, output_format, samples)


def decode(data: bytes, output_format: SampleFormat = SampleFormat.SIGNED16,
           nchannels: int = 2, sample_rate: int = 44100) -> DecodedSoundFile:
    """Convenience function to decode any supported audio file in memory to raw PCM samples in your chosen format."""
    sample_width, samples = _width_from_format(output_format)
    frames = ffi.new("ma_uint64 *")
    memory = ffi.new("void **")
    decoder_config = lib.ma_decoder_config_init(output_format.value, nchannels, sample_rate)
    result = lib.ma_decode_memory(data, len(data), ffi.addressof(decoder_config), frames, memory)
    if result != lib.MA_SUCCESS:
        raise DecodeError("failed to decode data", result)
    buffer = ffi.buffer(memory[0], frames[0] * nchannels * sample_width)
    samples.frombytes(buffer)
    return DecodedSoundFile("<memory>", nchannels, sample_rate, output_format, samples)


def _samples_generator(frames_to_read: int, nchannels: int, output_format: SampleFormat,
                       decoder: ffi.CData, data: Any) -> Generator[array.array, int, None]:
    _reference = data    # make sure any data passed in is not garbage collected
    sample_width, samples_proto = _width_from_format(output_format)
    allocated_buffer_frames = max(frames_to_read, 16384)
    try:
        decodebuffer = ffi.new("int8_t[]", allocated_buffer_frames * nchannels * sample_width)
        buf_ptr = ffi.cast("void *", decodebuffer)
        want_frames = (yield samples_proto) or frames_to_read
        while True:
            if want_frames > allocated_buffer_frames:
                raise MiniaudioError("wanted to read more frames than storage was allocated for ({} vs {})"
                                     .format(want_frames, allocated_buffer_frames))
            num_frames = lib.ma_decoder_read_pcm_frames(decoder, buf_ptr, want_frames)
            if num_frames <= 0:
                break
            buffer = ffi.buffer(decodebuffer, num_frames * sample_width * nchannels)
            samples = array.array(samples_proto.typecode)
            samples.frombytes(buffer)
            want_frames = (yield samples) or frames_to_read
    finally:
        lib.ma_decoder_uninit(decoder)


def stream_file(filename: str, output_format: SampleFormat = SampleFormat.SIGNED16, nchannels: int = 2,
                sample_rate: int = 44100, frames_to_read: int = 1024) -> Generator[array.array, int, None]:
    """
    Convenience generator function to decode and stream any supported audio file
    as chunks of raw PCM samples in the chosen format.
    If you send() a number into the generator rather than just using next() on it,
    you'll get that given number of frames, instead of the default configured amount.
    This is particularly useful to plug this stream into an audio device callback that
    wants a variable number of frames per call.
    """
    filenamebytes = _get_filename_bytes(filename)
    decoder = ffi.new("ma_decoder *")
    decoder_config = lib.ma_decoder_config_init(output_format.value, nchannels, sample_rate)
    result = lib.ma_decoder_init_file(filenamebytes, ffi.addressof(decoder_config), decoder)
    if result != lib.MA_SUCCESS:
        raise DecodeError("failed to decode file", result)
    g = _samples_generator(frames_to_read, nchannels, output_format, decoder, None)
    dummy = next(g)
    assert len(dummy) == 0
    return g


def stream_memory(data: bytes, output_format: SampleFormat = SampleFormat.SIGNED16, nchannels: int = 2,
                  sample_rate: int = 44100, frames_to_read: int = 1024) -> Generator[array.array, int, None]:
    """
    Convenience generator function to decode and stream any supported audio file in memory
    as chunks of raw PCM samples in the chosen format.
    If you send() a number into the generator rather than just using next() on it,
    you'll get that given number of frames, instead of the default configured amount.
    This is particularly useful to plug this stream into an audio device callback that
    wants a variable number of frames per call.
    """
    decoder = ffi.new("ma_decoder *")
    decoder_config = lib.ma_decoder_config_init(output_format.value, nchannels, sample_rate)
    result = lib.ma_decoder_init_memory(data, len(data), ffi.addressof(decoder_config), decoder)
    if result != lib.MA_SUCCESS:
        raise DecodeError("failed to decode memory", result)
    g = _samples_generator(frames_to_read, nchannels, output_format, decoder, data)
    dummy = next(g)
    assert len(dummy) == 0
    return g


def convert_sample_format(from_fmt: SampleFormat, sourcedata: bytes, to_fmt: SampleFormat,
                          dither: DitherMode = DitherMode.NONE) -> bytearray:
    """Convert a raw buffer of pcm samples to another sample format.
    The result is returned as another raw pcm sample buffer"""
    sample_width, _ = _width_from_format(from_fmt)
    num_samples = len(sourcedata) // sample_width
    sample_width, _ = _width_from_format(to_fmt)
    buffer = bytearray(sample_width * num_samples)
    lib.ma_pcm_convert(ffi.from_buffer(buffer), to_fmt.value, sourcedata, from_fmt.value, num_samples, dither.value)
    return buffer


def convert_frames(from_fmt: SampleFormat, from_numchannels: int, from_samplerate: int, sourcedata: bytes,
                   to_fmt: SampleFormat, to_numchannels: int, to_samplerate: int) -> bytearray:
    """Convert audio frames in source sample format with a certain number of channels,
    to another sample format and possibly down/upmixing the number of channels as well."""
    sample_width, _ = _width_from_format(from_fmt)
    num_frames = int(len(sourcedata) / from_numchannels / sample_width)
    sample_width, _ = _width_from_format(to_fmt)
    output_frame_count = lib.ma_calculate_frame_count_after_src(to_samplerate, from_samplerate, num_frames)
    buffer = bytearray(output_frame_count * sample_width * to_numchannels)
    frame_count = lib.ma_convert_frames(ffi.from_buffer(buffer), to_fmt.value, to_numchannels, to_samplerate,
                                        sourcedata, from_fmt.value, from_numchannels, from_samplerate, num_frames)
    return buffer


_callback_data = {}     # type: Dict[int, Union[PlaybackDevice, CaptureDevice, DuplexStream]]


@ffi.def_extern()
def _internal_data_callback(device: ffi.CData, output: ffi.CData, input: ffi.CData, framecount: int) -> None:
    if framecount == 0 or not device.pUserData:
        return
    userdata_id = struct.unpack('q', ffi.unpack(ffi.cast("char *", device.pUserData), struct.calcsize('q')))[0]
    callback_device = _callback_data[userdata_id]  # type: Union[PlaybackDevice, CaptureDevice, DuplexStream]
    callback_device.data_callback(device, output, input, framecount)


PlaybackCallbackGeneratorType = Generator[Union[bytes, array.array], int, None]
CaptureCallbackGeneratorType = Generator[None, Union[bytes, array.array], None]
DuplexCallbackGeneratorType = Generator[Union[bytes, array.array], Union[bytes, array.array], None]
GeneratorTypes = Union[PlaybackCallbackGeneratorType, CaptureCallbackGeneratorType, DuplexCallbackGeneratorType]


class AbstractDevice:
    def __init__(self):
        self.callback_generator = None          # type: Optional[GeneratorTypes]
        self._device = ffi.new("ma_device *")

    def __del__(self) -> None:
        self.close()

    def start(self, callback_generator: GeneratorTypes) -> None:
        """Start playback or capture, using the given callback generator (should already been started)"""
        if self.callback_generator:
            raise MiniaudioError("can't start an already started device")
        if not inspect.isgenerator(callback_generator):
            raise TypeError("callback must be a generator", type(callback_generator))
        self.callback_generator = callback_generator
        result = lib.ma_device_start(self._device)
        if result != lib.MA_SUCCESS:
            raise MiniaudioError("failed to start audio device", result)

    def stop(self) -> None:
        """Halt playback or capture."""
        self.callback_generator = None
        result = lib.ma_device_stop(self._device)
        if result != lib.MA_SUCCESS:
            raise MiniaudioError("failed to stop audio device", result)

    def close(self) -> None:
        """Halt playback or capture and close down the device."""
        self.callback_generator = None
        if self._device is not None:
            lib.ma_device_uninit(self._device)
            self._device = None
        if id(self) in _callback_data:
            del _callback_data[id(self)]


class CaptureDevice(AbstractDevice):
    """An audio device provided by miniaudio, for audio capture (recording)."""
    def __init__(self, input_format: SampleFormat = SampleFormat.SIGNED16, nchannels: int = 2,
                 sample_rate: int = 44100, buffersize_msec: int = 200, device_id: Union[ffi.CData, None] = None
                 ) -> None:
        super().__init__()
        self.format = input_format
        self.sample_width, _ = _width_from_format(input_format)
        self.nchannels = nchannels
        self.sample_rate = sample_rate
        self.buffersize_msec = buffersize_msec
        _callback_data[id(self)] = self
        self.userdata_ptr = ffi.new("char[]", struct.pack('q', id(self)))
        self._devconfig = lib.ma_device_config_init(lib.ma_device_type_capture)
        lib.ma_device_config_set_params(ffi.addressof(self._devconfig), self.sample_rate, self.buffersize_msec,
                                        0, 0, 0, self.format.value, self.nchannels, ffi.NULL, device_id or ffi.NULL)
        self._devconfig.pUserData = self.userdata_ptr
        self._devconfig.dataCallback = lib._internal_data_callback
        self.callback_generator = None  # type: Optional[CaptureCallbackGeneratorType]
        result = lib.ma_device_init(ffi.NULL, ffi.addressof(self._devconfig), self._device)
        if result != lib.MA_SUCCESS:
            raise MiniaudioError("failed to init device", result)
        if self._device.pContext.backend == lib.ma_backend_null:
            raise MiniaudioError("no suitable audio backend found")
        self.backend = ffi.string(lib.ma_get_backend_name(self._device.pContext.backend)).decode()

    def start(self, callback_generator: CaptureCallbackGeneratorType) -> None:      # type: ignore
        """Start the audio device: capture (recording) begins.
        The recorded audio data is sent to the given callback generator as raw bytes.
        (it should already be started before)"""
        return super().start(callback_generator)

    def data_callback(self, device: ffi.CData, output: ffi.CData, input: ffi.CData, framecount: int) -> None:
        if self.callback_generator:
            buffer_size = self.sample_width * self.nchannels * framecount
            data = bytearray(buffer_size)
            ffi.memmove(data, input, buffer_size)
            try:
                self.callback_generator.send(data)
            except StopIteration:
                self.callback_generator = None
                return
            except Exception:
                self.callback_generator = None
                raise


class PlaybackDevice(AbstractDevice):
    """An audio device provided by miniaudio, for audio playback."""
    def __init__(self, output_format: SampleFormat = SampleFormat.SIGNED16, nchannels: int = 2,
                 sample_rate: int = 44100, buffersize_msec: int = 200, device_id: Union[ffi.CData, None] = None
                 ) -> None:
        super().__init__()
        self.format = output_format
        self.sample_width, _ = _width_from_format(output_format)
        self.nchannels = nchannels
        self.sample_rate = sample_rate
        self.buffersize_msec = buffersize_msec
        _callback_data[id(self)] = self
        self.userdata_ptr = ffi.new("char[]", struct.pack('q', id(self)))
        self._devconfig = lib.ma_device_config_init(lib.ma_device_type_playback)
        lib.ma_device_config_set_params(ffi.addressof(self._devconfig), self.sample_rate, self.buffersize_msec,
                                        0, self.format.value, self.nchannels, 0, 0, device_id or ffi.NULL, ffi.NULL)
        self._devconfig.pUserData = self.userdata_ptr
        self._devconfig.dataCallback = lib._internal_data_callback
        self.callback_generator = None   # type: Optional[PlaybackCallbackGeneratorType]
        result = lib.ma_device_init(ffi.NULL, ffi.addressof(self._devconfig), self._device)
        if result != lib.MA_SUCCESS:
            raise MiniaudioError("failed to init device", result)
        if self._device.pContext.backend == lib.ma_backend_null:
            raise MiniaudioError("no suitable audio backend found")
        self.backend = ffi.string(lib.ma_get_backend_name(self._device.pContext.backend)).decode()

    def start(self, callback_generator: PlaybackCallbackGeneratorType) -> None:     # type: ignore
        """Start the audio device: playback begins. The audio data is provided by the given callback generator.
        The generator gets sent the required number of frames and should yield the sample data
        as raw bytes, a memoryview, an array.array, or as a numpy array with shape (numframes, numchannels).
        The generator should already be started before passing it in."""
        return super().start(callback_generator)

    def data_callback(self, device: ffi.CData, output: ffi.CData, input: ffi.CData, framecount: int) -> None:
        if self.callback_generator:
            try:
                samples = self.callback_generator.send(framecount)
            except StopIteration:
                self.callback_generator = None
                return
            except Exception:
                self.callback_generator = None
                raise
            samples_bytes = _bytes_from_generator_samples(samples)
            if samples_bytes:
                if len(samples_bytes) > framecount * self.sample_width * self.nchannels:
                    self.callback_generator = None
                    raise MiniaudioError("number of frames from callback exceeds maximum")
                ffi.memmove(output, samples_bytes, len(samples_bytes))


class DuplexStream(AbstractDevice):
    """Joins a capture device and a playback device."""
    def __init__(self, playback_format: SampleFormat = SampleFormat.SIGNED16,
                 playback_channels: int = 2, capture_format: SampleFormat = SampleFormat.SIGNED16,
                 capture_channels: int = 2, sample_rate: int = 44100, buffersize_msec: int = 200,
                 playback_device_id: Union[ffi.CData, None] = None, capture_device_id: Union[ffi.CData, None] = None
                 ) -> None:
        super().__init__()
        self.capture_format = capture_format
        self.playback_format = playback_format
        self.sample_width, _ = _width_from_format(capture_format)
        self.capture_channels = capture_channels
        self.playback_channels = playback_channels
        self.sample_rate = sample_rate
        self.buffersize_msec = buffersize_msec
        _callback_data[id(self)] = self
        self.userdata_ptr = ffi.new("char[]", struct.pack('q', id(self)))
        self._devconfig = lib.ma_device_config_init(lib.ma_device_type_duplex)

        lib.ma_device_config_set_params(
            ffi.addressof(self._devconfig), self.sample_rate, self.buffersize_msec, 0,
            playback_format.value, playback_channels, capture_format.value, capture_channels,
            playback_device_id or ffi.NULL, capture_device_id or ffi.NULL)
        self._devconfig.pUserData = self.userdata_ptr
        self._devconfig.dataCallback = lib._internal_data_callback
        self.callback_generator = None  # type: Optional[DuplexCallbackGeneratorType]

        result = lib.ma_device_init(ffi.NULL, ffi.addressof(self._devconfig), self._device)
        if result != lib.MA_SUCCESS:
            raise MiniaudioError("failed to init device", result)
        if self._device.pContext.backend == lib.ma_backend_null:
            raise MiniaudioError("no suitable audio backend found")
        self.backend = ffi.string(lib.ma_get_backend_name(self._device.pContext.backend)).decode()

    def start(self, callback_generator: DuplexCallbackGeneratorType) -> None:   # type: ignore
        """Start the audio device: playback and capture begin.
        The audio data for playback is provided by the given callback generator, which is sent the
        recorded audio data at the same time.
        (it should already be started before passing it in)"""
        return super().start(callback_generator)

    def data_callback(self, device: ffi.CData, output: ffi.CData, input: ffi.CData, framecount: int) -> None:
        buffer_size = self.sample_width * self.capture_channels * framecount
        in_data = bytearray(buffer_size)
        ffi.memmove(in_data, input, buffer_size)
        if self.callback_generator:
            try:
                out_data = self.callback_generator.send(in_data)
            except StopIteration:
                self.callback_generator = None
                return
            except Exception:
                self.callback_generator = None
                raise
            if out_data:
                samples_bytes = _bytes_from_generator_samples(out_data)
                ffi.memmove(output, samples_bytes, len(samples_bytes))


def _bytes_from_generator_samples(samples: Union[array.array, memoryview, bytes]) -> bytes:
    # convert any non-bytes generator result to raw bytes
    if isinstance(samples, array.array):
        return memoryview(samples).cast('B')       # type: ignore
    elif isinstance(samples, memoryview) and samples.itemsize != 1:
        return samples.cast('B')    # type: ignore
    elif numpy and isinstance(samples, numpy.ndarray):
        return samples.tobytes()
    return samples      # type: ignore


class WavFileReadStream(io.RawIOBase):
    """An IO stream that reads as a .wav file, and which gets its pcm samples from the provided producer"""
    def __init__(self, pcm_sample_gen: PlaybackCallbackGeneratorType, sample_rate: int, nchannels: int,
                 output_format: SampleFormat, max_frames: int = 0) -> None:
        self.sample_gen = pcm_sample_gen
        self.sample_rate = sample_rate
        self.nchannels = nchannels
        self.format = output_format
        self.max_frames = max_frames
        self.sample_width, _ = _width_from_format(output_format)
        self.max_bytes = (max_frames * nchannels * self.sample_width) or sys.maxsize
        self.bytes_done = 0
        # create WAVE header
        fmt = ffi.new("drwav_data_format*")
        fmt.container = lib.drwav_container_riff
        fmt.format = lib.DR_WAVE_FORMAT_PCM
        fmt.channels = nchannels
        fmt.sampleRate = sample_rate
        fmt.bitsPerSample = self.sample_width * 8
        data = ffi.new("void**")
        datasize = ffi.new("size_t *")
        if max_frames > 0:
            pwav = lib.drwav_open_memory_write_sequential(data, datasize, fmt, max_frames * nchannels)
        else:
            pwav = lib.drwav_open_memory_write(data, datasize, fmt)
        lib.drwav_close(pwav)
        self.buffered = bytes(ffi.buffer(data[0], datasize[0]))
        lib.drflac_free(data[0])

    def read(self, amount: int = sys.maxsize) -> Optional[bytes]:
        """Read up to the given amount of bytes from the file."""
        if self.bytes_done >= self.max_bytes or not self.sample_gen:
            return b""
        while len(self.buffered) < amount:
            try:
                samples = next(self.sample_gen)
            except StopIteration:
                self.bytes_done = sys.maxsize
                break
            else:
                self.buffered += _bytes_from_generator_samples(samples)
        result = self.buffered[:amount]
        self.buffered = self.buffered[amount:]
        self.bytes_done += len(result)
        return result

    def close(self) -> None:
        """Close the file"""
        pass
