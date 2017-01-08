[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

>> The distribution is uniform as can be seen from the CDF, which is a straight line. It shows that 10% of the sample are below the 10th percentile, 20% of the samples are below 20th percentile etc.

```python  
from __future__ import print_function, division  
%matplotlib inline  
import numpy as np  
import nsfg  
import first  
import thinkstats2  
import thinkplot  

x = np.random.random(1000)    
pmf = thinkstats2.Pmf(x)   
thinkplot.Pmf(pmf, linewidth=0.1)  
thinkplot.Config(xlabel='Random variable', ylabel='PMF')  
