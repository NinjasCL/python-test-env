IMAGE = ninjas-py-env
RUN = docker run --rm -it --mount src="$(shell pwd)/src",target=/src,type=bind $(IMAGE)

b build:
	docker build -f Dockerfile -t $(IMAGE) .
f format:
	$(RUN) black .
r run:
	$(RUN)
s shell:
	$(RUN) /bin/bash
t test:
	$(RUN) pytest
