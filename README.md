# Disclaimer : this project moved to the [protocol0](https://github.com/lebrunthibault/protocol0/tree/main/p0_script) monorepo

# Companion MIDI proxy script for [Protocol0 remote script]((https://github.com/lebrunthibault/Protocol0-Ableton-Remote-Script))

It allows the [Protocol0 backend](https://github.com/lebrunthibault/Protocol-0-backend) to communicate back to the script.

> NB : A surface script cannot listen to multiple midi ports at the same time

The remote script is already listening to the controller port (my faderfox ec4).
So the only way to communicate with it from the backend is to create a second script : 
it's only goal is to forward midi to the main script.

So this script simply routes external midi messages received on its input port to the [Protocol0 remote script](https://github.com/lebrunthibault/Protocol0-Ableton-Remote-Script).
Should be loaded twice in Live.
Once with P0_IN_MIDI, and the second time with P0_IN_HTTP virtual midi port as midi input port.
