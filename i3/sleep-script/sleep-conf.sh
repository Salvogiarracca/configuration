#!/bin/bash

SLEEP_TIME=600   # Default time between checks.
SAFE_PERCENT=40  # Still safe at this level.
DANGER_PERCENT=30  # Warn when battery at this level.
CRITICAL_PERCENT=20  # Suspend when battery at this level.

#NAGBAR_PID=0
#export DISPLAY=:0.0

function sendNotification
{
	notify-send -u critical  "BATTERY LOW!" "Please suspend before damaging the battery"
    #i3-nagbar -m 'Battery low!' -b 'Suspend!' 'i3lock -i /home/giuseppe/Pictures/Lockscreen/simple_lockscreen.png;systemctl suspend' >/dev/null 2>&1 &
    #NAGBAR_PID=$!
}

function killNagBar
{
    if [[ $NAGBAR_PID -ne 0 ]]; then
        ps -p $NAGBAR_PID | grep "i3-nagbar"
        if [[ $? -eq 0 ]]; then
            kill $NAGBAR_PID
        fi
        NAGBAR_PID=0
    fi
}

if pgrep -x "sleep-daemon.sh" > /dev/null
then
	echo "Already running. Exiting..."
else
	exec /home/giuseppe/.config/i3/sleep-script/sleep-daemon.sh &
	while [ true ]; do

	    if [[ -n $(acpi -b | grep -i discharging) ]]; then
	        rem_bat=$(acpi -b | grep -Eo "[0-9]+%" | grep -Eo "[0-9]+")
	        if [[ $rem_bat -gt $SAFE_PERCENT ]]; then
	            SLEEP_TIME=600
	        else
	            SLEEP_TIME=300
	            if [[ $rem_bat -le $DANGER_PERCENT ]]; then
	                SLEEP_TIME=120
	                sendNotification
	            fi
	            if [[ $rem_bat -le $CRITICAL_PERCENT ]]; then
	                SLEEP_TIME=300
					#TODO: execute xautolock-command instead of the next line
					i3lock -i /home/giuseppe/Pictures/Lockscreen/simple_lockscreen.png
	                systemctl suspend
	            fi
	        fi
	    else
	        SLEEP_TIME=600
	    fi

	    sleep ${SLEEP_TIME}s

	done
fi
