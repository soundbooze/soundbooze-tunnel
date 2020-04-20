#!/bin/sh

export PATH=$PATH:/home/ubuntu/go/bin
chisel client --auth user:pass --fingerprint 6e:34:f7:59:0a:2f:2b:19:ed:15:55:c0:4e:93:ef:64 18.136.193.107:443 socks
sleep 2

openvpn --config config.conf &
sleep 5

ip route add 18.136.193.107 via 192.168.36.1 dev wlp3s0 proto static
ip route change default via 10.9.8.9 dev tun0 proto static
