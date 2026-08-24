function ClienteList({ clientes }) {
  return (
    <table>
      <thead>
        <tr>
          <th>Nome</th>
          <th>Telefone</th>
          <th>E-mail</th>
        </tr>
      </thead>
      <tbody>
        {clientes.map((cliente) => (
          <tr key={cliente.id}>
            <td>{cliente.nome}</td>
            <td>{cliente.telefone}</td>
            <td>{cliente.email}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
 
export default ClienteList;
