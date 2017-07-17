# Distributed Board

Requirements:

- `python >= 3.6`


## Setup

```shell
make setup
```

## Run

Start first the server

```shell
make run_server
```

Then start the board

```shell
make run_board
```

So send the messages to server with

```
python client 'Your Name' 'Your message'
```
or test with ping message `make send_ping`
