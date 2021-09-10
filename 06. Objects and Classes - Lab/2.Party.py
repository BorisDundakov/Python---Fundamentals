class Party:
    def __init__(self):
        self.people = []



result = Party()
command = input()
while not command == "End":
    result.people.append(command)
    command = input()


print(f"Going: {', '.join(result.people)}")
print(f"Total: {len(result.people)}")
