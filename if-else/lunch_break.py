import math
series_name=input()
ep_duration=int(input())
lunch_break=int(input())
lunch=1/8*lunch_break
relaxation_time=1/4*lunch_break
time_left=lunch_break-(lunch+relaxation_time+ep_duration)   

if time_left>=0:
    print(f"You have enough time to watch {series_name} and left with {math.ceil(time_left)} minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, you need {math.ceil(abs(time_left))} more minutes.")