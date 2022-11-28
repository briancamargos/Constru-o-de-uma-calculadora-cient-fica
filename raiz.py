def Raiz(B:float, A:float=2): # A > Radicando / número que será extraido a raiz
        	   # B > índice
        if B == 0:
            Resultado = "ERRO"
        else:    
            Resultado =  A ** (1/B)
        return Resultado