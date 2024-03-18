def verificacaoFibo(num):
    # inicializa os dois primeiros números da sequência de Fibonacci
    a, b = 0, 1
    # conjunto para armazenar os números da sequência de Fibonacci
    fib= {a, b}
    
    # calcula a sequência de Fibonacci e armazena no conjunto
    while b <= num:
        a, b = b, a + b
        fib.add(b)
    
    # verifica se o número informado está na sequência de Fibonacci
    if num in fib:
        return f"O número {num} pertence a sequência de Fibonacci."
    else:
        return f"O número {num} não pertence a sequência de Fibonacci."

# resultado da verificação
numeroDigitado= int(input("Informe um número "
                          "para verificar na sequência de Fibonacci: "))
resultado = verificacaoFibo(numeroDigitado)
print(resultado)
