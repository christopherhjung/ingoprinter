import bus

class drv8711:
    def __init__(self, config):
        self.printer = config.get_printer()
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

def load_config_prefix(config):
    return drv8711(config)
