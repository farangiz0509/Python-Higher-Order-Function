emails = ["ali@gmail.com", "vali@yahoo.com", "sami@gmail.com", "bek@outlook.com"]


domains = list(map(lambda emails: emails.split("@")[1] , emails))
print(domains)