#!/bin/bash
# From https://github.com/adriancooney/Taskfile


function start {
    python
}

function format {
    black .
}

function test {
    pytest ${@}
}

function test:file {
    FILENAME=$1
    pytest "test/test_$FILENAME.py"
}

function test:file:fn {
    FILENAME=$1
    shift
    PARAMS="${@}"
    pytest "test/test_$FILENAME.py" -k "'$PARAMS'"
}

function default {
    # Default task to execute
    start
}

function help {
    echo "$0 <task> <args>"
    echo "Tasks:"
    compgen -A function | cat -n
}

TIMEFORMAT="Task completed in %3lR"
time ${@:-default}