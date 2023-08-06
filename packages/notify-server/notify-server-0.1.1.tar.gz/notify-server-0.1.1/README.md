# Notify Server

*An event server with multiple interfaces*

This is an event server that can be interacted with via http and sockets.

## Usage

Start the server:
```bash
notify-server localhost:8080 localhost:9000
```
Subscribe to an event via cli:
```bash
notify-client localhost:9000 receive terminal_event
```

Subscribe to an event via Python:
```python
from notify_cli import NotifyClient
client = NotifyClient('localhost', 9000)
client.subscribe('python_event', lambda event: print('Event:', event))

while True:
    sleep(1)
```

Send an event via cli:
```bash
notify-client localhost:9000 send python_event 'hello, from the cli'
```

Send an event via Python:
```python
from notify_cli import NotifyClient
client = NotifyClient('localhost', 9000)
client.send('terminal_event', 'hello from python')

while True:
    sleep(1)
```

Send an event via Curl:
```bash
curl -X POST http://localhost:8080/event/terminal_event -d "hello from the web"
```


## Installation

Dependencies:

 - [ruko-server](http://github.com/rukodb/ruko-server)
 
```bash
git clone http://github.com/rukodb/ruko-server
cd ruko-server && mkdir build && cd build
cmake .. && make -j4
sudo make install  # Make sure you install it to your PATH
```

Installation:

```bash
pip install notify-server  # Inside a virtualenv is recommended
```

If you are using the client code in a project you only need:
```bash
pip install notify-client
```
