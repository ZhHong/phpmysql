#!/bin/sh

if [ ! -d "../outputServer" ];
	then
		mkdir "../outputServer"
fi

echo "---stringres---"
cd stringres
python start.py $3
cd ..