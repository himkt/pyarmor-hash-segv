#!/bin/bash

for i in {1..10}; do
    printf "Trial %2d: " $i
    rm -rf dist
    uv run pyarmor gen -O dist -i src/pyarmor_segv >/dev/null 2>&1 || exit 1
    PYTHONPATH=./dist uv run python minimal_reproducer.py #>/dev/null 2>&1
    [ $? -eq 139 ] && echo "SEGFAULT ✗" || echo "Normal ✓"
done
