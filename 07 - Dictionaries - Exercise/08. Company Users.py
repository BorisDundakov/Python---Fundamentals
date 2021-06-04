command = input()
company_users = {}
while command != "End":
    split_command = command.split(" -> ")
    company_name = split_command[0]
    employee_ID = split_command[1]

    if company_name not in company_users:
        company_users[company_name] = [employee_ID]

    else:
        if employee_ID not in company_users[company_name]:
            company_users[company_name].append(employee_ID)

    command = input()
#
# print(company_users)
# print(type(company_users))
a = []
# print(company_users)
printed_keys = []


for key in sorted(company_users):
    for items in company_users[key]:
        if key not in printed_keys:
            print(key)
            printed_keys.append(key)

        print(f"-- {items}")
