[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> Percent population between 5'10'' and 6'1'': 34.2746837631%

```python
import scipy.stats

mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)


lim1 = 177.8 #5'10'' in cm
lim2 = 185.42000000000002 #6' 1'' in cm

print("Percent population between 5'10'' and 6'1'': %s" % ((dist.cdf(lim2) - dist.cdf(lim1))*100))

```
