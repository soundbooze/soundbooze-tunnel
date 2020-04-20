# Chisel

TCP Tunnel over HTTP

### Server

```
chisel server -p 443 --socks5 --key supersecret --auth user:pass
```

### Client

```
chisel client --auth user:pass --fingerprint xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx <ip:port> socks
```

### Test

```
curl -x socks5h://localhost:1080 http://ipinfo.io
```

### Github

- https://github.com/jpillora/chisel
