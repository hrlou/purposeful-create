#!/usr/bin/env bash
if [ ! -f "./eula.txt" ]; then
    read -p "Do you agree to the Minecraft Server EULA? (y/N): " yn
    case $yn in 
        yes | y | Y ) echo "eula=true" > eula.txt;;
        * ) echo exiting...;
	        exit;;
    esac
fi
while true; do
    java @jvm_args.txt -jar server.jar --nogui
    echo Server restarting...
    echo Press CTRL + Z to stop.
done