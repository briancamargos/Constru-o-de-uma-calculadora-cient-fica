##plotagem do gráfico

def plotgrafico(X,Y):

    import matplotlib.pyplot as grafico

    print('Plotagem do gráfico \n')
    
    titulo = 'Gráfico'
  
    grafico.figure(figsize=(10,5)) #tamanho do grafico

    grafico.plot( X , Y , label='X', linestyle='dashed' )  # (x , y, legenda, estilo de linha)

    grafico.title(titulo)  

    grafico.xlabel('X')

    grafico.ylabel('Y')

    #grafico.legend(prop={'size': 15})