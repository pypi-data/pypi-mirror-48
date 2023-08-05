# checkalive

Check system status.

- 检查系统IP地址绑定情况
- 检查系统端口监听情况
- 检查系统进程运行情况等。

# Install

```
    pip install checkalive
```

# Installed applications

- checkalive
- checkip
- checkport
- checkproc

# Application help

- checkalive

```
    E:\checkalive>checkalive --help
    Usage: checkalive [OPTIONS] COMMAND [ARGS]...

    Options:
    --help  Show this message and exit.

    Commands:
    checkip    Search for the given ip.
    checkport  Search for the given listening port.
    checkproc  Search for the given process.
```

- checkip

```
    E:\checkalive>checkip --help
    Usage: checkip [OPTIONS] IP

    Search for the given ip.

    Options:
    -i, --nic TEXT  Search the given network interfaces, can use multiple times.
                    Default to All.
    --help          Show this message and exit.
```

- checkport

```
E:\checkalive>checkport --help
Usage: checkport [OPTIONS] PORT

  Search for the given listening port.

Options:
  -i, --nic TEXT
  -p, --proto TEXT  One of all, tcp, tcp4, udp, udp4, inet, inet4, inet6,
                    tcp6, udp6. Default to tcp.
  --help            Show this message and exit.
```

- checkproc

```
E:\checkalive>checkproc --help
Usage: checkproc [OPTIONS]

  Search for the process. One of pid, pidfile, command must be given.

Options:
  -i, --pid INTEGER   Search by pid.
  -f, --pidfile TEXT  Search by pid written in pidfile.
  -c, --command TEXT  Search by command pattern.
  --help              Show this message and exit.
```