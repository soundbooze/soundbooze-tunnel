# Shadow Socks

A guideline for SOCK5 relay under Ubuntu (EC2 Instance)

- https://shadowsocks.org/en/index.html

### Server

service shadowsocks start

### Client

```
sslocal -c /etc/shadowsocks/config.json
```

### Config

```
{
    "server":"172.31.3.159",
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

### Test

```
curl --socks5 127.0.0.1:1080 http://ipinfo.io
```

or

Manual proxy configuration <b>(SOCKS Host) SOCKS v5</b>

### Relay

- https://github.com/shadowsocks/shadowsocks/wiki/Setup-a-Shadowsocks-relay
