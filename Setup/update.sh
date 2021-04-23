#!/bin/bash

echo "**********************************************************"
echo "Welcome to your 'orcspi'"
echo "**********************************************************"
echo 
echo "Updating .."

# Update distribtion
sudo apt-get update
#sudo apt-get -y upgrade

# Missing components here

# Cleaning up
sudo apt-get clean

