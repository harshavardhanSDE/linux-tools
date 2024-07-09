# linux-tools
A comprehensive list of Linux CLI tools, with examples.

[grep]() : Searching text within files, for example finding a specific string in a log file. <br>
[awk]() : Text processing and data extraction from files.<br>
[sed]() : stream editing for transforming text in a pipeline.<br>
[curl]() : Transferring data from or to a server, often used for making HTTP requests.<br>
[wget]() : Non-interactive network downloader, useful for retreiving files from the web.<br>
[ssh]() : Securely connecting to remote servers.<br>
[scp]() : Securely copying files between hosts on a network<br>
[rsync]() : Synchronizing files and directories between two locations.<br>
[tar]() : Archiving files into a single file and extracting files from an archive.<br>
[gzip]() : Compressing files.<br>
[top/htop]() : Displaying real-time system processes and resouce usage.<br>
[ps]() : Displaying information about active processes. <br>
[df]() : Displaying disk space usage.<br>
[du]() : Estimating file space usage.<br>
[netstat/ss](): Network statistics, useful for monitoring network connections and routing tables.<br>
[ping]() : Checking the connectivity between the local host and remote network host.<br>
[traceroute]() : Tracing the route packets take to reach a network host.<br>
[ip]() : Displaying and manipulating routing, network devices, interfaces, and tunnels.<br>
[iptables]() : Setting up, maintaining, and inspecting the tables of IP packet filter rules in the linux kernel<br>
[cron]() : Scheduling automated tasks to run at specified intervals. <br>
[systemcl]() : Managing system services.<br>

## grep
The `grep` command in linux is a powerful tool used for searching text using patterns. It has many options that can be combines to perform complex text searches.

### examples:
#### Basic usage:
```grep PATTERN FILE```

#### Options
`-i` : Ignores case distinctions. <br>
```grep -i "pattern" pattern.txt```

`-v`: Invert match, showing lines that do not match the pattern. <br>
```grep -v "pattern" pattern.txt```

`-c`: Count the number of matching lines. <br>
```grep -c "pattern" pattern.txt"```

`-l`: List file names with matches. <br> 
``` grep -l "pattern" *.txt ```

`-L`: List file names with the matchs. <br>
``` grep -L "pattern" *.txt```

`-n`: Show line numbers with output. <br>
``` grep -n "pattern" pattern.txt ```

`-r / -R`: Recursively search directories. <br>
``` grep -r "pattern" ~/patterns ```

`-w`: Match whole words <br>
``` grep -w "pattern" pattern.txt ```

`-x`: Match whole line. <br>
``` grep -x "pattern" pattern.txt ```

`-o`: Show only matched parts of a line. <br>
``` grep -o "pattern" pattern.txt ```

`-q`: Quiet mode ( no output, exit status indicates match)
``` grep -q "pattern" pattern.txt ```