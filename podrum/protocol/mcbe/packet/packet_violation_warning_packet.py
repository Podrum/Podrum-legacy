r"""
  ____           _
 |  _ \ ___   __| |_ __ _   _ _ __ ___
 | |_) / _ \ / _` | '__| | | | '_ ` _ \
 |  __/ (_) | (_| | |  | |_| | | | | | |
 |_|   \___/ \__,_|_|   \__,_|_| |_| |_|

 Copyright 2021 Podrum Team.

 This file is licensed under the GPL v2.0 license.
 The license file is located in the root directory
 of the source code. If not you may not use this file.
"""

from podrum.protocol.mcbe.mcbe_protocol_info import mcbe_protocol_info
from podrum.protocol.mcbe.packet.mcbe_packet import mcbe_packet


class packet_violation_warning_packet(mcbe_packet):
    def __init__(self, data: bytes = b"", pos: int = 0) -> None:
        super().__init__(data, pos)
        self.packet_id: int = mcbe_protocol_info.packet_violation_warning_packet

    def decode_payload(self) -> None:
        self.type: int = self.read_signed_var_int()
        self.severity: int = self.read_signed_var_int()
        self.violated_packet_id: int = self.read_signed_var_int()
        self.message: str = self.read_string()
        
    def encode_payload(self) -> None:
        self.write_signed_var_int(self.type)
        self.write_signed_var_int(self.severity)
        self.write_signed_var_int(self.violated_packet_id)
        self.write_string(self.message)
