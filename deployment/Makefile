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

format-sd-card: /dev/disk4
	diskutil unmountDisk disk4
	diskutil eraseDisk FAT32 SDCARD MBRFormat /dev/disk4

flash-hypriotos-on-sd-card: format-sd-card ../images/hypriotos-rpi-v1.11.1.img
	diskutil unmountDisk disk4
	sudo dd if=$(IMAGES_DIR)/hypriotos-rpi-v1.11.1.img of=/dev/disk4 bs=1024
	diskutil unmountDisk disk4

flash-robocarstore-on-sd-card: format-sd-card ../images/robocarstore_dk310_stretch.img
	diskutil unmountDisk disk4
	sudo dd if=$(IMAGES_DIR)/robocarstore_dk310_stretch.img of=/dev/disk4 bs=1024
	diskutil unmountDisk disk4
