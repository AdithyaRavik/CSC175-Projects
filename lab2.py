#--------------------------------
#Purpose- Find minutes in a week
#Input- Number of weeks
#Output- Minutes in a week in number format
#Assumptions- Users only putting in integers
#----------------------------------


minutes_in_hours = 60
hours_in_day = 24
days_in_week = 7
number_of_weeks = int(input("How many weeks are you trying to find?"))

minutes_per_week = hours_in_day * days_in_week * minutes_in_hours * number_of_weeks

print(" There are", minutes_per_week, "mins in", number_of_weeks,  "week")

# If you want to change a number you can change it in the variable instead of changing it in the equation. It would be a mess.
#Variables make the program easier and cleaner to read. 
