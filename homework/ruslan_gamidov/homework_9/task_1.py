from datetime import datetime

date = "Jan 15, 2023 - 12:05:33"
dt = datetime.strptime(date, "%b %d, %Y - %H:%M:%S")

print(dt.strftime("%B"))
print(dt.strftime("%d.%m.%Y, %H:%M"))
