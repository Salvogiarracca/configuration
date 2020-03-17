#BATTERY SAVER SCRIPT
# battery_saver [N]
# N:
#  - 0 Disabled
#  - 1 Balanced
#  - 2 Extreme Power Saving
#  - 3 Film Mode
#  - 4 Docking Mode

for i in "$@"
do
	case 0 in
		$i )
		echo BATTERY SAVING MODE: DISABLED
		notify-send "Battery saving mode" "DISABLED"
		
		if ! systemctl status bluetooth | grep --perl-regexp "(?<=Active: )active" > /dev/null 2>&1 ; then
			echo "ENABLING BLUETOOTH"
			sudo systemctl start bluetooth
		fi

		if ! pgrep blueman-applet > /dev/null 2>&1; then
			echo "STARTING blueman-applet"
			blueman-applet&
		fi
		
		if ! pgrep megasync > /dev/null 2>&1 ; then
			echo "STARTING megasync"
			megasync&
		fi


		if ! pgrep lightsOn > /dev/null 2>&1 ; then
			echo "STARTING lightsOn"
			./lightsOn.sh &
		fi

		echo "SETTING BACKLIGHT:50%"
		xbacklight -set 50

		if ! systemctl status NetworkManager | grep --perl-regexp "(?<=Active: )active" > /dev/null 2>&1 ; then
			#NetworkManager is not "active"
			echo "ENABLING NetworkManager"
			sudo systemctl start NetworkManager

			echo "STARTING nm-applet"
			#Do not remove the sleep, otherwise nm-applet won't detect the connection
			sleep 1
			nm-applet &
		fi

		if ! systemctl status wpa_supplicant | grep --perl-regexp "(?<=Active: )active" > /dev/null 2>&1 ; then
			#NetworkManager is not "active"
			echo "ENABLING wpa_supplicant"
			sudo systemctl start wpa_supplicant
		fi

		echo "SETTING DPMS TIME TO 300 300 300"
		xset dpms 300 300 300

		# if ! pgrep compton > /dev/null 2>&1 ; then
		# 	echo "STARTING compton"
		# 	compton -f -D 5 &
		# fi

		echo "SETTING LOCKSCREEN AFTER 10 mins"
		pkill xautolock
		/home/giuseppe/.config/i3/caffeine-script/xautolock-command.sh &
			;;
	esac
	case 1 in
		$i )
		echo BATTERY SAVING MODE: 1
		notify-send "Battery saving mode" "ENABLED MODE 1"

		echo "DISABLING BLUETOOTH"
		sudo systemctl stop bluetooth
		
		echo "KILLING blueman-applet"
		pkill blueman-applet
		
		echo "KILLING bluetoothd && obexd"
		pkill bluetoothd
		pkill obexd
		
		echo "KILLING megasync"
		pkill megasync

		echo "SETTING BACKLIGHT:10%"
		xbacklight -set 10

		echo "KILLING lightsOn"
		pkill lightsOn

		if ! systemctl status NetworkManager | grep --perl-regexp "(?<=Active: )active" > /dev/null 2>&1 ; then
			#NetworkManager is not "active"
			echo "ENABLING NetworkManager"
			sudo systemctl start NetworkManager

			echo "STARTING nm-applet"
			#Do not remove the sleep, otherwise nm-applet won't detect the connection
			sleep 1
			nm-applet&
		fi

		echo "SETTING DPMS TIME TO 60 60 60"
		xset dpms 60 60 60

		echo "SETTING LOCKSCREEN AFTER 7 mins"
		pkill xautolock
		/home/giuseppe/.config/i3/caffeine-script/xautolock-command.sh 7 &
			;;
	esac
	case 2 in
		$i )
		echo BATTERY SAVING MODE: 2
		notify-send "Battery saving mode" "ENABLED MODE 2"

		echo "DISABLING NetworkManager"
		sudo systemctl stop NetworkManager

		echo "KILLING nm-applet"
		pkill nm-applet

		echo "DISABLING wpa_supplicant"
		sudo systemctl stop wpa_supplicant

		echo "DISABLING bluetooth"
		sudo systemctl stop bluetooth
		
		echo "KILLING blueman-applet"
		pkill blueman-applet
		
		echo "KILLING bluetoothd && obexd"
		pkill bluetoothd
		pkill obexd
		
		echo "KILLING megasync"
		pkill megasync

		echo "SETTING BACKLIGHT:5%"
		xbacklight -set 5

		echo "KILLING lightsOn"
		pkill lightsOn

		echo "SETTING DPMS TIME TO 25 25 25"
		xset dpms 25 25 25

		# echo "KILLING compton"
		# pkill compton

		echo "SETTING LOCKSCREEN AFTER 5 mins"
		pkill xautolock
		/home/giuseppe/.config/i3/caffeine-script/xautolock-command.sh 5 &
			;;
	esac
	case 3 in
		$i )
		echo BATTERY SAVING MODE: 3: FILM MODE
		notify-send "Battery saving mode" "ENABLED MODE 3 - FILM MODE"

		echo "DISABLING bluetooth"
		sudo systemctl stop bluetooth

		echo "KILLING blueman-applet"
		pkill blueman-applet

		echo "KILLING bluetoothd && obexd"
		pkill bluetoothd
		pkill obexd

		echo "KILLING megasync"
		pkill megasync

		echo "SETTING DPMS TIME TO 5 MIN"
		xset dpms 300 300 300

		echo "DISABLING LOCKSCREEN"
		pkill xautolock
			;;
	esac
	case 4 in
		$i )
		echo BATTERY SAVING MODE: 4: DOCKING STATION MODE
		notify-send "Battery saving mode" "ENABLED MODE 4 - DOCKING STATION MODE"

		echo "SETTING DPMS TIME TO 5 MIN"
		xset dpms 300 300 300

		echo "SETTING LOCKSCREEN AFTER 10 mins"
		pkill xautolock
		/home/giuseppe/.config/i3/caffeine-script/xautolock-command.sh 10 &
			;;
	esac
done