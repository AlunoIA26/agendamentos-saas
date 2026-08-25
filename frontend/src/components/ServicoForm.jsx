import { useState } from "react";

function ServicoForm({ aoSalvar }) {
  const [nome, setNome] = useState("");
  const [duracaoMinutos, setDuracaoMinutos] = useState("");
  const [preco, setPreco] = useState("");
  const [erro, setErro] = useState("");

  async function handleSubmit(evento) {
    evento.preventDefault();
    setErro("");

    try {
      await aoSalvar({
        nome,
        duracao_minutos: Number(duracaoMinutos),
        preco: Number(preco),
      });

      setNome("");
      setDuracaoMinutos("");
      setPreco("");
    } catch (erro) {
      setErro(
        erro.response?.data?.erro ||
        erro.message ||
        "Erro ao salvar serviço."
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
        type="number"
        placeholder="Duração em minutos"
        value={duracaoMinutos}
        onChange={(e) => setDuracaoMinutos(e.target.value)}
      />

      <input
        type="number"
        step="0.01"
        placeholder="Preço"
        value={preco}
        onChange={(e) => setPreco(e.target.value)}
      />

      <button type="submit">Salvar</button>

      {erro && <p>{erro}</p>}
    </form>
  );
}

export default ServicoForm;