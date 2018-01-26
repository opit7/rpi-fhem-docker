FROM resin/rpi-raspbian:jessie 
MAINTAINER tif 

ENV TZ 'Europe/Berlin'

RUN apt-get update && apt-get install npm nodejs-legacy curl &&\
    apt-get clean\
     && apt-get -yq autoremove\
     && rm -rf /var/lib/apt/lists/*

RUN npm cache clean -f && npm install -g n &&\
    n stable

# Die gewünschte Version einkommentieren
#ADD ./core/images/alexa-fhem-0.3.5.tgz /
ADD ./core/images/alexa-fhem-0.4.4.tgz /

RUN mv package alexa-fhem && cd alexa-fhem &&\
	npm install && mkdir ~/.alexa

COPY ./config/ /alexa-fhem/

RUN ln -s /alexa-fhem/config.json ~/.alexa/config.json

COPY ./core/start.sh /alexa-fhem/

WORKDIR /alexa-fhem/

EXPOSE 3000
CMD ["bash","/alexa-fhem/start.sh"]
