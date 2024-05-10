# -------------------------------------------- Logando as tarefas --------------------------------------------------
def logging(func):
    def wrapper(*args, **kwargs):
        print(f"Nome da função: {func.__name__}")
        print(f"Argumentos: {args}")
        resultado = func(*args, **kwargs)
        print(f"Resultado: {resultado}")
        return resultado
    return wrapper

@logging
def soma(a,b):
    return a+b

soma(2,3)


# ---------------------------------------- (ANTES) Medição de desempenho --------------------------------------------------
def operação_demorada(n):
    somar = 0
    for i in range(n):
        somar += i
    return somar
print(operação_demorada(1000))


# ---------------------------------------- (DEPOIS) Medição de desempenho -------------------------------------------------
import time

def timer(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f"A função: '{func.__name__}' levou {fim-inicio:.4f} seg para executar.")
        return resultado
    return wrapper

@timer
def operação_demorada(n):
    soma = 0
    for i in range(n):
        soma += i
    return soma
print(operação_demorada(1000))


# ---------------------------------------- (ANTES) Verificação de Login -------------------------------------------------
def delete_database():
    print("Banco de dados deletado com sucesso.")

delete_database()


# ---------------------------------------- (DEPOIS) Verificação de Login -------------------------------------------------
def check_permissão(user):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if user != 'admin':
                raise Exception("Acesso negado, usuário não tem permissão!")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@check_permissão(user="admin")
def delete_database():
    print("Banco de daos deletado com sucesso.")

# @check_permissão(user="guest")
# def delete_database():
#     print("Banco de dados deletado com sucesso.")

delete_database()


# ---------------------------------------- (ANTES) Cache de resultados -------------------------------------------------
def fibonacci(n):
    if n < 2:
        return n
    print(f"Chamada de fib {n}")
    return fibonacci(n-1) + fibonacci(n-2)

fibonacci(5)
fibonacci(8)



# ---------------------------------------- (DEPOIS) Cache de resultados -------------------------------------------------
from functools import lru_cache

@lru_cache(maxsize=32)
def fibonacci(n):
    if n < 2:
        return n
    print(f"Chamada de fib {n}")
    return fibonacci(n-1) + fibonacci(n-2)

fibonacci(5)
fibonacci(8)