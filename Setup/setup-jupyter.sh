#!/bin/bash

echo "**********************************************************"
echo " Installing Jupyter - sit back & relax :) "
echo "**********************************************************"
echo 

sudo pip3 install jupyter
sudo pip3 install jupyterlab
sudo pip3 install jupyterthemes

cat > jupyter.service << EOF
[Unit]
After=network.service

[Service]
ExecStart=/usr/local/bin/jupyter lab --ip 0.0.0.0 --port 5555 --no-browser --ServerApp.root_dir='/home/pi/'
User=pi

[Install]
WantedBy=default.target
EOF

sudo mv jupyter.service /etc/systemd/system/
sudo systemctl enable jupyter.service
sudo systemctl start jupyter.service


echo "Finally we set the Jupyter password."
jupyter notebook password
