n = int(input())
positives_list = []
negatives_list = []

for _ in range(n):
    integer_input = int(input())
    if integer_input < 0:
        negatives_list.append(integer_input)
    else:
        positives_list.append(integer_input)

print(positives_list)
print(negatives_list)
print(f"Count of positives: {len(positives_list)}. Sum of negatives: {(sum(negatives_list))}")
