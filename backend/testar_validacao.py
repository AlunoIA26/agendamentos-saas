from models.cliente import Cliente
 
try:
    Cliente(1, "Maria Silva", "11999990000", "email-invalido")
except ValueError as erro:
    print(f"Validação funcionou: {erro}")
 
cliente = Cliente(1, "Maria Silva", "11999990000", "maria@email.com")
print(cliente)
