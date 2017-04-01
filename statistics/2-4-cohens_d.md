[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> REPLACE THIS TEXT WITH YOUR RESPONSE
First babies are lighter than others. Cohen's D for first babies total weight vs. others was -0.0886729270726 .
Cohen's D for pregnancy lengths of first babies vs. others was 0.0288790446544. Total weight difference between first babies vs. others was more significant than the difference in pregnancy lengths between first babies vs. others

```python  
# Cohen's D for first babies total weight vs. others
print(CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb))

# Cohen's D for first babies pregnancy lengths vs. others
print(CohenEffectSize(firsts.prglngth, others.prglngth))
```
