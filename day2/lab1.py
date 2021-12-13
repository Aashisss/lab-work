# convert seconds to day, hours, minutes and seconds

Sec=int(input("enter the value for seconds: "))
day = (((sec/60)/60)/24)
print(f"total day for given seconds:{day}")
hour =((sec/60)/60)
print(f"total hours for given seconds:{hour}")
minute =(sec/60)
print(f"total minutes fpr given seconds:{minute}")