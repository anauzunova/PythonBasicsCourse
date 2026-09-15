length=float(input('Length in cm: '))
width=float(input('Width in cm: '))
height=float(input('Height in cm: '))
taken_space_procent=float(input())/100
volume=length*width*height
space_for_water=volume-taken_space_procent*volume
print(space_for_water/1000,'L')
#print('Volume in cm3:',volume)