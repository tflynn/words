#!/usr/bin/env python

import sys
import os
from os import path

source_file=sys.argv[1]
if len(sys.argv) > 2:
    minimum_word_length = int(sys.argv[2])
else:
    minimum_word_length = 6

out_count = 0
with open(source_file) as word_file:
    for line in word_file.readlines():
        line = line.strip().replace("\n","")
        if len(line) >= minimum_word_length:
            out_count = out_count + 1
            print("{0},{1}".format(out_count,line))

