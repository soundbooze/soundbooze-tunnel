# Pluggable Transport

```
                  5150           80                                  80
18.136.193.107 shadowsocks : shapeshifter ----- 161.189.40.210 : shapeshifter  
                                                                      |
                                                                      |------------ shadowsocks client :1080
```

# AWS SG [Global]

### shadowsocks

```

$ ssserver -c config.json

{
    "server":"127.0.0.1",
    "server_port":5150,
    "local_address": "127.0.0.1",
    "local_port":1080,
    "password":"secretPassword",
    "timeout":300,
    "method":"aes-256-cfb",
    "fast_open": false,
    "workers": 1,
    "prefer_ipv6": false
}
```

### shapeshifter-dispatcher

Direct Install

```
$ go get -u github.com/OperatorFoundation/shapeshifter-dispatcher/shapeshifter-dispatcher
```

```
$ shapeshifter-dispatcher -transparent -server -state state -orport 127.0.0.1:5150 -transports obfs4 -bindaddr obfs4-0.0.0.0:80 -logLevel DEBUG -enableLogging -extorport 127.0.0.1:5747
```

### iptables

Authorizing inbound traffic either from AWS or iptables

```
iptables -F
iptables -t nat -F
iptables -t mangle -F

iptables -A INPUT -p tcp -s 161.189.40.210/32 --dport 80 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
iptables -A OUTPUT -p tcp --sport 80 -m conntrack --ctstate ESTABLISHED -j ACCEPT
iptables -A INPUT -p tcp --destination-port 80 -j DROP
```

# AWS CN [Inside]

### shapeshifter-dispatcher

Install via SOCKS5 Proxy

```
$ git config --global http.proxy socks5://127.0.0.1:1080
$ http_proxy=socks5://127.0.0.1:1080 go get -u github.com/OperatorFoundation/shapeshifter-dispatcher/shapeshifter-dispatcher
```

```
$ shapeshifter-dispatcher -transparent -client -state state -target 18.136.193.107:80 -transports obfs4 -proxylistenaddr 172.31.32.94:80 -options '{"cert": "okrAH4rGDgptSaXZz1BS7hCzNEwCniHu8f73U5vdVCcJqsKc4Rl6nNlCY7EegjeY7oRiLg", "iat-mode": "0"}' -logLevel DEBUG -enableLogging
```

### darkstat

```
START_DARKSTAT=yes
INTERFACE="-i eth0"
PORT="-p 443"
FILTER="port 80"
```

### iptables

Authorizing inbound traffic either from AWS or iptables

```
iptables -F
iptables -t nat -F
iptables -t mangle -F

iptables -A INPUT -p tcp -s 18.136.193.107/32 --dport 443 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
iptables -A OUTPUT -p tcp --sport 443 -m conntrack --ctstate ESTABLISHED -j ACCEPT
iptables -A INPUT -p tcp --destination-port 443 -j DROP
```

# Clients

- Android 

- https://play.google.com/store/apps/details?id=com.github.shadowsocks&hl=en

- iOS

- https://apps.apple.com/us/app/sockswitch-shadowsocks-client/id1453207024

- Mac, Windows and Linux

- https://shadowsocks.org/en/download/clients.html

```

$ ssserver -c config.json

{
    "server":"161.189.40.210",
    "server_port":80,
    "local_address": "127.0.0.1",
    "local_port":1080,
    "password":"secretPassword",
    "timeout":300,
    "method":"aes-256-cfb",
    "fast_open": false,
    "workers": 1,
    "prefer_ipv6": false
}
```

### Non Root Port Binding

#### Add non-root binding capability

```
# setcap cap_net_bind_service=+ep /usr/local/bin/shapeshifter-dispatcher
```

#### Remove non-root binding capability

```
# setcap cap_net_bind_service=-ep /usr/local/bin/shapeshifter-dispatcher
```

### SysV Init

- https://bitbucket.org/hananto88/88tuneling-ssf/src/master/init.d/

# Horizontal Scaling

- https://aws.amazon.com/elasticloadbalancing/
- https://www.amazonaws.cn/en/elasticloadbalancing/
