import { useEffect, useState } from "react";
import { buscarStatus } from "./services/api";
 
function App() {
  const [status, setStatus] = useState(null);
 
  useEffect(() => {
    buscarStatus().then(setStatus);
  }, []);
 
  return (
    <div>
      <h1>Agendamentos SaaS</h1>
      {status ? (
        <p>Backend conectado: {status.sistema} ({status.status})</p>
      ) : (
        <p>Conectando ao backend...</p>
      )}
    </div>
  );
}
 
export default App;
