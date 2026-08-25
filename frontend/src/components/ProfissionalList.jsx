function ProfissionalList({ profissionais }) {
  return (
    <table>
      <thead>
        <tr>
          <th>Nome</th>
          <th>Especialidade</th>
        </tr>
      </thead>

      <tbody>
        {profissionais.map((profissional) => (
          <tr key={profissional.id}>
            <td>{profissional.nome}</td>
            <td>{profissional.especialidade}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default ProfissionalList;