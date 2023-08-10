import socket
import struct
import textwrap

def main():
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

    while True:
        raw_data, addr = conn.recvfrom(65546)
        dest_mac, sndr_mac, eth_proto, data = ethernet_frame(raw_data)
        print('\nEthernet Frame:')
        print('Destination: {}, Source: {}, Protocol: {}'.format(dest_mac, sndr_mac, eth_proto))

#Unpacking ethernet frame:
def ethernet_frame(data):   #grabs first 14 bytes and unpacks it...
    dest_mac, sndr_mac, proto = struct.unpack('! 6s 6s H', data[:14])  #6s = 2 bytes, H = 2 bytes, small unsigned int
    return get_mac_addr(dest_mac), get_mac_addr(sndr_mac), socket.htons(proto), data[14:]

#Return formatted MAC address
def get_mac_addr(bytes_addr):
    bytes_str = map('{:02x}'.format, bytes_addr)
    return ':'.join(bytes_str).upper()

main()