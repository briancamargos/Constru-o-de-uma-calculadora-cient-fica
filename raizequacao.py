# encontra as raízes de uma equação, retorna os valores das raízes usando o método de bhaskara
def Raizequacao(a:float,b:float,c:float): #pensei aqui em pedir os indices a,b,c da equação para usar a formula
    
    delta = b**2 - 4*a*c
    
    if (delta > 0):
        delta = delta**(1/2) 
        x1 = (-b + delta)/2*a
        x2 = (-b - delta)/2*a
        return x1,x2

    elif (delta == 0):
        x1 = (-b)/2*a
        x2 = x1
        return x1,x2
    else: #caso delta seja menor que 0, não haverá raízes reais
        return "Não existem raízes reais"," " #pensar aqui como retornar esse erro