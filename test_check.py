#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
import sys
import sg5010

s=sg5010.Sg5010(4,0)

while True:
    print("Turn left ...")
    s.setdirection(100,10)
    time.sleep(0.5)
    print("Turn right ...")
    s.setdirection(-100,-10)
    time.sleep(0.5)
