from montypy.grail import utils

def test_sword():
    actual = utils.sword()
    expected = "sword"
    assert actual == expected