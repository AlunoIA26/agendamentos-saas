from config.database import conectar


class UsuarioRepository:
    def buscar_por_email(self, email):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "SELECT id, nome, email, senha_hash FROM usuarios WHERE email = %s",
            (email,),
        )

        linha = cursor.fetchone()

        cursor.close()
        conexao.close()

        return linha