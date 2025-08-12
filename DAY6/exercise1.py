for number in range(0, 11):
    print(number)

i = 0
while i <= 10:  # điều kiện dừng
    print(i)
    i += 1      # tăng i để tránh vòng lặp vô hạn

for number2 in range(10, -1, -1):  # start=10, stop=-1 (để bao gồm 0), bước -1
    print(number2)

i2 = 10
while i2 >= 0:
    print(i2)
    i2 -= 1  # giảm i mỗi vòng lặp

for loop in range(1, 8):  # i chạy từ 1 đến 7
    print('#' * loop)    # in i lần ký tự '#'

for hang in range(8):         # 8 hàng
    for cot in range(8):     # 8 cột trong mỗi hàng
        print('#', end=' ')  # in '#' và cách 1 dấu cách, không xuống dòng
    print()                # xuống dòng sau khi in xong 1 hàng

for i3 in range(11):  # từ 0 đến 10
    print(f"{i3} x {i3} = {i3 * i3}")

items = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']

for item in items:
    print(item)

for even in range(0, 101):
    if even % 2 == 0:
        print(even)

for odd in range(0, 101):
    if odd % 2 != 0:
        print(odd)