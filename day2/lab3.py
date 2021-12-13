 #Given the integer N - the number of minutes that is passed since midnight - how many
#hours and minutes are displayed on the 24h digital clock?
#The program should print two numbers: the number of hours (between)
#number of minutes (between 0 and 59).
#For example, if N = 150, then 150 minutes have passed since midnight
#am. So, the program should print 2 30.
#n = "no. of minutes passed since midnight"
n = "int(input(" minutes passed: "))
hours = n//60
minutes=n2*60
print(f"{n} minutes passed {hours}:{minutes}")