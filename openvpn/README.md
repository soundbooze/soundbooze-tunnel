## Implementation Note

### OpenVPN Server

- In Server enable runtime IP forwarding:

```
echo 1 > /proc/sys/net/ipv4/ip_forward
```

```
iptables -F
iptables -F -t nat

IF_MAIN=eth0
IF_TUNNEL=tun0
YOUR_OPENVPN_SUBNET=10.9.8.0/24
iptables -A FORWARD -i $IF_MAIN -o $IF_TUNNEL -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables -A FORWARD -s $YOUR_OPENVPN_SUBNET -o $IF_MAIN -j ACCEPT
iptables -t nat -A POSTROUTING -s $YOUR_OPENVPN_SUBNET -o $IF_MAIN -j MASQUERADE
```

### OpenVPN Client

- In client set the proper routing

```
ip route add <server-ip> via <default-gw-ip> dev eth0 proto static
ip route change default via <vpnserver-tun-ip> dev tun0 proto static
```

## GFW

### obfsproxy/

Mask OpenVPN traffic using obfsproxy (Pluggable Transport)

### shapeshifter/

Mask OpenVPN traffic using shapeshifter (Pluggable Transport)

### chisel/

OpenVPN through HTTP Tunnel

___

## Non GFW

### tls/

OpenVPN via TLS

### static/

OpenVPN via static key

### test/

Client/Server OpenVPN plain connection testing

### cert/

Certification Generation

### ovpn/

Generate OVPN file

### conf/

Miscellaneous config files
