from __future__ import print_function, unicode_literals


class NoEncryption(object):
    """Stub for testing"""

    def encrypt(self, data):
        return data

    def decrypt(self, data):
        return data
