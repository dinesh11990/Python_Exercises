name = input("Enter name: ")
from datetime import datetime
Total_days = datetime.now() - datetime(1990, 9, 11)
Result = Total_days.days
message = "Hi %s, days you have spent" % (name)
print(message,Result)
    