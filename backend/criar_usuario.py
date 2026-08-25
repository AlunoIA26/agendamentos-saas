from werkzeug.security import generate_password_hash
from config.database import conectar

conexao = conectar()
cursor = conexao.cursor()

cursor.execute(
    "INSERT INTO usuarios (nome, email, senha_hash) VALUES (%s, %s, %s)",
    (
        "Administrador",
        "admin@salao.com",
        generate_password_hash("troque123"),
    ),
)

conexao.commit()
cursor.close()
conexao.close()

print("Usuario admin@salao.com criado com sucesso.")