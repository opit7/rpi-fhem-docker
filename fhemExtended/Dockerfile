FROM debian:jessie

MAINTAINER tif

ENV DEBIAN_FRONTEND noninteractive
ENV TERM xterm

# Install dependencies
RUN apt-get update && apt-get upgrade -y --force-yes && apt-get install -y --force-yes --no-install-recommends apt-utils
RUN apt-get -y --force-yes install \
apt-transport-https \
build-essential \
dfu-programmer \
git \
snmp \
snmpd \
sudo \
telnet \
vim \
wget \
nano \
python \
python-dev \
python-pip 

# Python Module
RUN pip install spidev \
fhem \
numpy

WORKDIR /opt/fhemExtended

COPY ./core/ .

CMD [ "python","-u","/opt/fhemExtended/fhemExtended.py" ]
