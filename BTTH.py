numbers_employee = int(input("Nhập số lượng nhân viên: "))

for i in range(1, numbers_employee + 1):

    name_employee = input("Nhập tên nhân viên: ")

    while name_employee.strip() == '':
        name_employee = input("Lỗi. Tên không được để trống! Vui lòng nhập lại tên: ")

    days_work = int(input("Nhập số ngày làm: "))


    if days_work < 0 or days_work > 22:
        print("Lỗi. Số ngày nhập không hợp lệ! ")
        continue

    print(f"{name_employee}: ", end = "")
    for i in range(days_work):
        for j in range(1):
            print("*", end="") 
    print()

    if days_work >= 18:
        print("Làm việc chăm chỉ")
    elif days_work == 0:
        print("Nhân viên nghỉ toàn bộ tháng")
    elif days_work < 10:
        print("Làm việc ít")
    else:
        print("Làm việc bình thường")

    print()
