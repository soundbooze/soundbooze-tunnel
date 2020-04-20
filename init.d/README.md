Shapeshifter Service

## Update rc.d

```
# update-rc.d shapeshifter-dispatcher defaults
```

## State Directory

```
# mkdir /state
# chmod 755 /state
# chown ubuntu.ubuntu /state
```

## Start stopping service

```
# systemctl enable shapeshifter-dispatcher
```

```
# service shapeshifter-dispatcher status
# service shapeshifter-dispatcher start
# service shapeshifter-dispatcher stop
```
