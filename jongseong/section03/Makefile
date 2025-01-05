.PHONY: run volume build remove

volume:
	docker volume create section03

build:
	docker build -t section03 .

run:
	docker run -dit -p 8000:80 --name section03 -v section03:/api/files section03

remove:
	docker stop section03
	docker rm section03