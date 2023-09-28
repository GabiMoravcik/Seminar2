from scipy import stats 

rvs = stats.norm.rvs(loc = 27.23, scale = 25, size = (12))
print stats.ttest_1samp(rvs,5.0) 

#ttest_ind()  
#mean(X1) = 950
#mean(X2) = 1000
#sed = 80
#t = (mean(X1) - mean(X2)) / sed 

alpha = 0.01
#cv = t.ppf(1.0 - alpha, df) 
#print(cv) 

p = (1 - t.cdf(abs(t_stat), df)) * 2 
print(p)

#blabla
#blabla

