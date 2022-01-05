# Companion MIDI proxy script for Protocol0 surface script

> A surface script cannot listen to multiple midi ports at the same time
> 

Still using the [Protocol0 backend](https://github.com/lebrunthibault/Protocol-0-backend) I need to send midi to my script

So I created this smallest companion ableton surface script for Protocol0. 
It routes external midi messages to its input port to the [Protocol0 script](https://github.com/lebrunthibault/Protocol-0-Surface-Script).
Should be setup with P0_IN virtual midi port as input.