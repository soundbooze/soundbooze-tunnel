## Masking Shadowsocks with Shapeshifter Pluggable Transport

- https://github.com/OperatorFoundation/shapeshifter-dispatcher

```
Install via SOCKS5 Proxy

git config --global http.proxy socks5://127.0.0.1:1080
http_proxy=socks5://127.0.0.1:1080 go get -u github.com/OperatorFoundation/shapeshifter-dispatcher/shapeshifter-dispatcher
```

### Server

```
shapeshifter-dispatcher -transparent -server -state state -orport 172.31.3.159:443 -transports obfs4 -bindaddr obfs4-0.0.0.0:80 -logLevel DEBUG -enableLogging -extorport 127.0.0.1:5747
```

### Client

Find 'cert' under state/

```
shapeshifter-dispatcher -transparent -client -state state -target 18.136.193.107:80 -transports obfs4 -proxylistenaddr 127.0.0.1:1080 -options '{"cert": "okrAH4rGDgptSaXZz1BS7hCzNEwCniHu8f73U5vdVCcJqsKc4Rl6nNlCY7EegjeY7oRiLg", "iat-mode": "0"}' -logLevel DEBUG -enableLogging
```

### Shadowsocks Server

```
{
    "server":"172.31.3.159",
    "server_port":443,
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

### Shadowsocks Client

```
{
    "server":"127.0.0.1",
    "server_port":1080,
    "local_address": "127.0.0.1",
    "local_port":5150,
    "password":"secretPassword",
    "timeout":300,
    "method":"aes-256-cfb",
    "fast_open": false,
    "workers": 1,
    "prefer_ipv6": false
}
```

### Test

```
curl --socks5 127.0.0.1:5150 http://ipinfo.io
```
