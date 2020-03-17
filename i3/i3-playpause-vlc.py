# Play pause vlc
import subprocess
import os

if __name__ == "__main__":
	output = subprocess.check_output("xprop -id $(xdotool getwindowfocus) WM_CLASS", shell=True)
	array = output.split('\"')
	if array[1] == "vlc":
		os.system("qdbus org.mpris.MediaPlayer2.vlc /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause")
