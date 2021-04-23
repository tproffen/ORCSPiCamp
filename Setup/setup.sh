#!/bin/bash

echo "**********************************************************"
echo "Welcome to your 'orcspi'"
echo "**********************************************************"
echo 
echo "Let us setup your Raspberry Pi Zero. "
echo "Sit back and relax - this will take several minutes."
echo 

# Set new password
echo "Orcs2021\nOrcs2021" | passwd

# Update hostname
CUR_HOSTNAME=$(cat /etc/hostname)
NEW_HOSTNAME=orcspi

# Change the hostname
sudo hostnamectl set-hostname $NEW_HOSTNAME
sudo hostname $NEW_HOSTNAME

# Change hostname in /etc/hosts & /etc/hostname
sudo sed -i "s/$CUR_HOSTNAME/$NEW_HOSTNAME/g" /etc/hosts
sudo sed -i "s/$CUR_HOSTNAME/$NEW_HOSTNAME/g" /etc/hostname

# Display new hostname
echo "The new hostname is $NEW_HOSTNAME"

# Update distribtion
sudo apt-get update
sudo apt-get -y upgrade

# Python environment

sudo apt-get -y install git
sudo apt-get -y install python3-pip
sudo apt-get -y install python3-matplotlib python3-numpy

mkdir -p /home/pi/.jupyter
cp jupyter_notebook_config.py /home/pi/.jupyter/
sudo cp jupyter.service /etc/systemd/system/
sudo systemctl enable jupyter.service
sudo systemctl start jupyter.service

# Enviro setup
sudo pip3 install enviroplus
sudo raspi-config nonint do_i2c 0
sudo raspi-config nonint do_spi 0

# Copy examples from Github
# TBD

# Cleaning up
sudo apt-get clean

# Ask if reboot
while true; do
    read -p "Do you wish to reboot now?" yn
    case $yn in
        [Yy]* ) sudo reboot; break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done
