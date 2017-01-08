[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> As can be seen from the plots the biased plot has a higher mean and is skewed towards the right, indicating that families with more children are more likely to appear in our sample.
Python Code  

#Actual vs Biased  
from __future__ import print_function, division  
import pandas as pd  
import numpy as np  
import math  
import nsfg  
import thinkstats2  
import thinkplot  

def BiasPmf(pmf, label):  
    new_pmf = pmf.Copy(label=label)  
    for x, p in pmf.Items():  
        new_pmf.Mult(x, x)  
    new_pmf.Normalize()  
    return new_pmf  

resp = nsfg.ReadFemResp()  
pmf = thinkstats2.Pmf(resp.numkdhh, label = 'numkdhh')  
biased_pmf = BiasPmf(pmf, label='biased')  
thinkplot.PrePlot(2)  
thinkplot.Pmfs([pmf, biased_pmf])  
thinkplot.Show(xlabel='Number of children', ylabel='PMF')  

