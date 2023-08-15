def square_digits(num):

    lista = []
    
    num = str(num)
    num = list(num)
    for i in num:
        i = int(i)
        #print(i)
        lista.append(i**2)

    

    new_list = [str(i) for i in lista]
    

    string_value = "".join(new_list)
    #number = int(string_value)
    print(int(string_value))
    
    #print(num)

square_digits(9119)