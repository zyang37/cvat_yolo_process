#!/bin/bash

if [ -z "$1" ]
then
	ipython setup.py
elif [ "$1" = "clean" ]
then
	rm -f obj.names
	rm -f train.data
	rm -f train.txt
	rm -f -r train/*
	rmdir train
	rm -f -r label/*
	rmdir label
else
	echo "invalid command"
fi
