#!/usr/bin/bash

cd /home/vagrant/
git clone https://github.com/bundestag/gesetze.git

while true
do
    cd /home/vagrant/gesetze
    git pull
    sleep 5d
done