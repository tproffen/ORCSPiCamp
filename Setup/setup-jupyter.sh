#!/bin/bash

echo "**********************************************************"
echo " Installing Jupyter - sit back & relax :) "
echo "**********************************************************"
echo 

sudo pip3 install jupyter
sudo pip3 install jupyterlab
sudo pip3 install jupyterthemes

mkdir -p /home/pi/.jupyter
cd /home/pi/.jupyter

cat > jupyter_notebook_config.py <<EOF
# Configuration file for jupyter-notebook.
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.port = 5555
c.Notebook.open_browser = False
c.NotebookApp.quit_button = False
EOF

cat > jupyter.service << EOF
[Unit]
After=network.service

[Service]
ExecStart=/usr/local/bin/jupyter lab --config=/home/pi/.jupyter/jupyter_notebook_config.py
User=pi

[Install]
WantedBy=default.target
EOF

sudo mv jupyter.service /etc/systemd/system/
sudo systemctl enable jupyter.service
sudo systemctl start jupyter.service


echo "Finally we set the Jupyter password."
jupyter notebook password
