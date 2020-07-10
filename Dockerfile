FROM python:3.8
RUN pip install --no-cache-dir typing-extensions pytest black
WORKDIR /src

# https://github.com/adriancooney/Taskfile
COPY ./src/Taskfile.sh ./
RUN chmod +x ./Taskfile.sh
RUN echo "alias run=./Taskfile.sh" >> /root/.bashrc