from types import MethodType
from typing import Any, Tuple

from _Framework.ControlSurface import ControlSurface, get_control_surfaces
from _Framework.Util import find_if
from protocol0 import Protocol0
from protocol0.enums.LogLevelEnum import LogLevelEnum
from protocol0.utils.log import log_ableton


class Protocol0Midi(ControlSurface):
    """
    This is needed because we cannot select multiple input ports in Live and windows MIDI ports are single client.
    So we send input to a loopback port connected to this small script and route it back to the main script.
    Alternate solution is more cumbersome: Merge midi ports with something like Bome

    This expects the Protocol0 code to be in the Remote scripts (will not even appear in the list otherwise)
    And will log an error if the Protocol0 script is not used as a Control Surface
    """

    def __init__(self, c_instance=None):
        # type: (Any, bool) -> None
        super(Protocol0Midi, self).__init__(c_instance=c_instance)
        # stop log duplication
        self._c_instance.log_message = MethodType(lambda s, message: None, self._c_instance)  # noqa
        self.main_p0_script = find_if(lambda s: isinstance(s, Protocol0), get_control_surfaces())  # type: Protocol0
        if self.main_p0_script is None:
            log_ableton("Error: couldn't find main Protocol0 script", level=LogLevelEnum.ERROR)
            return

        log_ableton("Found Protocol0 Script")

    def receive_midi(self, midi_bytes):
        # type: (Tuple) -> None
        log_ableton("Received midi bytes in P0 Midi !")
        if self.main_p0_script:
            self.main_p0_script.midiManager.receive_midi(midi_bytes)
        else:
            log_ableton("Received midi input but no Protocol0 script to forward it to", level=LogLevelEnum.ERROR)
