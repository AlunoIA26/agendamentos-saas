import { useState, useMemo } from "react";
 
const POR_PAGINA = 10;
 
function formatarDataHora(valor) {
  return new Date(valor).toLocaleString("pt-BR", {
    day: "2-digit",
    month: "2-digit",
    year: "numeric",
    hour: "2-digit",
    minute: "2-digit",
  });
}
 
// Converte qualquer formato de data que a API devolva
// para "AAAA-MM-DD", o mesmo formato usado pelo
// <input type="date">.
function apenasData(valor) {
  const data = new Date(valor);
  if (isNaN(data)) return "";
  const ano = data.getFullYear();
  const mes = String(data.getMonth() + 1).padStart(2, "0");
  const dia = String(data.getDate()).padStart(2, "0");
  return `${ano}-${mes}-${dia}`;
}
 
// Verifica se alguma palavra do nome COMECA com o texto
// digitado: "s" encontra "Silva" e "Maria Souza",
// mas nao "Cassia".
function comecaCom(nome, busca) {
  const termo = busca.trim().toLowerCase();
  if (!termo) return true;
  return (nome || "")
    .toLowerCase()
    .split(/\s+/)
    .some((palavra) => palavra.startsWith(termo));
}
 
function dataHoje() {
  return apenasData(new Date());
}
 
function AgendaList({
  agendamentos,
  aoCancelar,
  aoConcluir,
}) {
  const [filtroData, setFiltroData] = useState(dataHoje());
  const [filtroCliente, setFiltroCliente] = useState("");
  const [filtroProfissional, setFiltroProfissional] =
    useState("");
  const [pagina, setPagina] = useState(1);
 
  const filtrados = useMemo(() => {
    return agendamentos.filter((a) => {
      if (
        filtroData &&
        apenasData(a.data_hora) !== filtroData
      ) {
        return false;
      }
      if (!comecaCom(a.cliente, filtroCliente)) return false;
      if (!comecaCom(a.profissional, filtroProfissional)) {
        return false;
      }
      return true;
    });
  }, [
    agendamentos,
    filtroData,
    filtroCliente,
    filtroProfissional,
  ]);
 
  const total = Math.ceil(filtrados.length / POR_PAGINA);
  const visiveis = filtrados.slice(
    (pagina - 1) * POR_PAGINA,
    pagina * POR_PAGINA
  );
 
  function aoMudarFiltro(fn) {
    fn();
    setPagina(1);
  }
 
  function limparFiltros() {
    setFiltroData("");
    setFiltroCliente("");
    setFiltroProfissional("");
    setPagina(1);
  }
 
  return (
    <div>
      <div className="filtros-agenda">
        <input
          type="date"
          value={filtroData}
          onChange={(e) =>
            aoMudarFiltro(() =>
              setFiltroData(e.target.value)
            )
          }
        />
        <input
          type="text"
          placeholder="Buscar cliente..."
          value={filtroCliente}
          onChange={(e) =>
            aoMudarFiltro(() =>
              setFiltroCliente(e.target.value)
            )
          }
        />
        <input
          type="text"
          placeholder="Buscar profissional..."
          value={filtroProfissional}
          onChange={(e) =>
            aoMudarFiltro(() =>
              setFiltroProfissional(e.target.value)
            )
          }
        />
        <button
          onClick={() =>
            aoMudarFiltro(() => setFiltroData(dataHoje()))
          }
        >
          Hoje
        </button>
        <button onClick={limparFiltros}>Ver todos</button>
      </div>
 
      {visiveis.length === 0 ? (
        <p>
          Nenhum agendamento encontrado para os filtros
          selecionados.
        </p>
      ) : (
        <table>
          <thead>
            <tr>
              <th>Data/Hora</th>
              <th>Cliente</th>
              <th>Profissional</th>
              <th>Serviço</th>
              <th>Status</th>
              <th>Ações</th>
            </tr>
          </thead>
          <tbody>
            {visiveis.map((agendamento) => (
              <tr key={agendamento.id}>
                <td>
                  {formatarDataHora(agendamento.data_hora)}
                </td>
                <td>{agendamento.cliente}</td>
                <td>{agendamento.profissional}</td>
                <td>{agendamento.servico}</td>
                <td>{agendamento.status}</td>
                <td className="acoes-agendamento">
                  {agendamento.status === "confirmado" && (
                    <>
                      <button
                        className="botao-concluir"
                        onClick={() =>
                          aoConcluir(agendamento.id)
                        }
                      >
                        ✓ Concluir
                      </button>
                      <button
                        className="botao-cancelar"
                        onClick={() =>
                          aoCancelar(agendamento.id)
                        }
                      >
                        ✕ Cancelar
                      </button>
                    </>
                  )}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
 
      {total > 1 && (
        <div className="paginacao">
          <button
            onClick={() =>
              setPagina((p) => Math.max(1, p - 1))
            }
            disabled={pagina === 1}
          >
            Anterior
          </button>
          <span>
            {pagina} / {total}
          </span>
          <button
            onClick={() =>
              setPagina((p) => Math.min(total, p + 1))
            }
            disabled={pagina === total}
          >
            Próxima
          </button>
        </div>
      )}
    </div>
  );
}
 
export default AgendaList;
