#!/usr/bin/env python3
# Author: Diego Orozco
# Author ID: dorozco
# Date Created: 2025/05/28

import sys

if len(sys.argv) == 2:
    timer = int(sys.argv[1])
else:
    timer = 3

while timer > 0:
    print(timer)
    timer = timer - 1

print('blast off!')
