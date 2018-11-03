# WavHeader.py
#   Extract basic header information from a WAV file
import logging
import os
import struct


def parse_wav_list(buf):
    print(buf)


def detect_chunks(start, file):
    pass


def get_wav_headers(strWAVFile):
    """ Extracts data in the first 44 bytes in a WAV file and writes it
            out in a human-readable format
    """

    logging.basicConfig(level=logging.DEBUG)

    # def DumpHeaderOutput(structHeaderFields):
    #     for key in structHeaderFields.keys():
    #         print("%s: " % (key), structHeaderFields[key])
    # end for
    # Open file
    try:
        fileIn = open(strWAVFile, 'rb')
    except IOError:
        logging.debug("Could not open input file %s" % (strWAVFile))
        return None
    # end try
    # Read in all data
    bufHeader = fileIn.read(38)
    # Verify that the correct identifiers are present
    if (bufHeader[0:4] != b"RIFF") or \
       (bufHeader[12:16] != b"fmt "):
        logging.debug("Input file not a standard WAV file")
        return None
    # endif
    fields = {'ChunkSize': 0, 'Format': '',
              'Subchunk1Size': 0, 'AudioFormat': 0,
              'NumChannels': 0, 'SampleRate': 0,
              'ByteRate': 0, 'BlockAlign': 0,
              'BitsPerSample': 0, 'Filename': '', 'Duration': 0, 'SampleRate': 0}
    # Parse fields
    fields['ChunkSize'] = int(struct.unpack('<L', bufHeader[4:8])[0])
    fields['Format'] = bufHeader[8:12]
    fields['Subchunk1Size'] = int(struct.unpack('<L', bufHeader[16:20])[0])
    fields['AudioFormat'] = struct.unpack('<H', bufHeader[20:22])[0]
    fields['NumChannels'] = int(struct.unpack('<H', bufHeader[22:24])[0])
    fields['SampleRate'] = int(struct.unpack('<L', bufHeader[24:28])[0])
    fields['ByteRate'] = int(struct.unpack('<L', bufHeader[28:32])[0])
    fields['BlockAlign'] = int(struct.unpack('<H', bufHeader[32:34])[0])
    fields['BitsPerSample'] = int(struct.unpack('<H', bufHeader[34:36])[0])
    # Locate & read data chunk
    # chunks = {}
    # dataChunkLocation = 0
    # fileIn.seek(0, 2)  # Seek to end of file
    # inputFileSize = fileIn.tell()
    # nextChunkLocation = 12  # skip the RIFF header
    #
    # while 1:
    #     # Read subchunk header
    #     print(nextChunkLocation)
    #     fileIn.seek(nextChunkLocation)
    #     bufHeader = fileIn.read(8)
    #     print(bufHeader)
    #     if bufHeader[0:4] == b"data":
    #         dataChunkLocation = nextChunkLocation
    #     # endif
    #     chunk_size = struct.unpack('<L', bufHeader[4:8])[0]
    #     res = {"start": nextChunkLocation + 8, "size": chunk_size}
    #     nextChunkLocation += (8 + chunk_size)
    #     chunks[bufHeader[0:4]] = res
    #     if nextChunkLocation >= inputFileSize:
    #         break
    #
    #     # endif
    # # end while
    # # Dump subchunk list
    # print("Subchunks Found: ")
    # for key in chunks:
    #     print("%s, " % key)
    #     print("%s, " % chunks[key])
    #
    # if b'LIST' in chunks:
    #     wav_list = chunks[b'LIST']
    #     fileIn.seek(wav_list["start"])
    #     buf = fileIn.read(wav_list["size"])
    #     parse_wav_list(buf)

    # endif
    # Print output
    # fields['Filename'] = os.path.basename(strWAVFile)
    fields['Duration'] = int(fields["ChunkSize"] / (fields['SampleRate'] * fields['NumChannels'] * fields["BitsPerSample"] / 8))
    # DumpHeaderOutput(fields)
    # Close file
    fileIn.close()
    #print(fields)
    return (fields)


# r = PrintWavHeader("/home/vin/Doctorat/data/acoustic/field/Hochstetter/2018/Plot1/5B536690.WAV")
# print(r)
