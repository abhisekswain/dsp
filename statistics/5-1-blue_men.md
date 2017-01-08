[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> 34.2% of the male US population is elgible to join the Blue Man group. The difference of the CDF's between the 2 height limits gives the percentage of men in the required range.
```python
from __future__ import print_function, division  
import pandas as pd  
import numpy as np    
import nsfg  
import thinkstats2  
import thinkplot  
import analytic  
import scipy.stats  

gaussian_dist = scipy.stats.norm(loc=178, scale=7.7)  
lower_height = gaussian_dist.cdf(177.8)  
upper_height = gaussian_dist.cdf(185.4)  
print (lower_height-upper_height)  
