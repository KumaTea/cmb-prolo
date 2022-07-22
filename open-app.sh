#!/bin/sh

# set -ex

# open app
# monkey -p cmb.pb -c android.intent.category.LAUNCHER 1
monkey -p cmb.pb 1
sleep 5  # wait for app to load

# open login page
input tap 960 270  # account
sleep 1
input tap 540 1500  # cancel fingerprint
sleep 1
input tap 540 1560  # more
sleep 1
input tap 540 1800  # password
sleep 1
