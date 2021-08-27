import sys

from protocol0_midi.Protocol0Midi import Protocol0Midi

sys.path.insert(0, "C:\\Python27\\Lib\\site-packages")

def create_instance(c_instance):  # noqa
    return Protocol0Midi(c_instance)
