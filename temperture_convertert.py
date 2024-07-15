def cToFConverter():
    while True:
        cTemp = (input("Please enter C degree:")) # có thể convert sang int nhưng ko thể sang float luôn
        if cTemp:
            cTemp = float(cTemp) # ko thể convert directly ctemp ở trên vì fai convert int trc
            fTemp = round(9*cTemp/5 + 32,1)
            print(f"{cTemp} C is converted to {fTemp}F")
            break # cho vào vòng loop while để cho users chỉ nhận giá trị true
        else:
            print("cTempt input is empty")
            continue # cho users cơ hội input temp đến khi true thì thôi


def main():
    #print ("Hello")
    cToFConverter()  #nếu ko gọi statement thì file ko execute 実行

if __name__ == "__main__":
    main()
