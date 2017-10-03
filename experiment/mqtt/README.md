# Warning

We want to make sure we test thsi on vanilla machine. POssibly raspberry is good, or VM
This is to avoid security issues

# Server

https://mosquitto.org/download/

Documentation

https://mosquitto.org/documentation/
https://github.com/mqtt/mqtt.github.io/wiki


    mosquitto -c mosquitto.conf

# On OSX

This is just a collection and needs to be looked at more carefully for security reasons. Do not modify the firewall so only localhost can at this time comnnect.

https://simplifiedthinking.co.uk/2015/10/03/install-mqtt-server/

Install

    brew install mosquitto

THis will give you a number of files located in various driectories.

* Configuration file: 

        /usr/local/etc/mosquitto/mosquitto.conf

* Management programs

        /usr/local/bin/mosquitto_passwd
        /usr/local/bin/mosquitto_pub
        /usr/local/bin/mosquitto_sub

* Server program

        /usr/local/sbin/mosquitto


If you like to use the defauklt settings start the server with

    /usr/local/sbin/mosquitto

To test the server use

    python test.py

If you like to mofiy the config file copy it in your local directory, modify and start the server with

    cp /usr/local/etc/mosquitto/mosquitto.conf mosquitto.conf
    mosquitto -c mosquitto.conf


# public brokers

https://github.com/mqtt/mqtt.github.io/wiki/public_brokers

# Raspberry

https://mosquitto.org/2013/01/mosquitto-debian-repository/
https://learn.adafruit.com/diy-esp8266-home-security-with-lua-and-mqtt/configuring-mqtt-on-the-raspberry-pi

Passwords

http://www.steves-internet-guide.com/mqtt-username-password-example/


# Commandline Ussage

In one window say

    mosquitto_sub -t topic/state

In another window, send a message to the server so it can be picked up by the subscriber.

    mosquitto_pub -t topic/state -m "Hello World"


# Automatic launch after boot

NOT recommended at this time

To start the MQTT server on startup.

    ln -sfv /usr/local/opt/mosquitto/*.plist ~/Library/LaunchAgents

The server can be started now by running

    launchctl load ~/Library/LaunchAgents/homebrew.mxcl.mosquitto.plist

MIssing does not document how to stop or remove


Homebrew updates

Fix homewbrow with

    brew doctor

Watch the output carefully and fix things. On my machine I needed to do 

    brew prune
    brew install openssl@1.1

add sbin to ~/.bashrc file if it is missing
    
    echo 'export PATH="/usr/local/sbin:$PATH"' >> ~/.bash_profile
