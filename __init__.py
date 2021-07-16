from protocol0_midi.Protocol0Midi import Protocol0Midi

# noinspection PyBroadException
try:
    import protocol0.make_path
except Exception:
    pass


def create_instance(c_instance):  # noqa
    return Protocol0Midi(c_instance)
