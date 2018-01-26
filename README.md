# fhem-docker
This is Docker project for the Raspberry Pi3(arm64) including the following containers:
 - fhem
 - mqtt
 - alexa 
 - fhemExtended (python-interface)

## Installtion
#### Requirements
You need a working Docker environment(including the package docker-compose). For example you can use the already prebuild [Hypriot Docker Images](https://blog.hypriot.com/downloads/). 
Or you can just install Docker with this command `curl -sSL https://get.docker.com | sh`.

Dont forget to enable SPI. This can be achieved by adding `dtparam=spi=on` to the `config.txt` if your using the Hypriot Image or via `sudo raspi-config` and then enable SPI interface: `Interfacing Options > P4 SPI > Yes` if your using a standard [Raspbian Image](https://www.raspberrypi.org/downloads/raspbian/).

#### Install container
To install this container run the following command, after you are logged in into your Raspberry Pi via ssh:
```
cd rpi-fhem-docker
source install.sh
```
The installation process might take a little longer. But afterwards you are presented a fully working fhem homeautomation server ready to control Sonoff devices with Amazon Alexa.

Have fun 🙂
