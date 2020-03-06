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
        self.spi = bus.MCU_SPI_from_config(config, 3, default_speed=4000000)

    def _handle_connect(self):
        self.gcode.respond_info("iniiiiiiiiit")
        self.spi.spi_send(0x0E21)
        self.spi.spi_send(0x1196)
        self.spi.spi_send(0x2097)
        self.spi.spi_send(0x31D7)
        self.spi.spi_send(0x4430)
        self.spi.spi_send(0x583C)
        self.spi.spi_send(0x60F0)
        self.spi.spi_send(0x7000)


def load_config_prefix(config):
    return drv8711(config)
