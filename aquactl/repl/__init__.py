"""\
                                               __
    .---.-.-----.--.--.---.-.----.-----.-----.|  |
    |  _  |  _  |  |  |  _  |   _|  -__|  _  ||  |
    |___._|__   |_____|___._|__| |_____|   __||__|
             |__|                      |__|

    ----a repl for the aqua hplc controller------
"""

from .magics import Magics

from IPython.terminal.embed import InteractiveShellEmbed
ipy = InteractiveShellEmbed()

ipy.register_magics(Magics)


def run():
    ipy.show_banner(__doc__)
    ipy.mainloop()
