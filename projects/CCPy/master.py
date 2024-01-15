from defs import cmd as cmd

import struct

class master():

    def __init__(self, transport):
        self.ctr = 0
        self.transport = transport

    # A Command Receive Object CRO is sent from the master device to one of
    # the slave devices. The slave device answers with a Data Transmission
    # Object DTO containing a Command Return Message CRM.
    def __CRO__(self, cmd, data = bytearray(6)):
        print(cmd)
        print(data)
        pass

    # Mandatory Commands
    def connect(self, canID, station_address):

        data = bytearray(6)
        data[0] = struct.pack('<c', station_address);

        self.__CRO__(cmd['CONNECT'], data)

    def get_ccp_version(self):
        pass

    def exchange_id(self):
        pass

    def set_mta(self):
        pass

    def dnload(self):
        pass

    def upload(self):
        pass

    def get_daq_size(self):
        pass

    def set_daq_ptr(self):
        pass

    def write_daq(self):
        pass

    def start_stop(self):
        pass

    def disconnect(self):
        pass



