def fibonacci(n):
    ultimo = 1
    penultimo = 0
    
    count = 0
    termo = 0
   
    #calcula a sequencia de fibonacci
    while termo < n:    
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1      
    
    #verifica se o termo pertence a sequencia        
    if(n == termo):
            print(n," Pertence a sequencia de Fibonacci")
    else:
            print(n," Nao pertence a sequencia de Fibonacci")        
        
#teste
for i in range(10):
    fibonacci(i)