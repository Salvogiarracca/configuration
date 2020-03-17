# i3-config  
  
## Script description  
.  
├── battery_saver.sh							Script with different configurations battery saving.  
│  
├── blur										│	Application that adds blur to an image.  
├── blur.c										│	Not required for this i3 configuration  
│  
├── caffeine-script								│	DEPRECATED  
│   ├── caffeine-script.sh						│	Script that cheks if vlc is open and prevents  
│   └── xautolock-command.sh					│	the monitor from turning off.  
│  
├── CheatsheetsViewer							│	GTK application that shows a list of cheatsheets  
│   ├── CheatsheetMenu.py						│	  
│   └── Cheatsheet_viewer.sh					│	This file contains the path for the cheatsheets  
│  
├── colorschemes								│	Folder that contains various colorschemes  
│   ├── default-gray							│	To set a colorscheme, copy the related file in config.d	  
│   │   └── 15-colorscheme.conf					│	and compile again the config.  
│   └── half-life								│  
│       ├── 15-colorscheme.conf					│	Some themes uses a .Xresources file to set the terminal colors  
│       └── background.png						│  
│  
├── config										│	Compiled version of config.d files  
│  
├── config.d									Directory with config files  
│   ├── 00-core.conf  
│   ├── 10-workspaces.conf  
│   ├── 15-colorscheme.conf  
│   ├── 20-keypad.conf  
│   ├── 30-for-window-properties.conf  
│   ├── 40-audio-brightness.conf  
│   ├── 41-keybinds.conf  
│   ├── 42-autorun.conf  
│   ├── 45-gaps.conf  
│   └── 50-misc.conf  
│  
├── dependencies.txt  
│  
├── i3blocks									│	i3blocks config files and plugin  
│   ├── battery									│  
│   └── spotify.py								│  
├── i3blocks.conf								│  
│  
│  
├── i3-close-focused-window.py					Script to close the focused window if present in a whitelist. (Works with a keybind Mouse3 by default)  
├── i3config-generator.sh						Script that takes the config.d and generates config  
├── i3-exit.py									GTK application for poweroff, reboot etc...  
├── i3lock-command.sh							Command for locking and suspend  
├── i3-master-slave-layout.py					Doesn't work well... to be improved  
├── i3-playpause-vlc.py							Command for play/pause vlc with dbus  
├── i3-swap-workspace-between-screens.py		In a 2 monitor setup, swaps the two workspaces between monitors  
├── i3-switch-if-workspace-empty				Switch to a previously used workspace if the current become empty. Supports multi-monitor setup with a flag  
├── i3-vlc-remote.py							Command for play/pause vlc with dbus  
├── LayoutMenu.py								GTK application that let you choose the layout for your monitors. The path for the layouts is in the script.  
├── lightsOn.sh									Script that prevents screensaver and locking if a media is playing.  
├── README.md  
├── sleep-script								│	Script that manages battery level and critical actions  
│   ├── sleep-conf.sh							│	  
│   └── sleep-daemon.sh							│  
├── TaskApp.py									GTK application for tasks		  
├── update-system								Script to update mirrors and pacman packages  
└── wallpaper_saver.sh							If used with background_changer let you save the background you are currently using.  
  

