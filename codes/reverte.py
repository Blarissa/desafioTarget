def reverte(palavra):
    count = len(palavra)-1
    inverso = ""
    
    #inverte a palvra
    while count >= 0:
        inverso = inverso + palavra[count]
        count -=1
    
    #mostra o resultado    
    print(inverso)
    
reverte("maria")    
reverte("arara") 
reverte("jose") 