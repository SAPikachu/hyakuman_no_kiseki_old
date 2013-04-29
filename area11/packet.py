from __future__ import print_function, unicode_literals

import bson

CONTROL_PACKET = b"c"
DATA_PACKET = b"d"


def decode(data):
    if data[0] == DATA_PACKET:
        return DATA_PACKET, data[1:]

    return CONTROL_PACKET, bson.loads(data[1:])


def encode_control(data):
    return CONTROL_PACKET + bson.dumps(data)


def encode_data(data):
    return DATA_PACKET + data
