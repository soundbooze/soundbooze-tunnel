### obfsproxy

#### Server

```
(OpenVPN: Listen Port 80)
(obfsproxy: Listen Port 443)

# obfsproxy --log-file=obfsproxy.log --log-min-severity=info obfs3 --dest=127.0.0.1:80 server 0.0.0.0:443
```

#### server.conf

```
port 80
proto tcp
dev tun

ca      /home/ubuntu/cnsg/ca.crt
cert    /home/ubuntu/cnsg/server.crt
key     /home/ubuntu/cnsg/server.key
dh      /home/ubuntu/cnsg/dh.pem

server 10.9.8.0 255.255.255.0
ifconfig-pool-persist ipp.txt

keepalive 10 120

comp-lzo
persist-key
persist-tun

status /dev/null #/tmp/openvpn-status.log

push "redirect-gateway def1"
verb 3
client-to-client
duplicate-cn

```

#### Client

```
# obfsproxy --log-file=obfsproxy.log --log-min-severity=info obfs3 socks 127.0.0.1:1080
```

#### client.conf

```
client
dev tun
port 443
proto tcp

remote 18.136.193.107 443
nobind

ca ./ca.crt
cert ./client.crt
key ./client.key

comp-lzo
persist-key
persist-tun

verb 3

socks-proxy-retry
socks-proxy 127.0.0.1 1080

pull-filter ignore redirect-gateway
```
