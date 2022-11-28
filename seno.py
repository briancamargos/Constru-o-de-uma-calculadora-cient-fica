#O método usado para calcular o seno, foi série de taylor

def Seno(graus:float): # a função será montada presupondo que o angulo "a" de entrada está em graus.
    
    rads = (graus*3.141592653)/180 #conversão de graus para radiano
    
    termo_n = rads + 0.001    #esse 0.001 é para evitar erro caso a pessoa entre com "0 graus" como valor
    aux1 = 1                  #conta a posição do termo para saber se é uma soma ou subtração no somatorio
    aux2 = 1                  #usado na formula da série de taylor
    while (termo_n >= 0.001): #Faz o calculo até um dos termos n da série ser menor que 0.001
        
        i = 1                 #calculo do fatorial de aux2
        fatorial = 1
        while (i <= aux2): 
            fatorial *= i
            i += 1

        termo_n = (rads**aux2)/fatorial  #calculo do termo n da serie taylor
        
        if (aux1 == 1):
            seno = rads                  #o primeiro termo
        elif (aux1 %2 == 0):
            seno = seno - termo_n        #o somatorio dos termos n pares
        else:
            seno = seno + termo_n        #o somatorio dos termos n impares
        
        aux1 += 1
        aux2 += 2
    
    seno = round(seno,4)                 #arrendondamento para 4 casas decimais
    return seno