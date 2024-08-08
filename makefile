run:
	podman-compose -f docker/docker-compose.yml up

stop:
	podman-compose -f docker/docker-compose.yml down

build:
	podman build -t oxford -f ./docker/Dockerfile

