import subprocess
import os
import sys

# output = subprocess.check_output("xprop -id $(xdotool getwindowfocus) WM_CLASS", shell=True)
# array = output.split('\"')
# if array[1] == "vlc":
if True:
    if sys.argv[1] == "PlayPause":
        os.system("qdbus org.mpris.MediaPlayer2.vlc /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause")
    elif sys.argv[1] == "Seek":
        time = int(sys.argv[2]) * 1000000
        os.system("qdbus org.mpris.MediaPlayer2.vlc /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Seek {}".format(time))

                
