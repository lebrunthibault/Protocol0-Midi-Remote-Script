# Companion MIDI proxy script for [Protocol0 surface script]((https://github.com/lebrunthibault/Protocol-0-Surface-Script))

It allows the [Protocol0 backend](https://github.com/lebrunthibault/Protocol-0-backend) to communicate back to the script.

> NB : A surface script cannot listen to multiple midi ports at the same time

The surface script is already listening to the controller port (my faderfox ec4).
So the only way to communicate with it from the backend is to create a second script : 
it's only goal is to forward midi to the main script.

So this script simply routes external midi messages received on its input port to the [Protocol0 script](https://github.com/lebrunthibault/Protocol-0-Surface-Script).
Should be setup with P0_IN virtual midi port as input.