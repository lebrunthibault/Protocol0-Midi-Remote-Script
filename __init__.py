import os
import sys
from os.path import dirname

from protocol0_midi.Protocol0Midi import Protocol0Midi

sys.path.insert(0, "%s\\protocol0\\venv\\Lib\\site-packages" % dirname(dirname(os.path.realpath(__file__))))

def create_instance(c_instance):  # noqa
    return Protocol0Midi(c_instance)
