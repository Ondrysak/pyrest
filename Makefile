build:
	sudo docker build -t "pyrest-alpine:latest" .
container: build
	sudo docker run -d -p 5000:5000 pyrest-alpine
health: build
	sudo docker run -p 5000:5000 -d --rm --name pyrest-health --cpus="1" --memory="500m" --memory-swap="700m" --health-interval=1s --health-timeout=3s --health-retries=3 --health-cmd "curl 0.0.0.0:5000/status || exit 1" pyrest-alpine
swarmhealth: build
	sudo docker service create --name pyrest-swarm --replicas 2 -p 5000:5000 --health-interval=2s --health-timeout=10s --health-retries=3 --limit-memory="500m" --limit-cpu="1" --health-cmd "curl 0.0.0.0:5000/status || exit 1" pyrest-alpine
local: build
	pip install .
	flask run --host=0.0.0.0
tests:
	pytest
documentation:
	pydoc -p 1234
	
