#Client Gateway
#--------------

### Main Link

ip route add 161.189.40.210 via 192.168.36.1 dev wlp3s0 proto static
#ip route change default via 10.9.8.9 dev tun0 proto static

### GW

#ip route del default
#ip route add default gw 10.9.8.1

route del default
route add default gw 10.9.8.1
