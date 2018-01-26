# Installiere:
# - fhem
# - mosquitto
# - mysql
# - fhemExtended
# - alexa-fhem

ip="$(ifconfig | grep -A 1 'eth0' | tail -1 | cut -d ':' -f 2 | cut -d ' ' -f 1)"

echo "Installiere fhem-docker"
docker-compose up -d
echo "FHEM ist wurde installiert! Der Server ist unter http://$ip:8083/ erreichbar.\n" 
 
echo "Installiere portainer"
docker run -d --name portainer -p 9000:9000 -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer
echo "Portainer wurde installiert! Der Server ist unter http://$ip:9000/ erreichbar."
