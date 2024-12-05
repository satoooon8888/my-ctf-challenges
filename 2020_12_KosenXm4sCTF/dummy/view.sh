#!/bin/sh
objdump -d dummy -M intel \
| grep -Pv "(add|sub|mov|cmp)    e.x," \
