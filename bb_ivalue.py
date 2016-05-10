import math
#current book value
cbv = 6.02
#old book value
obv = 3.88
#number of years between current and old
bvYears = 9.0
#dividends received for 1 year
coupon = 1.32
#current book value
par = cbv 
#number of year of federal note
fedYears = 10
#10 year treasure rate(%)
r = 1.31

#calculate Average Book Value Rate(%)
upper = 1.0/bvYears
base=cbv/obv
a=math.pow(base,upper)
bvc=100*(a-1)
print bvc

#calulate Intrinsit Value
perc=(1+bvc/100)
base2=math.pow(perc,fedYears)
parr=par*base2
r=r/100

extra=math.pow((1+r),fedYears)

iValue=coupon*(1-(1/extra))/r+parr/extra; 

print iValue

