import gpib

class GPIBTransport:
    EOS_NONE = 0x0
    EOS_REOS = 0x400
    EOS_XEOS = 0x800
    EOS_BIN  = 0x1000

    TIMEOUTS = [None, '0us', '30us', '100us', '300us', '1ms', '3ms', '10ms',
                '30ms', '100ms', '300ms', '1s', '3s', '10s', '30s', '100s', '300s', '1000s']

    def __init__(self, board=0, paddr=0, saddr=None, timeout='10s', send_eoi=True,
            eos_char=None, eos_mode=EOS_NONE):

        if not 0 <= paddr <= 30:
            raise ValueError("Primary address must be in [0, 30].")

        if saddr is not None and not 0 <= saddr <= 30:
            raise ValueError("Secondary address must be in [0, 30].")

        # linux-gpib uses the unfortunate NI convention of
        # adding 0x60 to the secondary address
        saddr = 0 if saddr is None else saddr + 0x60

        timeout = self.TIMEOUTS.index(timeout)

        eos = (eos_char or 0) | eos_mode

        self._handle = gpib.dev(board, paddr, saddr, timeout, send_eoi, eos)

    def __del__(self):
        # close on drop
        self.close()

    def __repr__(self):
        return f'<GPIB {self._handle}>'

    def close(self):
        if self._handle is not None:
            gpib.close(self._handle)
            self._handle = None

    def write(self, data: str):
        gpib.write(self._handle, data)

    def write_async(self, data: str):
        gpib.write_async(self._handle, data)

    def read(self, length=512):
        return gpib.read(self._handle, length)

    @property
    def transfer_count(self):
        return gpib.ibcnt()

    @property
    def status(self):
        return gpib.ibsta()
