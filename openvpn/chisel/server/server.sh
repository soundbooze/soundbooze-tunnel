#!/bin/sh

# Chisel Server 

chisel server -p 443 --socks5 --key supersecret --auth user:pass

# TLS Server

nohup openvpn --config config.conf &

iptables -F
iptables -F -t nat

IF_MAIN=eth0
IF_TUNNEL=tun0
YOUR_OPENVPN_SUBNET=10.9.8.0/24
iptables -A FORWARD -i $IF_MAIN -o $IF_TUNNEL -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables -A FORWARD -s $YOUR_OPENVPN_SUBNET -o $IF_MAIN -j ACCEPT
iptables -t nat -A POSTROUTING -s $YOUR_OPENVPN_SUBNET -o $IF_MAIN -j MASQUERADE
