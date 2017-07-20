#!/bin/bash

# screen position
screen_geometry="$(xrandr -d "${DISPLAY}" --query | grep ' primary ' | sed -n '1p' | grep -o -e '[0-9]\+x[0-9]\+')"
screen_width="$(echo "${screen_geometry}" | cut -d'x' -f1)"
screen_height="$(echo "${screen_geometry}" | cut -d'x' -f2)"

# dmenu width and height
width=700
height=$(( 20 * 18 ))

# execute dmenu
echo -e "$@" | dmenu -f -i -spotlight -p '' -l 20 -x $(((${screen_width} - ${width}) / 2)) -y $(((${screen_height} - ${height}) / 2)) -w ${width} -sb '#FFBDBDBD' -sf '#000000' -nb '#FFDBDBDB' -nf '#000000' -fn 'Terminesspowerline:size=18'
