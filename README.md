# Caeborg Discord Bot

This is a custom Discord Bot written in Python that contains learning tools and quick access utilities. This project is designed to be run on a Linux server

## Prerequisites
* Git - version 2.30+
* Python - version 3.9.2 is latest tested version. Upgrade at own risk.
* Pip - 20.3.4 is latest tested version. Upgrade at own risk.
The following python dependencies are also required:
* `pillow` - version 8.1.2  
* `better_profanity` - version 0.7.0  
* `colorama` - version 0.4.6  
* `discord` - version 1.7.3  
* `requests` - version 2.25.1  
* `pydictionary` - version 2.0.1  
These Python dependencies can be installed with `pip`. The package versions specified are the newest working tested and might cause incompatibility or broken code. Please install manually as we are working on a `setup.py` file. The `discord` library has been confirmed to break the bot in the newest version, which at the time of writing this is `2.2.2`.
``` sh
pip install pillow better_profanity colorama requests pydictionary discord==1.7.3
```


## Installation

``` sh 
git clone https://github.com/dtasada/CaeborgDiscordBot ~/Caeborg
cp ~/Caeborg/sys/.bashrc ~/
cp ~/Caeborg/sys/caeborg.service /etc/systemd/system/caeborg.service
```

## Setup
This project is designed to only be run on your computer, as we obviously do not host our own servers. To set up your own server or local instance, create a Discord bot using Discord Developers and paste the credentials into a file called `specs.json` in the root of the folder.  

If run on a dedicated Linux server, the setup is as follows:
``` sh
echo "$USER ALL=(root) NOPASSWD: /bin/systemctl" > /etc/sudoers.tmp
sudo -n systemctl-daemon reload
sudo -n systemctl start --now caeborg
```
If you do not want to set up a server, manually running `main.py` will do.
