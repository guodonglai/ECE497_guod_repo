# Here's how to use imagemagick to display text
# Make a blank image
SIZE=320x240
TMP_FILE=/tmp/frame.png

#place boris on the frame with some text on it.
convert tux.png.1 -fill black -font Times-Roman -pointsize 15\
        -resize $SIZE \
       	-draw "text 0,20 'By Donglai'" \
	-draw "text 0,40 'tux.png'"\
       	$TMP_FILE

#show frame
sudo fbi -noverbose -T 1 $TMP_FILE

