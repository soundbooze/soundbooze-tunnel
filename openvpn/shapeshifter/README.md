### shapeshifter-dispatcher

- https://github.com/OperatorFoundation/shapeshifter-dispatcher

```
Install via SOCKS5 Proxy

git config --global http.proxy socks5://127.0.0.1:1080
http_proxy=socks5://127.0.0.1:1080 go get -u github.com/OperatorFoundation/shapeshifter-dispatcher/shapeshifter-dispatcher
```

#### Server

```
(OpenVPN: Listen Port 80)
(obfsproxy: Listen Port 443)

# shapeshifter-dispatcher -transparent -server -state state -orport 127.0.0.1:80 -transports obfs4 -bindaddr obfs4-0.0.0.0:443 -logLevel DEBUG -enableLogging -extorport 127.0.0.1:5747
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

Find 'cert' under state/

```
# shapeshifter-dispatcher -transparent -client -state state -target 18.136.193.107:443 -transports obfs4 -proxylistenaddr 127.0.0.1:1080 -options '{"cert": "ghf0QAijppskFaVYZcDPOTuLiD8f7lGopc/A1amMH5LYIL2fGLBgtmVewMkHKhBCCtyfLw", "iat-mode": "0"}' -logLevel DEBUG -enableLogging
```

#### client.conf

```
client
dev tun
port 1080
proto tcp

remote 127.0.0.1 1080
nobind

ca ./ca.crt
cert ./client.crt
key ./client.key

comp-lzo
persist-key
persist-tun

verb 3

pull-filter ignore redirect-gateway
```
