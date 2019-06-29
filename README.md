# pystebin
Your own command line based pastebin server in Python

<p align="center"><img src="example.gif"/></p>

#### How to use

Start the server:
```
$ sudo python3 pystebin.py
```

Use Netcat along with ```cat``` or ```echo``` to send data to server:
```
$ echo "Hello world!" | nc SERVER 9090
$ cat some_file | nc SERVER 9090
```

The server is configured to return a 5 digit string with the stored file ID. Use ```curl``` to see the contents:
```
$ curl http://SERVER/ACB5X
```
