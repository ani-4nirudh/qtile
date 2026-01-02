#!/bin/bash
# Path: ~/.config/qtile/monitor-hotplug.sh

USER="praani"
DISPLAY=":0"
XAUTHORITY="/home/$USER/.Xauthority"

# Give system 2 seconds to settle
sleep 2

export DISPLAY XAUTHORITY

# Display names
LAPTOP="eDP-1"
EXTERNAL=("DP-1" "DP-2" "DP-3" "DP-4" "HDMI-1")

# Check connected externals
CONNECTED=()
for port in "${EXTERNAL[@]}"; do
	if xrandr --query | grep -q "^$port connected"; then
		CONNECTED+=("$port")
	fi
done

if [ ${#CONNECTED[@]} -gt 0 ]; then
	# External display connected
	MAIN=${CONNECTED[0]}
	echo "$(date): External $MAIN connected, setting as primary" >> /tmp/monitor-hotplug.log

	su - "$USER" -c \
	"export DISPLAY=$DISPLAY XAUTHORITY=$XAUTHORITY; \
	xrandr --output $LAPTOP --mode 1920x1080 --rate 60 --right-of $MAIN --output $MAIN --mode 2560x1440 --primary --rate 60"

else
	echo "$(date): No external display, using laptop only" >> /tmp/monitor-hotplug.log

	su - "$USER" -c \
		"export DISPLAY=$DISPLAY XAUTHORITY=$XAUTHORITY; \
		xrandr --output $LAPTOP --mode 1920x1080 --primary --output DP-1 --off --output DP-2 --off --output DP-3 --off --output DP-4 --off --output HDMI-1 --off"
fi
