import socket
import struct
import textwrap

#Unpacking ethernet frame:
def ethernet_frame(data):   #grabs first 14 bytes and unpacks it...
    dest_mac, sndr_mac, proto = struct.unpack('! 6s 6s H', data[:14])  #6s = 2 bytes, H = 2 bytes, small unsigned int
    return get_mac_addr(dest_mac), get_mac_addr(sndr_mac), socket.htons(proto), data[14:]

