"""
List Comprehensions
giúp b viết code ngắn gọn(đb trọng loop đã có)
"""
# new_list [<action> for <item> in <iterator> if <some condition>]

word = "Hello World"
# binh thuong use loop for
print([char for char in word]) # interator là các ký tự sẽ có trong list, item là char
# tạo ra list mới từng str trong str word

even_numbers = [i for i in range(0,10) if i%2 == 0]
print (even_numbers)

transactions = [100,200,300,150,80]
TAX_RATE = 0.08
SERVICE_CHARGE = 0.07
def get_price_tax_price(bill):
    return bill*(1 + TAX_RATE + SERVICE_CHARGE)
final_prices = [get_price_tax_price(bill) for bill in transactions]
print(final_prices)

# Advanced Functions
#list() --> convert strings => list
my_strings = "Welcome to codeexplore Channel"
list_of_char = list(my_strings)
print(list_of_char)

# zip(): looping through two list simultaneously 
wizards = ['Harry Potter', 'Ron', 'Hermione']
pets = ['Hedwig', 'Scabber','Crookshank']
for wiz, pet in zip(wizards,pets):
    print(f"{wiz} has {pet}")
# từng wizard sẽ tương tự vs pet tạo ra 1 list str lớn
#  [[''Harry Potter','Hedwig'],['Ron','Scabber'], ['Hermione','Crookshank']]
for index,(wiz, pet) in enumerate(zip(wizards, pets)):
    print(f"{index +1}. {wiz} has {pet}")

# sorted() của list sẽ advanced hơn theo hàm lambda
sort_by_second = sorted(
    ['hi', 'you', 'hello', 'Code'], key = lambda el: el[1]) # el là element
# tạo hàm lambda tempt vs input là el: el[1] từ index 1 của từng str
print(sort_by_second)

# 2D Array/List = Matrix : mảng 2 chiều
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(matrix[0][1])
#Transform Matrix in list:
list_converted = [matrix[row][col]
                  for row in range(len(matrix)) for col in range(len(matrix))]
print(list_converted)
# Combine columns with zip and *: 
print([x for x in zip(*matrix)])