"""
Project: Random Password Generator
"""

import string
import random

LETTERS = string.ascii_letters # trong library str có các ký tự ascii
# chứa các ký tự abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
NUMBERS = string.digits
PUNCTUATION =string.punctuation
# chứa các dấu <>%$...

def get_password_leghth():
    password_length = input("How long do you want your password: ")
    return int(password_length)

def password_generator (length): # pass có length defaul nó 
    printable = f"{LETTERS}{NUMBERS}{PUNCTUATION}" #password chứa các ký tự
    printable = list(printable) #phải convert về list mới có thể dùng ramdon để đảo thứ tự trg password
    random.shuffle(printable) # cách use random để shuffle, lúc này các ký tự let,nums punc đc trộn lên ngẫu nhiên but chưa có length

    random_password = random.choices(printable, k=length) # use hàm choices trong random để lấy length ký tự ngẫu nhiên
    random_password = "".join(random_password) # các str này trong list random_password. nối các str tạo thành str to mới bằng join
    return random_password # nhớ sau khi biến đổi hàng loạt biến trên phải trả về gtri cuối


def main():
    password_length = get_password_leghth()
    password = password_generator(password_length)
    print(password)



if __name__ == "__main__":
    main()

