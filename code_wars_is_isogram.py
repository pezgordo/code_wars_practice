def is_isogram(string):
    #your code here

    for i in string:
        
        if string.count(i) > 1:
            isogram = False
        else: 
            isogram = True

        
        return isogram

        
    
        
        
def imprime_letras(string):
    for i in string:
        if string.count(i) > 1:
            return False
        
        return True
        
      

print(is_isogram("moose"))
print(is_isogram("mose"))



print(imprime_letras("moose"))