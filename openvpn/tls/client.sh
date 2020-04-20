SERVER_IP="161.189.40.210"
DIR="/home/oche/Configuration/OpenVPN/cert/cert"
openvpn --remote $SERVER_IP --dev tun0 --ifconfig 10.9.8.2 10.9.8.1 --tls-client --ca $DIR/ca.crt --cert $DIR/client.crt --key $DIR/client.key --reneg-sec 60 --verb 5 --port 500
