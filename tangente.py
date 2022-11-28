#O método usado para calcular o tangente, foi série de taylor

def Tangente(graus:float):          
    from seno import Seno
    from cosseno import Cosseno

    if Cosseno(graus) == 0:
        return 'Erro, tangente tendendo ao infinito'
    else:

        tangente = Seno(graus)/Cosseno(graus)
    
        tangente = round(tangente,1)                 #arrendondamento para 1 casa decimal, precisão para valores proximos de 89 graus fica baixa, 
                                                    #então acaba não fazendo sentido usar mais casas décimais
        return tangente                        