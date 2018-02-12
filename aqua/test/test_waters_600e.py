from unittest.mock import MagicMock

from aqua.devices import Waters600E


def test_id():
    gpib = MagicMock()
    gpib.query.return_value = "ID,MODL,x,x,xx,1.337"
    dev = Waters600E(gpib)

    assert dev.id()['model'] == 'MODL'
    assert dev.id()['version'] == '1.337'


def test_sparge_state():
    gpib = MagicMock()
    gpib.query.return_value = "SP,R, 0.0,Y,N,Y,N"
    dev = Waters600E(gpib)

    assert dev.sparge_state()['s'] == 0.0
    assert dev.sparge_state()['flags'] == \
        {'a': True, 'b': False, 'c': True, 'd': False}
