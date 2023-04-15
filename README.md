# Caeborg Discord Bot

This is a custom Discord Bot written in Python that contains learning tools and quick access utilities. This project is designed to be run on a Linux server

## Prerequisites


## Installation

``` sh 
git clone https://github.com/dtasada/CaeborgDiscordBot ~/Caeborg
cp ~/Caeborg/sys/.bashrc ~/
cp ~/Caeborg/sys/caeborg.service /etc/systemd/system/caeborg.service
```

## Setup
If run on a Linux server, the setup is as follows:
``` sh
echo "$USER ALL=(root) NOPASSWD: /bin/systemctl" > /etc/sudoers.tmp
sudo -n systemctl-daemon reload
sudo -n systemctl start --now caeborg
```
If run locally, running `main.py` will do.
The Project is designed to only be run on your computer, and will have to be set up accordingly. Create a Discord bot using Discord Developers and paste the credentials into a file called `specs.json` in the root of the folder.
