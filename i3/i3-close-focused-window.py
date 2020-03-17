# This script close the focused window only if
# the process name is in the list below.
PROCESS = [	'pavucontrol',
						'blueman-manager',
						'arandr',
						'qalculate-gtk',
						'feh']

import subprocess
import os

if __name__ == "__main__":
	output = subprocess.check_output("xprop -id $(xdotool getwindowfocus) WM_CLASS", shell=True)
	array = output.split('\"')
	if array[1] in PROCESS:
		os.system("pkill " + array[1])
