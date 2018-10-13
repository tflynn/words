#!/usr/bin/env python

import sys
import json
source_file=sys.argv[1]

dict_by_pos = {}
with open(source_file) as word_file:
    for line in word_file.readlines():
        line = line.strip().replace("\n","")
        pos, word = line.split(",")
        dict_by_pos[pos] = word

print(json.dumps(dict_by_pos))

