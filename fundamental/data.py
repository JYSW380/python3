from datetime import datetime

date = datetime.now() - datetime(1900, 12, 23)
print(date)

now = datetime(2019, 5, 7)
print(now)
print(now.strftime("%Y"))

whenever = datetime.strptime("2018-09-11", "%Y-%m-%d")
print(whenever)
print(whenever.day)

delta = datetime.now() - datetime(1900, 12, 23)
print(delta.days)


