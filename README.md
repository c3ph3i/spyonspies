# SyOnSpies
[![](https://img.shields.io/badge/version-1.0.0-green.svg)](https://github.com/c3ph3i/spyonspies/releases/tag/1.0.0) [![](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/c3ph3i/spyonspies/blob/master/LICENSE)

------------

Turn on this program and start to spy on your spies.  When you run it, it will be executed every time, when someine unlock your PC

## Requirement
- Linux OS
- Installed Python
- Installed OpenCV2 for Python

## Installation

### Download
For first download the repo:
```bash
git clone https://github.com/c3ph3i/spyonspies
```

### Create environment
Go to /inc folder and rename **env.example.py** to **env.py**. Edit it.
For email sending you have to configure your SMPT connection. You can create free gmail account for it.

### Run
Once the configuration is complete, make executable **autorun.sh** file and run it.
```bash
chmod +x autorun.sh
./autorun.sh
```

Leave the terminal opened. Now lock the PC and unlock.

If you enabled photo saving and loggin, you can find it in /data folder


## IMPORTANT
Lock / unlock handling is working via **DBUS_SESSION_BUS_ADDRESS** global variable. Not all machines use it.

## Tested
- Kali Linux 2017.1
- Ubuntu 17.04

## Todo
- Load application on PC turning on and with PC lock/unlock handler feature
- Test on other machines, create  enviroment for each tested machine, where the application worked

### License
[MIT](https://github.com/c3ph3i/spyonspies/blob/master/LICENSE "MIT")


