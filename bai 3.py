def soThuanNghich(n):
    ideal1= str(n)
    ideal2 = ideal1[::-1]
    if (ideal1 == ideal2):
        print(n, "là số thuận nghịch!")
    else:
        print(n, "không phải là số thuận nghịch!")


ten = input("Nhập họ và tên: ")
print("Họ và tên đầy đủ là:", ten)
n = int(input("Nhập số nguyên dương n: "))
soThuanNghich(n)