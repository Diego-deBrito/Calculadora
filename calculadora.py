print("\n************************************************ Calculadora ***********************************************")

# Funções  para cada uma das operações
def soma (n1,n2):
    return n1 + n2

def sub (n1,n2):
    return n1 - n2

def mult (n1,n2):
    return n1 * n2

def div (n1,n2):
    return n1 // n2


# Interação com usuário
print("Selecione o número da operação desejada: ")
print("1 - Soma\n"
      "2 - Subtração\n"
      "3 - Multiplicação\n"
      "4 - Divisão ")


escolha = (input("\nDigite sua opção (1/2/3/4) "))

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo  número: "))


# Condicionais para escolha do usuário
if escolha == "1":
    print("\n")
    print(num1, "+" , num2,"=", soma( num1, num2 ))
    print("\n")
elif escolha == "2":
    print("\n")
    print(num1, "-", num2, "=", sub(num1, num2 ))
    print("\n")
elif escolha == "3":
    print("\n")
    print(num1, "x", num2, "=", sub(num1, num2))
    print("\n")
elif escolha == "4":
    print()
    print(num1, "/", num2, "=", div(num1,num2))