IMAGE = ninjas-py-env
RUN = docker run --rm -it --mount src="./src",target=/src,type=bind $(IMAGE)

b build:
	docker build -f Dockerfile -t $(IMAGE) .
f format:
	$(RUN) black .
g github:
	make build
	make test
r run:
	$(RUN)
s shell:
	$(RUN) /bin/bash
t test:
	$(RUN) pytest
