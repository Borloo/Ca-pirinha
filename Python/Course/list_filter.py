numbers = [8, 7, 10, 12, 9, 5, 100, 12, 10, 8]
unique_number = []

for num in numbers:
    if num not in unique_number:
        unique_number.append(num)

print(unique_number)
