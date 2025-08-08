# 1
empty_list = []

# 2
items = ['apple', 'banana', 'cherry', 'mango', 'orange', 'grape']

# 3
print(len(items)) 

#4
first_item = items[0]
middle_item = items[len(items) // 2]
last_item = items[-1]
print("First:", first_item)
print("Middle:", middle_item)
print("Last:", last_item)

#5
mixed_data_types = ['Blonky', 17, 1.65, 'Single', 'Hanoi']
print(mixed_data_types)

#6
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#7
print(it_companies)

#8
print("Number of companies:", len(it_companies))

#9
print("First company:", it_companies[0])
print("Middle company:", it_companies[len(it_companies) // 2])
print("Last company:", it_companies[-1])

#10
it_companies[4] = 'Intel'
print("Modified list:", it_companies)

#11
it_companies.append('Tesla')

#12
it_companies.insert(len(it_companies) // 2, 'Samsung')

#13
it_companies[2] = it_companies[2].upper()  # Change one (not IBM)

#14
joined_companies = '#; '.join(it_companies)
print(joined_companies)

#15
print('Google' in it_companies)

#16
it_companies.sort()
print(it_companies)

#17
it_companies.reverse()
print(it_companies)

#18
print(it_companies[:3])

#19
print(it_companies[-3:])

#20
length = len(it_companies)
if length % 2 == 0:
    middle = it_companies[(length // 2) - 1: (length // 2) + 1]
else:
    middle = [it_companies[length // 2]]
print(middle)

#21

# Danh sách tuổi ban đầu
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sắp xếp danh sách
ages.sort()
print("Sorted ages:", ages)

# Tìm min và max
min_age = min(ages)
max_age = max(ages)
print("Min age:", min_age)
print("Max age:", max_age)

# Thêm lại min và max vào danh sách
ages.append(min_age)
ages.append(max_age)
print("Ages after appending min and max again:", ages)

# Sắp xếp lại sau khi thêm
ages.sort()

# Tìm median (trung vị)
n = len(ages)
if n % 2 == 0:
    median = (ages[n // 2 - 1] + ages[n // 2]) / 2
else:
    median = ages[n // 2]
print("Median age:", median)

# Tính trung bình (average)
average = sum(ages) / len(ages)
print("Average age:", average)

# Tính range
range_ = max_age - min_age
print("Age range:", range_)

# So sánh khoảng cách giữa min/average và max/average
min_diff = abs(min_age - average)
max_diff = abs(max_age - average)
print("abs(min - average):", min_diff)
print("abs(max - average):", max_diff)
