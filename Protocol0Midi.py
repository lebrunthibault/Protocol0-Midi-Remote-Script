from types import MethodType
from typing import Any, Tuple

from _Framework.ControlSurface import ControlSurface, get_control_surfaces
from _Framework.Util import find_if
from a_protocol_0 import Protocol0


class Protocol0Midi(ControlSurface):
    """
    This is needed because we cannot select multiple input ports in Live of windows MIDI ports being single client.
    So we send input to a virtual port connected to this small script and route it back to the main script.
    """

    def __init__(self, c_instance=None, test_mode=False):
        # type: (Any, bool) -> None
        super(Protocol0Midi, self).__init__(c_instance=c_instance)
        # stop log duplication
        self._c_instance.log_message = MethodType(lambda s, message: None, self._c_instance)  # noqa
        self.main_p0_script = find_if(lambda s: isinstance(s, Protocol0), get_control_surfaces())  # type: Protocol0
        if self.main_p0_script is None:
            self.log_message("Error: couldn't find main Protocol0 script")
            return

        self.log_message("Found Protocol0 Script")

    def receive_midi(self, midi_bytes):
        # type: (Tuple) -> None
        self.log_message("P0Midi: receive midi_bytes")
        self.log_message(midi_bytes)
        if self.main_p0_script:
            self.main_p0_script.midiManager.receive_midi(midi_bytes)
        else:
            self.log_message("Received midi input but no Protocol0 script to forward it to")
