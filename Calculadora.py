import PySimpleGUI as sg
from soma import Soma
from subtracao import Subtracao 
from multiplicacao import Multiplicacao
from divisao import Divisao
from potencia import Potencia
from raiz import Raiz
from seno import Seno
from cosseno import Cosseno
from tangente import Tangente

sg.theme('Dark Blue 3')   # Tema da GUI

# Coisas e itens dentro da janela.
layout =    [  
            [sg.Text('    ',key ='-tela-', size = (65, 5), background_color = 'black', enable_events = True)],
            [sg.Button('1', size = (6, 3)), sg.Button('2', size = (6, 3)), sg.Button('3', size = (6, 3)), sg.Button('Apagar', size = (6, 3)), sg.Button('+', size = (6, 3)), sg.Button('-', size = (6, 3)), sg.Button('x', size = (6, 3)), sg.Button('/', size = (6, 3))],
            [sg.Button('4', size = (6, 3)), sg.Button('5', size = (6, 3)), sg.Button('6', size = (6, 3)), sg.Button('Limpar', size = (6, 3)), sg.Button('potencia', size = (14, 3)), sg.Button('raiz', size = (14, 3))],
            [sg.Button('7', size = (6, 3)), sg.Button('8', size = (6, 3)), sg.Button('9', size = (6, 3)), sg.Button('.', size = (6, 3)), sg.Button('seno', size = (8, 3)), sg.Button('cosseno', size = (8, 3)), sg.Button('tangente', size = (8, 3))], 
            [sg.Button('0', size = (6, 3)), sg.Button('=', size = (15, 3))] 
            ]

# Cria a janela
window = sg.Window('CALCULADORA', layout)

# variaveis e funções auxiliares

Entradas_Numeros = []
Operacao = ''
Numero = []
Aux1 = 0
ponto = True
nao_numero = True
Result = False

def ligaOp(j):
    list = ['+','-','x','/','raiz','potencia','seno','cosseno','tangente']
    for i in list:
         window[i].update(disabled=j)
def Botauns(j):
    list = ['+','-','x','/','raiz','potencia','seno','cosseno','tangente','1','2','3','4','5','6','7','8','9','0','.','Apagar','=']
    for i in list:
         window[i].update(disabled=j)


# Loop que registra os eventos na janela e registra os inputs e tal

while True:
    
    event, values = window.read()      #Lê os eventos e os valores a cada loop
    
    if event == sg.WIN_CLOSED:         #termina o loop quando o usuario fecha a janela
        break
    
    # registra os botões da calculadora
    Fim_numero = False
    Result = False
    if Aux1 == 1:
        ligaOp(True)
    
    #casos que o usuario digite um numero de 0 a 9
    if event == '1' or event == '2' or event == '3' or event == '4' or event == '5' or event == '6' or event == '7' or event == '8' or event == '9' or event == '0' or event == 'Apagar' or event == '.':
        nao_numero = True
        if event == '1':                    
            Entradas_Numeros.append('1')
        elif event == '2':
            Entradas_Numeros.append('2')
        elif event == '3':
            Entradas_Numeros.append('3')
        elif event == '4':
            Entradas_Numeros.append('4')
        elif event == '5':
            Entradas_Numeros.append('5')
        elif event == '6':
            Entradas_Numeros.append('6')
        elif event == '7':
            Entradas_Numeros.append('7')
        elif event == '8':
            Entradas_Numeros.append('8')
        elif event == '9':
            Entradas_Numeros.append('9')    
        elif event == '0':
            Entradas_Numeros.append('0')
        elif event == 'Apagar':            #apaga o ultimo botão clicado, caso não tenha nada digitado, só evita o erro
            if Entradas_Numeros == []:
                continue
            else:
                Entradas_Numeros.pop()     
        elif event == '.':                 #coloca o ponto, mas evita pontos seguidos
            if ponto == True:
                Entradas_Numeros.append('.')
                ponto = False  
            elif Entradas_Numeros == []:
                Entradas_Numeros.append('0.')
            else:
                continue
    
    #casos que o usuario digite uma das operações
    elif event == '+' or event == '-'or event == 'x'or event == '/' or event == 'raiz' or event == 'potencia':
        ponto = True
        Fim_numero = True
        Aux1 = 1

        if event == '+':
            Operacao = '+'
        elif event == '-':
            Operacao = '-'
        elif event == 'x':
            Operacao = 'x'
        elif event == '/':
            Operacao = '/'
        elif event == 'raiz':
            Operacao = ' raiz de '
        elif event == 'potencia':
            Operacao = ' elevado à '
    
    elif event == 'seno'or event == 'cosseno'or event == 'tangente':  
        ponto = True
        Fim_numero = True
        Aux1 = 1
        ligaOp(True)
        if event == 'seno':
            Operacao = ' seno de '     
        elif event == 'cosseno':
            Operacao = ' cosseno de '     
        elif event == 'tangente':
            Operacao = ' tangente de '


    elif event == 'Limpar':                      #elimina tudo digitado
        Entradas_Numeros = []
        Numero = []
        Botauns(False)
        Aux1 = 0
            
    #verifica se o usuario digitou uma operação ou numero
    if Fim_numero:
        if nao_numero:
            Numero.append(''.join(Entradas_Numeros))
            Numero.append(Operacao) 
            Entradas_Numeros = []
            nao_numero = False 
        else:
            if Numero == []:
                continue
            else:
                Numero.pop()
                Numero.append(Operacao)


    # evento que chama as funçoes de operação para as funções baseado no string que o usuario montou 
    # clicar nos botões da calculadora
    Resultado = '    '
    if event == '=':
        Result = True
        Botauns(True)
        try:
            Numero.append(''.join(Entradas_Numeros))
            if Numero[1] == ' seno de ' or Numero[1] == ' cosseno de ' or Numero[1] == ' tangente de ':
                N = float(Numero[2])
                if Numero[1] == ' seno de ':
                    Resultado = Seno(N)
                elif Numero[1] == ' cosseno de ':
                    Resultado = Cosseno(N)
                elif Numero[1] == ' tangente de ':
                    Resultado = Tangente(N)

            elif (Numero[1] == '+' or Numero[1] == '-' or Numero[1] == 'x' or Numero[1] == '/' or Numero[1] == ' raiz de ' or Numero[1] == ' elevado à '):
                N1 = float(Numero[0]) #estranhamente, quando tentei converter para float dentro das funções, não dava certo
                N2 = float(Numero[2])
                if Numero[1] == '+':
                    Resultado = Soma(N1,N2)
                elif Numero[1] == '-':
                    Resultado = Subtracao(N1,N2)
                elif Numero[1] == 'x':
                    Resultado = Multiplicacao(N1,N2)
                elif Numero[1] == '/':
                    Resultado = Divisao(N1,N2)
                elif Numero[1] == ' raiz de ':
                    Resultado = Raiz(N1,N2)
                elif Numero[1] == ' elevado à ':
                    Resultado = Potencia(N1,N2)
                
            
        except:
            Numero = 'ERRO'
            



    #monta o string com as informações para o usuario
    if Result:
        
        TELA = ''.join(Numero) + '         =       ' + str(Resultado)
        
    else:
        auxTELA = ''.join(Entradas_Numeros)
        TELA = ''.join(Numero) + ''.join(auxTELA)


    #atualiza a tela
    window['-tela-'].update(TELA)
    


    print(Numero)
    print(Resultado)

window.close()