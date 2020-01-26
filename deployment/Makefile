#!/usr/bin/env bash

.SHELLFLAGS = -e -c
SHELL=/usr/local/bin/bash
ROOT_DIR=$$(dirname $$(pwd))
IMAGES_DIR=$(ROOT_DIR)/images

download-hypriot-rpi-image: ../images/hypriotos-rpi-v1.11.1.img
download-robocarstore-rpi-image: ../images/robocarstore_dk310_stretch.img

../images/hypriotos-rpi-v1.11.1.img:
	@wget https://github.com/hypriot/image-builder-rpi/releases/download/v1.11.1/hypriotos-rpi-v1.11.1.img.zip -O hypriotos-rpi-v1.11.1.img.zip
	@unzip hypriotos-rpi-v1.11.1.img.zip && rm hypriotos-rpi-v1.11.1.img.zip
	@mkdir -p $(IMAGES_DIR)
	@mv hypriotos-rpi-v1.11.1.img $(IMAGES_DIR)

../images/robocarstore_dk310_stretch.img:
	@wget https://www.dropbox.com/s/raw/z8uhfoetlxwpsua/robocarstore_dk310_stretch.img.gz -O robocarstore_dk310_stretch.img.gz
	@gunzip robocarstore_dk310_stretch.img.gz
	@mkdir -p $(IMAGES_DIR)
	@mv robocarstore_dk310_stretch.img $(IMAGES_DIR)

../images/robocarstore_dk310_stretch.img:
	@wget https://www.dropbox.com/s/raw/z8uhfoetlxwpsua/robocarstore_dk310_stretch.img.gz -O robocarstore_dk310_stretch.img.gz
	@gunzip 2019-09-26-raspbian-buster-lite.img.zip
	@mkdir -p $(IMAGES_DIR)
	@mv 2019-09-26-raspbian-buster-lite.img $(IMAGES_DIR)

format-sd-card: /dev/disk2
	@diskutil unmountDisk disk2
	@diskutil eraseDisk FAT32 RASP_SD MBRFormat /dev/disk2

flash-hypriotos-on-sd-card: format-sd-card ../images/hypriotos-rpi-v1.11.1.img
	@diskutil unmountDisk disk2
	@sudo dd if=$(IMAGES_DIR)/hypriotos-rpi-v1.11.1.img of=/dev/disk2 bs=1024
	@diskutil unmountDisk disk2

flash-robocarstore-on-sd-card: format-sd-card ../images/robocarstore_dk310_stretch.img
	@diskutil unmountDisk disk2
	sudo dd if=$(IMAGES_DIR)/robocarstore_dk310_stretch.img of=/dev/disk2 bs=1024
	@diskutil unmountDisk disk2

flash-raspbian-buster-on-sd-card: format-sd-card ../images/2019-09-26-raspbian-buster-lite.img
	@diskutil unmountDisk disk2
	sudo dd if=$(IMAGES_DIR)/2019-09-26-raspbian-buster-lite.img of=/dev/disk2 bs=1024
	@diskutil unmountDisk disk2

setup-wifi-credentials:
	@touch /Volumes/boot/ssh
	@echo -e "country=US\nctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev\nupdate_config=1\n\nnetwork={\n   ssid=\"iPhone de Baptiste\"\n   psk=\"oueskonva\"\n   priority=1\n   id_str=\"mobil\"\n}" > /Volumes/boot/wpa_supplicant.conf
	@echo -e "\nnetwork={\n   ssid=\"LesB0yz\"\n   psk=\"tutrouveraspas\"\n   priority=2\n   id_str=\"home\"\n}" >> /Volumes/boot/wpa_supplicant.conf
