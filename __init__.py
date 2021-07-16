from a_protocol_0_midi.Protocol0Midi import Protocol0Midi

# noinspection PyBroadException
try:
    import a_protocol_0.make_path
except Exception:
    pass


def create_instance(c_instance):  # noqa
    return Protocol0Midi(c_instance)
