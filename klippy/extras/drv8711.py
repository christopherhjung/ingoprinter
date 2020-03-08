# MCP4018 digipot support (via bit-banging)
#
# Copyright (C) 2019  Kevin O'Connor <kevin@koconnor.net>
#
# This file may be distributed under the terms of the GNU GPLv3 license.

import bus

class drv8711:
    def __init__(self, config):
        self.printer = config.get_printer()
        self.gcode = self.printer.lookup_object("gcode")
        self.printer.register_event_handler("klippy:connect", self._handle_connect)
        self.spi = bus.MCU_SPI_from_config(config, 3)

    def _handle_connect(self):
        self.send(0x0E21)
        self.send(0x1196)
        self.send(0x2097)
        self.send(0x31D7)
        self.send(0x4430)
        self.send(0x583C)
        self.send(0x60F0)
        self.send(0x7000)

    def send(self, val):
        data = [(val >> 8) & 0xff, val & 0xff]
        self.spi.spi_send(data)
        response = self.spi.spi_send(data)

    def reverse_mask(self, x):
        x = ((x & 0x55555555) << 1) | ((x & 0xAAAAAAAA) >> 1)
        x = ((x & 0x33333333) << 2) | ((x & 0xCCCCCCCC) >> 2)
        x = ((x & 0x0F0F0F0F) << 4) | ((x & 0xF0F0F0F0) >> 4)
        x = ((x & 0x00FF00FF) << 8) | ((x & 0xFF00FF00) >> 8)
        x = ((x & 0x0000FFFF) << 16) | ((x & 0xFFFF0000) >> 16)
        return x

def load_config_prefix(config):
    return drv8711(config)
