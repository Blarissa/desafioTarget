def faturamentoEstados():
    faturamento = {
            'SP' : 67836.43,
            'RJ' : 36678.66,
            'MG' : 29229.88,
            'ES' : 27165.48,
        'Outros' : 19849.53
    }
    
    #realizando soma do faturamento
    soma = 0
    for UF in faturamento.keys():
        soma = soma + faturamento[UF]
    
    #calculando percentual e inserindo num dicionario
    porcentagem = {
        'SP' : round(faturamento['SP']*100/soma,2),
        'RJ' : round(faturamento['RJ']*100/soma,2),
        'MG' : round(faturamento['MG']*100/soma,2),
        'ES' : round(faturamento['ES']*100/soma,2),
        'Outros' : round(faturamento['Outros']*100/soma,2)
    }
    #mostrando resultado    
    print("Percentual que cada estado teve do valor total: ",porcentagem)
    
faturamentoEstados()