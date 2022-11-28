def Raiz(A:float,B:float): # A > Radicando / número que será extraido a raiz
        	   # B > índice
        if B == 0:
            Resultado = "ERRO"
        else:    
            Resultado =  A ** (1/B)
        return Resultado