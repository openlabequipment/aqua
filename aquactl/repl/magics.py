from IPython.core import magic
import aqua.client

@magic.magics_class
class Magics(magic.Magics):
    @magic.line_magic
    def ping(self, line):
        """ping the aqua controller server.
        will print {success,fail} status + the roundtrip time-to-reply"""

        print("sending rpc ping...")
        pass
