# scrot -B 5 /home/giuseppe/Pictures/Lockscreen/lock1.png; 
scrot /home/giuseppe/Pictures/Lockscreen/lock1.png; 
corrupter -mag 1 -boffset 10 -meanabber 5 /home/giuseppe/Pictures/Lockscreen/lock1.png /home/giuseppe/Pictures/Lockscreen/lock1.png
i3lock -i /home/giuseppe/Pictures/Lockscreen/lock1.png -t && systemctl suspend;
# i3lock -i /home/giuseppe/Pictures/Lockscreen/lock1.png -t
