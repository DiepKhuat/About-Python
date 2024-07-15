# Is Unique: Implement an Algorithm to determine if a string has all unique characters.
# Hint : Use Hash Table => Dict : key-value is unique in dict

"""
def unique(str):
    char_set = {}
    for char in str:            # loop lần lượt các key(acacd)
        if char in char_set:    # lần 1 a ko có, nên gắn nó value 1 cho vào trg dict
            return False        # kq chưa trả về( ko biết T  hay F)cứ thế tiếp tục đến chữ a. đã có trong dict
        char_set[char] = 1      # kq return về False
    return True                 # Nếu char ko có trong dict thì gắn hết k-v cho loop và kq cuối return True

if __name__ == "__main__":
    str = "abacd"
    print(unique(str))
"""


# Để test những test case nhiều( rất nh str) thì use library unittest

import unittest
# Hàm function unique
def unique(str):
    char_set = {}
    for char in str:            
        if char in char_set:    
            return False       
        char_set[char] = 1    
    return True                  

class Test(unittest.TestCase):
# lập những dữ liệu testcase để execute hàm unique
    dataT = [('abcd'),('sgdhak23'),('')]  
    dataF = [('asdcade'), ('232 jcdj -:')]
# tạo hàm testcase để test từng cái str ở dataT bởi function unique
    def test_unique(self): # self ở đây là chính nó trong class test
        #true check
        for test_case in self.dataT:   # loop từng các testcase ở dataT
            actualResult = unique(test_case) #pass vào unique vs giá trị là testcase. đặt nó tên là actualResult
            self.assertTrue(actualResult) # dùng hàm asserttrue để compare vs kq actualResult
        #false check
    def test_unique(self):
        for test_case in self.dataF:
            actualResult = unique(test_case)
            self.assertFalse(actualResult)

if __name__ == "__main__":
    unittest.main()

