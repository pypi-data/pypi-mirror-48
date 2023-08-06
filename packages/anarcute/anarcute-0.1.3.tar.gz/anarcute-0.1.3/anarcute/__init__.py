#!/usr/bin/env python3
import sys, os
import hy
this_dir, this_filename = os.path.split(__file__)
DATA_PATH = os.path.join(this_dir, "", "lib.hy")
hy.eval(hy.read_str(open(DATA_PATH,"r+").read()))