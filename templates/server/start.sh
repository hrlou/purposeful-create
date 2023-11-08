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
    java -Xms4000M -Xmx4000M -XX:+UseG1GC -XX:G1HeapRegionSize=4M -XX:+UnlockExperimentalVMOptions -XX:+ParallelRefProcEnabled -XX:+AlwaysPreTouch -XX:MaxInlineLevel=15 -jar server.jar --nogui
    echo Server restarting...
    echo Press CTRL + Z to stop.
done