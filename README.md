# Caeborg Discord Bot

This is a custom Discord Bot written in Python that contains learning tools and quick access utilities.

## Installation

`git clone https://github.com/dtasada/CaeborgDiscordBot ~/Caeborg
cp ~/Caeborg/sys/.bashrc ~/
cp ~/Caeborg/sys/caeborg.service /etc/systemd/system/caeborg.service
echo "$USER ALL=(root) NOPASSWD: /bin/systemctl" > /etc/sudoers.tmp
sudo -n systemctl-daemon reload
sudo -n systemctl start --now caeborg`
