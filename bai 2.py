def TongBien(n):
    total= 0
    Number = n
    while (n > 0):
        total = total + n % 10
        n = int(n / 10)
    print("Tổng các chữ số của", Number, "là:", total)


middleName = input("Nhập tên đệm: ")
print("Tên đệm vừa nhập:", middleName)

n = int(input("Nhập số nguyên dương n = "))
TongBien(n)