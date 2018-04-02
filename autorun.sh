#!/bin/bash

pid=$(pgrep sessio)

export DBUS_SESSION_BUS_ADDRESS=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/${pid}/environ|cut -d= -f2-)

DIR=$(dirname $([ -L $0 ] && readlink -f $0 || echo $0))

# First execute. Let you to know who turned on your comp
# python $DIR/spy.py

# Handle unlocking
dbus-monitor --session "type='signal',interface='org.gnome.ScreenSaver'" |
  while read x; do
    case "$x" in 
      *"boolean false"*) python $DIR/spy.py;;  
    esac
  done
