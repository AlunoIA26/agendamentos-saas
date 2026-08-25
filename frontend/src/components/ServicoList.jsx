function ServicoList({ servicos }) {
  const formatarPreco = new Intl.NumberFormat("pt-BR", {
    style: "currency",
    currency: "BRL",
  });

  return (
    <table>
      <thead>
        <tr>
          <th>Nome</th>
          <th>Duração</th>
          <th>Preço</th>
        </tr>
      </thead>

      <tbody>
        {servicos.map((servico) => (
          <tr key={servico.id}>
            <td>{servico.nome}</td>
            <td>{servico.duracao_minutos} minutos</td>
            <td>{formatarPreco.format(servico.preco)}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default ServicoList;