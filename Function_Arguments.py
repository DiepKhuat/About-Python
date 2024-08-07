
def print_name(name): # name là parameter =tham số của hàm print_name
    print(name)

def main():
    #pass #special keyword: python sẽ ko hiện error
    print_name("CodeXplore") # function call gọi hàm
# CodeXplore dc gọi là argument = biến tương tự vs vc name ="CodeXplore"


"""
Có 2 loại tham số: default parameter and required parameter
parameter trog print_name là required
khi gắn trực tiếp name ="codeXplore" ngay ở printname thì nó là default

đối vs arguments có 2 loại positional: dựa theo vị trí của paraments để gắn gtri
Keyword Argument:print_name(a =1, b=2, c=hello) 
"""
# Variable-length parameters(*args, **kwargs)
# if u mark a parameter with 1 asterisk(*), 
# u can pass any # of positional arguments to your function(typically called *args)

def varibaleLengthArgExample(a,b,*args, **kwargs): 
    print(a,b)
    for arg in args: # *args dc coi list, so use loop for to list items
        print(arg)
    for key,value in kwargs.items():
        print(key,value)
def main():
    varibaleLengthArgExample('a','b','Hello World', 1, size ='up 4', age=36)

# **Kwargs là dict nên dùng for loop vs key-val 
# khi dùng thì chỉ cần kwargs ko cần ** 

#compulsory là 2 gtri a,b buộc phải cung cấp. còn *args và **kwargs thì ko có cx dc

if __name__ == "__main__":
    main()