#!/usr/bin/python

import i3ipc

# If this flag is set to true, after the swap will be focused the initial workspace
# otherwise will be focused the first monitor
FLAG = True


i3 = i3ipc.Connection()

if FLAG:
	initial_workspace = i3.get_tree().find_focused().workspace().name

for display in i3.get_outputs():
	if display['current_workspace'] != None:
		i3.command('workspace --no-auto-back-and-forth ' + display['current_workspace'])
		i3.command('move workspace to output right')

if FLAG:
	i3.command('workspace --no-auto-back-and-forth ' + initial_workspace)