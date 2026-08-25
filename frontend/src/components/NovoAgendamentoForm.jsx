import { useState } from "react";
 
function NovoAgendamentoForm({ clientes, profissionais, servicos, aoSalvar }) {
  const [clienteId, setClienteId] = useState("");
  const [profissionalId, setProfissionalId] = useState("");
  const [servicoId, setServicoId] = useState("");
  const [dataHora, setDataHora] = useState("");
 
  function handleSubmit(evento) {
    evento.preventDefault();
    aoSalvar({
      cliente_id: Number(clienteId),
      profissional_id: Number(profissionalId),
      servico_id: Number(servicoId),
      data_hora: dataHora,
    });
    setClienteId("");
    setProfissionalId("");
    setServicoId("");
    setDataHora("");
  }
 
  return (
    <form onSubmit={handleSubmit}>
      <select value={clienteId} onChange={(e) => setClienteId(e.target.value)}>
        <option value="">Selecione o cliente</option>
        {clientes.map((c) => (
          <option key={c.id} value={c.id}>{c.nome}</option>
        ))}
      </select>
 
      <select value={profissionalId} onChange={(e) => setProfissionalId(e.target.value)}>
        <option value="">Selecione o profissional</option>
        {profissionais.map((p) => (
          <option key={p.id} value={p.id}>{p.nome}</option>
        ))}
      </select>
 
      <select value={servicoId} onChange={(e) => setServicoId(e.target.value)}>
        <option value="">Selecione o serviço</option>
        {servicos.map((s) => (
          <option key={s.id} value={s.id}>{s.nome}</option>
        ))}
      </select>
 
      <input
        type="datetime-local"
        value={dataHora}
        onChange={(e) => setDataHora(e.target.value)}
      />
 
      <button type="submit">Agendar</button>
    </form>
  );
}
 
export default NovoAgendamentoForm;
