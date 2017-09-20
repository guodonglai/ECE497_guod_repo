#!/bin/bash

#set configuration register to 0x84 to make POL=1 and in comparator mode
i2cset -y 1 0x48 1 0x84
i2cset -y 1 0x49 1 0x84
#set the Tlow to approximately 72F
i2cset -y 1 0x48 2 0x16
i2cset -y 1 0x49 2 0x16
#set the Thigh to approximately 75F
i2cset -y 1 0x48 3 0x18
i2cset -y 1 0x49 3 0x18



temp=`i2cget -y 1 0x48 0`
temp2=$(($temp*9/5+32))
echo "Temperature read from address 0x48 is" $temp2


temp=`i2cget -y 1 0x49 0`
temp1=$(($temp*9/5+32))
echo "Temperature read from address 0x49 is" $temp1

