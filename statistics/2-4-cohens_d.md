[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> The Cohens'd value between first born babies and others is -0.10845. This indicates that the difference between means is small as the 95% confidence intervals are between 1.66-1.78. One would have a problem detecting the difference in total weigth of babies.
Python Code:

#Solution to problem in chapter 2, ex 4
#Cohen's d
from __future__ import print_function, division
import pandas as pd
import numpy as np
import math
import nsfg
import thinkstats2

def cohensdcalc(group1, group2):
    mean1 = group1.mean()
    mean2 = group2.mean()
    diff = mean1 - mean2
    var1 = group1.var()
    var2 = group2.var()
    n1 = len(group1)
    n2 = len(group2)
    pooled_var = (n1*var1 + n2*var2)/(n1+n2)
    d = diff/np.sqrt(pooled_var)
    return d
preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]
cohensdcalc(firsts.birthwgt_lb, others.birthwgt_lb)

