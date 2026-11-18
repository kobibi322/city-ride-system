from datetime import datetime

start = datetime(2026, 11, 17, 10, 0)
end = datetime(2026, 11, 17, 14, 30)

difference = end - start

print(difference.days)
