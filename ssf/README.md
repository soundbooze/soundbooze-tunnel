# Secure Socket Funneling (SSF)

A guideline for Secure Socket Funneling under Ubuntu (EC2 Instance)

- https://securesocketfunneling.github.io/ssf/#home

### DEPS
```
apt-get install libssl1.0-dev libboost1.65 libboost-dev libkrb5-dev
apt-get install cmake g++
```

### Clone
```
git clone https://github.com/securesocketfunneling/ssf
cd ssf && git submodule update --init
```

### Build
```
mkdir build && cd build
cmake /root/ssf -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr/local
make && make install
```

## SERVER
```
ssfd -p 80 -c /usr/local/etc/config.json
```

## CLIENT

### SOCK5
```
ssf -D 1080 -p 80 18.136.193.107
```

### Copy
```
ssfcp -p 80 /etc/hosts 18.136.193.107@/tmp/footest
```
