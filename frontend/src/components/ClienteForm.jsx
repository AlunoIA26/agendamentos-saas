import { useState } from "react";
 
function ClienteForm({ aoSalvar }) {
  const [nome, setNome] = useState("");
  const [telefone, setTelefone] = useState("");
  const [email, setEmail] = useState("");
 
  function handleSubmit(evento) {
    evento.preventDefault();
    aoSalvar({ nome, telefone, email });
    setNome("");
    setTelefone("");
    setEmail("");
  }
 
  return (
    <form onSubmit={handleSubmit}>
      <input
        placeholder="Nome"
        value={nome}
        onChange={(e) => setNome(e.target.value)}
      />
      <input
        placeholder="Telefone"
        value={telefone}
        onChange={(e) => setTelefone(e.target.value)}
      />
      <input
        placeholder="E-mail"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />
      <button type="submit">Salvar</button>
    </form>
  );
}
 
export default ClienteForm;
