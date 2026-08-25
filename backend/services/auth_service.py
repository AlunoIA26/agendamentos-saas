import os
from datetime import datetime, timedelta, timezone

import jwt
from werkzeug.security import check_password_hash

from repositories.usuario_repository import UsuarioRepository


CHAVE_SECRETA = os.getenv("JWT_SECRET", "chave-de-desenvolvimento")


class AuthService:
    def __init__(self):
        self.repository = UsuarioRepository()

    def login(self, email, senha):
        usuario = self.repository.buscar_por_email(email)

        if usuario is None or not check_password_hash(usuario[3], senha):
            raise ValueError("E-mail ou senha inválidos.")

        payload = {
            "usuario_id": usuario[0],
            "nome": usuario[1],
            "exp": datetime.now(timezone.utc) + timedelta(hours=8),
        }

        return jwt.encode(
            payload,
            CHAVE_SECRETA,
            algorithm="HS256",
        )

    def validar_token(self, token):
        return jwt.decode(
            token,
            CHAVE_SECRETA,
            algorithms=["HS256"],
        )