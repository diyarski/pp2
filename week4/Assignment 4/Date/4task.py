from datetime import datetime

date_1 = datetime(2023, 2, 18, 12, 30, 0)
date_2 = datetime(2023, 2, 20, 10, 30, 0)

difference = (date_2 - date_1).total_seconds()

print("The difference between the two dates is", difference, "seconds.")
