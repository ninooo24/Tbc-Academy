
a=int(input('please enter the first natural number: '))
b=int(input('please enter the second natural number: '))
if a<=0 or b<=0:
    print("please enter the natural numbers")
else:
    if a%b==0:
        print(b,'is multiple for',a)
    else:
        print(b,'is not multiple for',a)