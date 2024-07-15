"""name= input("Enter your name :")
print (f"Hello {name} welcome to python")
# f" {} là ép biến để ko fai call nh lần

# ý nghĩa của hàm if__name__=="__main__"
def welcome():
    print ("Welsom to corexplore Channel")

def func1():
    print ("This is funct")

def main():
    welcome()
    func1()

if __name__ == "__main__":
    main()
"""
def emailProcess(email):
    email_username = email[0:email.index("@")]
    #print(f"User email is:{user_email}")
    email_domain = email[email.index("@") +1:]
    return (email_username, email_domain)

def printMsg(email_username, email_domain):
    print(f"Username is: {email_username}; Email Domain is: {email_domain}")
                                                                
def main():                                                     
    email = input("Please enter your email:").strip()                 
    email_username,email_domain = emailProcess(email)           
    printMsg(email_username, email_domain)                      

if __name__ == "__main__":
    main()

"""nếu ko muốn gọi hàm printMsg thì phải viết như dưới:
def main(email_username, email_domain):
    email = input("Please enter your email:")
    email_username,email_domain = emailProcess(email)
    print(f"Username is: {email_username}, Email Domain is:{email_domain}") # nếu muốn print emaiusername vs domain thì ko thể vì def chỉ có ()

if __name__ == "__main__":
    main("email_username", "email_domain")
"""