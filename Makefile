.PHONY: setup run_server run_board send_ping

setup:
	pip install -r requirements.txt

run_server:
	python server

run_board:
	python board

send_ping:
	python client 'ping' 'pong'
