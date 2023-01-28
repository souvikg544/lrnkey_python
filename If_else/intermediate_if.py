# Write a program to compute the following bill of a retail store:
#  Cost --------------------         Discount
# >$1000        ----------             $100
# >$750 <$1000      --------           $80
# >400 <750        ------              $50
# <400               ------            $30

c=float(input("Enter the cost of the article : $"))
d=0.0
# $1100 DISCOUNT- $100   Final price- $(1100-100) = $1000
final_price=0.0

if(c>=1000):
    d=100
elif((c>=750)&(c<1000)):
    d=80
elif((c>=400)&(c<750)):
    d=50
else:
    d=30

final_price=c-d

print("The discount given = $",d)
print("The final price of the article is : $",final_price)
