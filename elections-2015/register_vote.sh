#!/bin/bash

echo "Registering $1"
RAND=`/usr/bin/apg -a 1 -M nl -n 1 -m 42 -x 42 -c cl_seed -E ghijklmnopqrstuvwxyz`
echo -e "\n$RAND" >> $1
CHECKSUM=`/usr/bin/md5sum $1 | awk -F' ' '{ print $1 }'`
mv $1 votes/${CHECKSUM}
echo $CHECKSUM
