# checkalive

检查系统状态，如：

- 指定的IP地址是否存在。
- 指定的端口是否被监听。
- 指定的进程是否存活。

# 安装

```
    pip install checkalive
```

# 安装的可执行程序

- checkalive
- checkip
- checkport
- checkproc

# 程序帮忙信息

- checkalive

各种检查命令的包装程序。通过子命令指定特别的检查类型。

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

检查指定的IP地址是否存在。

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

检查指定的端口是否被监听。

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

检查指定的进程是否存活。

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