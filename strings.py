"""
String Format
"""
# có 3 cách : %, .format(), f-strings
# %
name = "CodeExplore"
my_string = "Welcome to %s" % name # %s means ép kiểu str, và cộng vs str name

pi = 3.14159
s = "pi  number"
my_string = "Variable is %f from %s" %(pi,s)
# %f ép kiểu float, %(pi,s) và cộng với variable pi và s
# %.2f means muốn lấy 2 số thập phân thôi
my_string = "Variable is %.2f from %s" %(pi,s)
print(my_string)

# .format()
age = 28
height = 153.5
my_string = "I am {} years old; {:.3f} cm".format(age,height)
# {} là để gtri age vs height vào trong đó. format() trong() chứa variable
# {:.3f} means lấy 3 số thập phân sau dấu phẩy
print(my_string)

# f-Strings mới có từ python version 3.6 trở đi
my_string = f"Pi is {pi:.2f} and my name is {name} and {age} years old"
print(my_string)