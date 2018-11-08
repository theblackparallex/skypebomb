#!/bin/bash

if [ $(id -u) -ne 0 ]; then
	echo "The Installer Must ran as ROOT"
	exit 1
fi

reset
echo "INSTALl"
read varos

rm -r firefox &> /dev/null
rm -r base &> /dev/null
rm ngrok* &> /dev/null

mkdir base

echo ""



ARCH="$(arch)"
echo "Detecting Arch: ${ARCH}"
echo " "
chmod -R 777 ./
apt-get update -y  &> /dev/null | echo "UPDATING"

pip install selenium &> /dev/null
pip install Skype4py &> /dev/null

if [[ ${ARCH} == "i686" || ${ARCH} == "i686" ]]; then
	wget -O GECKO.tar.gz https://github.com/mozilla/geckodriver/releases/download/v0.18.0/geckodriver-v0.18.0-linux32.tar.gz &> /dev/null | echo "INSTALLING GECKODRIVER"
else
	if [[ ${ARCH} == "i386" || ${ARCH} == "i386" ]]; then
	        wget -O GECKO.tar.gz https://github.com/mozilla/geckodriver/releases/download/v0.18.0/geckodriver-v0.18.0-linux32.tar.gz &> /dev/null | echo "INSTALLING GECKODRIVER"
	else
	        wget -O GECKO.tar.gz https://github.com/mozilla/geckodriver/releases/download/v0.18.0/geckodriver-v0.18.0-linux64.tar.gz &> /dev/null | echo "INSTALLING GECKODRIVER"
	fi
fi


tar xvzf GECKO.tar.gz &> /dev/null | echo "EXTRACTING GECKODRIVER"
chmod +x geckodriver
mv geckodriver base/ | echo "MOVING GECKODRIVER TO THE RIGHT DIR"

if [[ ${ARCH} == "i686" || ${ARCH} == "i686" ]]; then
        wget -O firefox.tar.bz2 https://ftp.mozilla.org/pub/firefox/releases/52.9.0esr/linux-i686/en-US/firefox-52.9.0esr.tar.bz2 &> /dev/null | echo "DOWNLOADING FIREFOX"
else
	wget https://ftp.mozilla.org/pub/firefox/releases/52.9.0esr/linux-x86_64/en-US/firefox-52.9.0esr.tar.bz2 -O firefox.tar.bz2 &> /dev/null | echo "DOWNLOADING FIREFOX"
fi

tar xvjf firefox.tar.bz2 &> /dev/null | echo "EXTRACTING FIREFOX"
chmod -R 777 firefox/
mv firefox base/ &> /dev/null | echo "MOVING FIREFOX TO THE RIGHT DIR"

rm *.zip
rm *.tar.gz
rm *.tar.bz2

echo " "
echo "[DONE]"
