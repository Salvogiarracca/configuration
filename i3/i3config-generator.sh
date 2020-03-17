#! /bin/bash

if [ $# -lt 1 ]; then
	echo "USAGE: $0 PATH"
	exit 1
fi

include_path=$1
i3_config="$HOME/.config/i3/config"

rm -f "$i3_config"

for f in "${include_path}"/*.conf; do
	echo -e "\n################## ${f} ##################\n" >> "${i3_config}"
	cat "${f}" >> "${i3_config}"
done
	

