#Retornando funções em funçoes.

def to_calcule(operation):
    def plus(num_1, num_2):
        return num_1 + num_2
    def minus(num_1, num_2):
        return num_1 - num_2
    
    
    if operation == "+":
        return plus
    if operation == ("-"):
        return minus
        
op = to_calcule("-")(1,2)



# Passando func em parâmetros

def messg_one(name):
    print("Executing message one")
    return f"Hello, {name}"

def messag_long(name):
    print("Executing long message")
    return f"Hello, how are you {name}"

def executing(function, name):
    return function(name)

print(executing(messg_one, "André"))


# Funções internas

def funcao_externa():
    print("Sou da função externa")
    
    def funcao_interna_um ():
        print("Sou da função interna 01")

    def funcao_interna_dois ():
        print("Sou da função interna 02")

    funcao_interna_um()
    funcao_interna_dois()


funcao_externa()