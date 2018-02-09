#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 22:23:52 2017

@author: BhavikaJalli
"""
import heapq
x = [1,2,16,34,54,23,12]
it = heapq.nlargest(2, range(len(x)), key=x.__getitem__)
a = 3



if (it[1] ==3 or a==3):
    count+=1