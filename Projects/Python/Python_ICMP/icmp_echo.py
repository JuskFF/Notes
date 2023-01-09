# -*- coding: utf-8 -*-

"""
    A class of constructing the icmp echo request(default) or
    echo reply.

    :copyleft: Created by Jusk 2022-10-21
    :license: GUN GPL v2
"""

import os
import struct
import socket

DATA_STRING = "ABCDEFHIJ"


class Echo(object):

    def __init__(self, _type=8, payload=DATA_STRING):
        """Initialize ICMP Echo(Default) or Echo reply field

        Parameter:
            TYPE -> 8bit,The default value of this parameter is 8 i.e. Echo request.
            If it is set to 0 indicated Echo reply.
            CODE -> 8bit.
            CHECKSUM -> 16bit.
            IDENTIFIER -> 8bit Usually use the value of PID to pad.
            SEQ_NUM -> 8bit.
            PAYLOAD -> Less than 1472 bytes.

        Raise:
            When the value you set for the _type parameter is invalid,
            the init function will throw an ICMP Echo Type exception.

        Returns:
            This init function has no return value.

        """
        if _type == 8 or _type == 0:
            self._type = _type
        else:
            raise ValueError("The ICMP Echo message type value can only be 0 or 8.")
        self.code = 0
        self.checksum = 0
        self.identifier = os.getpid()
        self.seq_num = 1
        self.payload = payload

    def encapsulate_payload(self):
        """Encapsulate payload to byte stream

        Returns:
            Return a tuple which contained the ICMP_Header's byte stream and its length.
        """
        b_raw_string = self.payload.encode("utf-8")
        b_payload = struct.pack("!{}s".format(len(b_raw_string)), b_raw_string)
        len_b_payload = len(b_raw_string)

        return b_payload, len_b_payload

    def encapsulate_header(self):
        """Encapsulate ICMP header to byte stream

        Returns:
            Return a tuple which contained the ICMP_Payload's byte stream and its length.
        """
        b_header = struct.pack("!2B3H", self._type, self.code, self.checksum,
                               self.identifier, self.seq_num)
        len_b_header = struct.calcsize("!2B3H")

        return b_header, len_b_header

    def get_bytes_before_checksum(self):
        """Get the byte stream before calculating checksum

        Returns:
            Return a tuple which contained the ICMP's byte stream and its length.
        """
        b_icmp = self.encapsulate_header()[0] + self.encapsulate_payload()[0]
        len_b_icmp = self.encapsulate_header()[1] + self.encapsulate_payload()[1]

        return b_icmp, len_b_icmp

    def calculate_checksum(self):
        """Calculate the ICMP Header checksum

        Returns:
             Return the checksum -> bytes
        """
        # calculate the sum of 16 bit
        checksum = 0
        b_icmp = self.get_bytes_before_checksum()[0]
        len_b_icmp = self.get_bytes_before_checksum()[1]
        if len_b_icmp % 2:
            b_icmp += b"\x00"
            len_b_icmp += 1
        for i in range(len_b_icmp // 2):
            one_byte, = struct.unpack("!H", b_icmp[i*2:i*2+2])
            checksum += one_byte

        # Judge whether there is carry
        while True:
            carry = checksum >> 16
            if carry:
                checksum = (checksum & 0xFFFF) + carry
            else:
                break
        checksum = ~checksum & 0xFFFF
        b_checksum = struct.pack("!H", checksum)

        return b_checksum

    def get_bytes_after_checksum(self):
        """Get the byte stream after calculating checksum

        Returns:
            Return a tuple of the final byte stream of the ICMP and its length.
        """
        b_before_checksum = self.get_bytes_before_checksum()[0]
        b_c_checksum = self.calculate_checksum()
        b_after_checksum = b_before_checksum[:2] + b_c_checksum + b_before_checksum[4:]

        return b_after_checksum, len(b_after_checksum)











a = Echo(8,"777777")
# print(a.encapsulate_header()[0])
# print(a.encapsulate_payload()[0])
# print(a.encapsulate_header()[1])
# print(a.encapsulate_payload()[1])
# print(a.get_bytes_before_checksum()[0])
# print(a.get_bytes_before_checksum()[1])
# print(a.get_bytes_before_checksum()[0])
# print(a.calculate_checksum())
# print(a.get_bytes_after_checksum()[0])
# print(a.get_bytes_after_checksum()[1])
# len1 = a.encapsulate_payload()[1]
# raw_b_str, = struct.unpack("{}s".format(len1), a.encapsulate_payload()[0])
# print(raw_b_str.decode("utf-8"))
# print(a.encapsulate_payload()[0])
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
# s.sendto(a.get_bytes_after_checksum()[0], ("10.200.176.10", 0))
s.bind(("10.200.176.83", 0))
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
while True:
    print("data receiving.....")
    rec = s.recvfrom(1500)

    print(rec)
    print(len(rec[0]))