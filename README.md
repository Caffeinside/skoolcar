# skoolcar
Project created for the Skool AI to participe in the IronCar autonomous car competition


## Car Bootstrapping

### Hardware

Tutorial followed: http://docs.robocarstore.com/ (documentation provided by the store we bought the car from)

### Software

Tutorial followed: https://docs.donkeycar.com/guide/install_software/ (official DonkeyCar documentation)

The car still need a better calibration.
Based on the connection on the servo controller:
- Steering channel: 1
- Throttle channel: 0
(Those can be changed in the config.py file.)

### Adding your wifi

The wifi config file is in: /etc/wpa_supplicant/wpa_supplicant.conf.
If you can't connect to an already configured network to modify this file, you can use an Ethernet cable: https://www.dexterindustries.com/howto/connecting-raspberry-pi-without-monitor-beginners/

### Connecting to the pi

1. Verify that you're sharing the same network: ping donkeypi.local
2. Connect via ssh: ssh pi@donkeypi.local
Password: skoolcar

### Turning off the pi

1. Run the following command: sudo shutdown -h now
2. Wait for the green light to turn off completey before you remove the power. Else you could damage the SSD reader.


## Next steps

- Use the IronCar simulator to run a first supervised approach based on a virtual dataset: https://pypi.org/project/simulateur-ironcar/ 



