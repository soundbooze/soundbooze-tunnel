openvpn --dev tun0 --ifconfig 10.9.8.1 10.9.8.2 --tls-server --dh /etc/openvpn/easy-rsa/keys/dh2048.pem --ca /etc/openvpn/easy-rsa/keys/ca.crt --cert /etc/openvpn/easy-rsa/keys/server.crt --key /etc/openvpn/easy-rsa/keys/server.key --reneg-sec 60 --verb 5 --port 500

iptables -F
iptables -F -t nat

IF_MAIN=eth0
IF_TUNNEL=tun0
YOUR_OPENVPN_SUBNET=10.9.8.0/24
iptables -A FORWARD -i $IF_MAIN -o $IF_TUNNEL -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables -A FORWARD -s $YOUR_OPENVPN_SUBNET -o $IF_MAIN -j ACCEPT
iptables -t nat -A POSTROUTING -s $YOUR_OPENVPN_SUBNET -o $IF_MAIN -j MASQUERADE
