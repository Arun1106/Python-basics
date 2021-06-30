import re
phone_number="91-1234567890"
if re.search('\w{2}-\w{10}',phone_number):
    print("phone number")
else:
    print("change it")