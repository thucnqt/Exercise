# -*- coding: utf-8 -*-
import re
import csv
import os.path

#default_name = "^[a-zA-Z_ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶ" + "ẸẺẼỀỀỂưăạảấầẩẫậắằẳẵặẹẻẽềềểỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợ" + "ụủứừỬỮỰỲỴÝỶỸửữựỳỵỷỹ\\s]+$"
#dads
# hello world
def input_name():
    # Dùng try - except xử lí chuỗi input người dùng nhập tránh crash hoặc bug. 
    while True:
        try:
            name = input('Xin chào! Hãy nhập tên đầy đủ bên dưới: ')
            if len(name.strip()) == 0:
                print("Vui lòng không nhập khoảng trắng")
                continue 
            global validate # Biến toàn cục 
            validate = re.findall(r'^[a-zA-Z_ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶ" + "ẸẺẼỀỀỂưăạảấầẩẫậắằẳẵặẹẻẽềềểỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợ" + "ụủứừỬỮỰỲỴÝỶỸửữựỳỵỷỹ\\s]+$', name)
            # regex Vietnamese language
            if not validate:
                raise ValueError
            else:
                break
        except ValueError:
            print('Nhập tên không hợp lệ !!')

def show_info():
    global b,c,ho,lot,ten # Biến toàn cục 
    c = ''.join(validate)
    b = c.split()
    # Kiểm tra điều kiện nhập từ ten người dùng đẻ tránh sai sót 
    if len(b) == 2:
        ho = b[0]
        lot = 'NULL'
        ten = b[1]
        print ("Chúc bạn {} một ngày tốt lành!".format(ten))
    elif len(b) == 1:
        ho = 'NULL'
        lot = 'NULL'
        ten = b[0]
        print ("Chúc bạn {} một ngày tốt lành!".format(ten))
    else:
        ho = b[0]
        lot = ' '.join(b[1:-1])
        ten = b[-1]
        print ("Chúc bạn {} một ngày tốt lành!".format(ten))

def write_csv():
    if (os.path.isfile('danhsachten.csv')):
        with open('danhsachten.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow([c, ho, lot,ten])
    else:
        with open('danhsachten.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(["Họ tên", "Họ", "Lót","Tên"])
            writer.writerow([c, ho, lot,ten])
    
    
input_name() # Hàm nhập tên 
show_info() # Hàm hiển thị Chúc ngày mới 
write_csv() # Ghi thông tin vào file danhsachten.csv

 