def fibonacci(n):
    fibonacci_sequence = [0, 1]
    
    while fibonacci_sequence[-1] < n:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    
    if n in fibonacci_sequence:
        return True
    else:
        return False

def main():
    numero = int(input("Informe um número: "))
    
    if fibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")

if __name__ == "__main__":
    main()
