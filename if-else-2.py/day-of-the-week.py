day=int(input())
result=''
if day==1:
    result='Monday'
elif day==2:
    result='Tuesday'
elif day==3:
    result='Wednesday'
elif day==4:
    result='Thursday'
elif day==5:
    result='Friday'
elif day==6:
    result='Saturday'
elif day==7:
    result='Sunday'
else:
    result='Error'

print(result)