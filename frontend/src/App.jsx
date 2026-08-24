import { useState } from "react";
import ClienteList from "./components/ClienteList";
import ClienteForm from "./components/ClienteForm";
 
const clientesIniciais = [
  { id: 1, nome: "Maria Silva", telefone: "11999990000", email: "maria@email.com" },
];
 
function App() {
  const [clientes, setClientes] = useState(clientesIniciais);
 
  function adicionarCliente(novoCliente) {
    setClientes([...clientes, { ...novoCliente, id: Date.now() }]);
  }
 
  return (
    <div>
      <h1>Clientes</h1>
      <ClienteForm aoSalvar={adicionarCliente} />
      <ClienteList clientes={clientes} />
    </div>
  );
}
 
export default App;
