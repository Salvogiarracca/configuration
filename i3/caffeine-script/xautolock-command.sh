#! /bin/bash
time=10
for i in "$@"
do
	time=$i
done

# Suspend the pc after the time in minute
xautolock -detectsleep -time $time -locker '/home/giuseppe/.config/i3/i3lock-command.sh' -notify 30 -notifier 'notify-send -u critical "SCREEN LOCKING..." "The screen will lock in 30 seconds"'
