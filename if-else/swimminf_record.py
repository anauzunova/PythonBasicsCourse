import math
record=float(input())
metres=float(input())
secs_per_metre=float(input())
ivans_time_not_slowed=metres*secs_per_metre
times_slowed=metres//15
ivans_total_time=ivans_time_not_slowed+times_slowed*12.5


if ivans_total_time<record:
    print(f'Yes, he succeeded! The new world record is {(ivans_total_time):.2f} seconds.')
else:
    print(f'No, he failed! He was {(ivans_total_time-record):.2f} seconds slower.')