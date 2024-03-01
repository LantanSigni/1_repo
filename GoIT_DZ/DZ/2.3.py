work_experience = int(input("Enter your full work experience in years: "))

if work_experience <= 5 and work_experience > 1:
    developer_type = "Middle"
    print(developer_type)
elif work_experience <= 1:
    developer_type = "Junior"
    print(developer_type)
else:
    developer_type = "Senior"
    print(developer_type)
