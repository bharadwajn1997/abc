import array
number=input("enter a number")
quotient=1
bind=[]
i=0
while(quotient!=0):
    remainder=number%2
    number=number//2
    quotient=number
    bind.append(remainder)

bind.reverse()
for i in bind:
    print i,













