import { useState } from "react";
import { login } from "../services/api";

function LoginForm({ aoEntrar }) {
  const [email, setEmail] = useState("");
  const [senha, setSenha] = useState("");
  const [erro, setErro] = useState(null);

  async function handleSubmit(evento) {
    evento.preventDefault();

    try {
      setErro(null);
      await login(email, senha);
      aoEntrar();
    } catch (e) {
      setErro(e.message);
    }
  }

  return (
    <form className="login-card" onSubmit={handleSubmit}>
      <h1>Agendamentos SaaS</h1>

      <p>Entre para acessar a agenda</p>

      {erro && <p className="erro">{erro}</p>}

      <input
        type="email"
        placeholder="E-mail"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />

      <input
        type="password"
        placeholder="Senha"
        value={senha}
        onChange={(e) => setSenha(e.target.value)}
      />

      <button type="submit">Entrar</button>
    </form>
  );
}

export default LoginForm;