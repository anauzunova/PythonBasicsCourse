time_first=int(input('Enter the time of the first competitor'))
time_second=int(input('Enter the time of the second competitor'))
time_third=int(input('Enter the time of the third competitor'))
total=time_first+time_second+time_third
minutes=total//60
seconds=total%60
if seconds>=10:
    print(f'The total time is {minutes}:{seconds}')
elif seconds<10:
    print(f'The total time is{minutes}:0{seconds}')
