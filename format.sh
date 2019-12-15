#!/bin/bash
find mhs5200 -name "*.py" | xargs -n1 -P8 pyupgrade --py37-plus
find mhs5200 -name "*.py" | xargs -n1 -P8 reorder-python-imports --py37-plus
find mhs5200 -name "*.py" | xargs -n1 -P8 black --target-version py37

