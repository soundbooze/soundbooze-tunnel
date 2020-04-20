# IODINE

An alternative tunneling if all fails

## Installation

### Package

```
# apt-get install iodine
```

### Source

```
# git clone https://github.com/yarrick/iodine
# make && make install
```

## Domain Name (Optional)

```
t1              IN      NS      t1ns.mydomain.com.
t1ns            IN      A       SERVER_IP_ADDRESS
```

## Running DNS Tunnel

### Server

```
sudo iodined -f -c -P password 10.0.1.1 t1.mydomain.com &
```

### Client

```
sudo iodine -f -P password t1.mydomain.com &
```

Now the client has the tunnel ip 10.0.1.2 and the server has 10.0.1.1. Try pinging each other through the tunnel.

### Proxy

Create an SSH tunnel over the DNS tunnel
 
```
ssh -N -D 9999 user@10.0.1.1
```

### System Configuration

#### /etc/defaults/iodine

```
START_IODINED to true
IODINED_ARGS to -c 10.0.1.1 ourdomain.com
IODINED_PASSWORD to password
```

```
# service iodine start
```

### Public/Private Key

```
ssh-keygen -f ~/.ssh/id_rsa -q -P ""
```

<b>Passwordless</b>, Copy this key to your destination server.

```
cat ~/.ssh/id_rsa.pub
```

### Cron & Rsync

- https://opensource.com/article/17/11/how-use-cron-linux

```
rsync -avz -e "ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" --progress /root/bigfile.txt username@198.211.117.129:/
```

### Browser

Configure your proxy settings for socks 5 proxy localhost port 9999

### MySQL Replication

- https://www.toptal.com/mysql/mysql-master-slave-replication-tutorial
- https://www.digitalocean.com/community/tutorials/how-to-set-up-master-slave-replication-in-mysql
- https://www.proweb.co.id/articles/ict/setting_mysql_replication.html

### References

- https://davidhamann.de/2019/05/12/tunnel-traffic-over-dns-ssh/
- http://toddharris.net/blog/2005/10/23/rsyncing-through-an-ssh-tunnel/
- https://wiki.attie.co.uk/wiki/Tunnel_IP_through_DNS
