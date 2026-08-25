import { useState } from "react";

function ProfissionalForm({ aoSalvar }) {
  const [nome, setNome] = useState("");
  const [especialidade, setEspecialidade] = useState("");
  const [erro, setErro] = useState("");

  async function handleSubmit(evento) {
    evento.preventDefault();
    setErro("");

    try {
      await aoSalvar({ nome, especialidade });

      setNome("");
      setEspecialidade("");
    } catch (erro) {
      setErro(
        erro.response?.data?.erro ||
        erro.message ||
        "Erro ao salvar profissional."
      );
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <input
        placeholder="Nome"
        value={nome}
        onChange={(e) => setNome(e.target.value)}
      />

      <input
        placeholder="Especialidade"
        value={especialidade}
        onChange={(e) => setEspecialidade(e.target.value)}
      />

      <button type="submit">Salvar</button>

      {erro && <p>{erro}</p>}
    </form>
  );
}

export default ProfissionalForm;