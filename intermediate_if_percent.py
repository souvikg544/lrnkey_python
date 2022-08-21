# Write a program to compute the following bill of a retail store:
#  Cost --------------------         Discount
# >$1100        ----------             12%
# >$650 <$1100      --------           9%
# >450 <650        ------              6%
# <450             ------              4%

mp=float(input("Enter the market price : $"))
d=0.0
sp=0.0

# $1500------------- d= 12/100 * 1500  = $180 ------ sp= 1500-180 = $1320

if(mp>1100):
    d=(12/100)*mp
elif((mp>650)&(mp<=1100)):
    d=(9/100)*mp
elif((mp>450)&(mp<=650)):
    d=(6/100)*mp
else:
    d=(4/100)*mp

print("The discount is : $",d)
sp= mp-d
print("The final selling price is : $",sp)

