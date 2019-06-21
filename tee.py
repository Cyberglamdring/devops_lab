#!/usr/bin/env python
class Tee(object):
    """Write on file online"""

    def __init__(self, *files):
        self.files = files

    def write(self, obj):
        for f in self.files:
            f.write(obj)
            f.flush()   # If the output to be visible immediately

    def flush(self) :
        for f in self.files:
            f.flush()