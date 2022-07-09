import json

def faturamento():
    dados = []
    count = maior = soma = 0
    menor = 9999999
    
    #abrindo e lendo arquivo json
    with open('dados.json') as f:  
        dados = json.load(f)
    
    for valor in dados:   
        #avaliando maior e menor valor do faturamento
        if valor['valor'] != 0 :
            if valor['valor'] > maior:
                maior = valor['valor']
                
            if valor['valor'] < menor:
                menor = valor['valor']
            
            #soma do faturamento 
            soma = soma + valor['valor']        
        else:
            #contando dias de faturamento 0.0
            count+=1 
               
    #calculando media    
    media = soma/(30 - count)
    
    #contando quantos dias tem o faturamento maior que a media mensal
    count = 0 
    for valor in dados:   
        if valor['valor'] != 0 and valor['valor'] > media:
               count +=1
    
    #mostrando resultados           
    print("Maior faturamento do mes: ",maior)
    print("Menor faturamento do mes: ",menor)
    print("Numero de dias em que o faturamento foi maior"+ 
          " que a media mensal: ",count)

    
faturamento()