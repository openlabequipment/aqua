class Waters600E:
    def __init__(self, gpib):
        self.gpib = gpib

    def id(self):
        r = self.gpib.query("ID").split(',')

        model = r[1]
        version = r[-1]

        return dict(model=model, version=version)

    def sparge_state(self):
        r = self.gpib.query("SP,R").split(',')

        s = float(r[2].strip())  # idk what this is for
        sparge_flags = dict(zip(['a', 'b', 'c', 'd'],
                                [(f == 'Y') for f in r[3:7]]))

        return dict(s=s, flags=sparge_flags)
