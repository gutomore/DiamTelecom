import os

class Pcap:
    def __init__(self, filepath, ports: list = [], filter='diameter'):
        self.filepath = filepath
        self.filename = os.path.basename(filepath)
        self.filter = filter
        self.ports = ports

    @property
    def decode_as(self):
        decode_as = {}
        for port in self.ports:
            decode_as[f"tcp.port=={port}"] = 'diameter'
        return decode_as