	#!/bin/bash

# Check if vlc is running
# In that case disable dpms and kill xautolock

# -x flag only match processes whose name (or command line if -f is
# specified) exactly match the pattern.

running=true

exec /home/giuseppe/.config/i3/caffeine-script/xautolock-command.sh &
if mkdir /var/lock/.caffeine-script-00
then
	while :
	do
		if pgrep -x "vlc" > /dev/null
		then
		    echo "Running"
			if [ "$running" = false ] ; then
				xset -dpms
				pkill xautolock
			fi
			running=true
		else
		    echo "Stopped"
			if [ "$running" = true ] ; then
				xset +dpms
				exec /home/giuseppe/.config/i3/caffeine-script/xautolock-command.sh &
			fi
			running=false
		fi

		sleep 290
	done

rmdir /var/lock/.caffeine-script-00
fi
