import { useEffect, useState } from "react";

import {
  buscarFaturamento,
  urlExportacaoCsv,
  urlExportacaoExcel,
} from "../services/api";

const moeda = new Intl.NumberFormat("pt-BR", {
  style: "currency",
  currency: "BRL",
});

// Primeiro dia do mês atual, no formato AAAA-MM-DD.
function inicioDoMes() {
  const hoje = new Date();
  const mes = String(hoje.getMonth() + 1).padStart(2, "0");

  return `${hoje.getFullYear()}-${mes}-01`;
}

// Data de hoje no formato AAAA-MM-DD.
function hoje() {
  const d = new Date();
  const mes = String(d.getMonth() + 1).padStart(2, "0");
  const dia = String(d.getDate()).padStart(2, "0");

  return `${d.getFullYear()}-${mes}-${dia}`;
}

function RelatorioFaturamento() {
  const [linhas, setLinhas] = useState([]);
  const [inicio, setInicio] = useState(inicioDoMes());
  const [fim, setFim] = useState(hoje());
  const [carregando, setCarregando] = useState(false);

  function carregar() {
    setCarregando(true);

    buscarFaturamento(inicio, fim)
      .then(setLinhas)
      .finally(() => setCarregando(false));
  }

  useEffect(() => {
    carregar();

    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [inicio, fim]);

  function verTudo() {
    setInicio("");
    setFim("");
  }

  function esteMes() {
    setInicio(inicioDoMes());
    setFim(hoje());
  }

  const totalFaturamento = linhas.reduce(
    (soma, linha) => soma + Number(linha.faturamento),
    0
  );

  const totalAtendimentos = linhas.reduce(
    (soma, linha) => soma + Number(linha.atendimentos),
    0
  );

  const ticketMedio =
    totalAtendimentos > 0
      ? totalFaturamento / totalAtendimentos
      : 0;

  return (
    <div>
      <div className="filtros-relatorio">
        <label>
          De
          <input
            type="date"
            value={inicio}
            onChange={(e) => setInicio(e.target.value)}
          />
        </label>

        <label>
          Até
          <input
            type="date"
            value={fim}
            onChange={(e) => setFim(e.target.value)}
          />
        </label>

        <button onClick={esteMes}>
          Este mês
        </button>

        <button onClick={verTudo}>
          Todo o período
        </button>
      </div>

      {carregando && (
        <p>Carregando relatório...</p>
      )}

      {!carregando && linhas.length === 0 ? (
        <p>
          Nenhum atendimento concluído no período
          selecionado.
        </p>
      ) : (
        !carregando && (
          <>
            <div className="cards-resumo">
              <div className="card">
                <div className="card-titulo">
                  Faturamento total
                </div>

                <div className="card-valor">
                  {moeda.format(totalFaturamento)}
                </div>
              </div>

              <div className="card">
                <div className="card-titulo">
                  Atendimentos concluídos
                </div>

                <div className="card-valor">
                  {totalAtendimentos}
                </div>
              </div>

              <div className="card">
                <div className="card-titulo">
                  Ticket médio
                </div>

                <div className="card-valor">
                  {moeda.format(ticketMedio)}
                </div>
              </div>
            </div>

            <table>
              <thead>
                <tr>
                  <th>Profissional</th>
                  <th>Atendimentos</th>
                  <th>Faturamento</th>
                </tr>
              </thead>

              <tbody>
                {linhas.map((linha) => (
                  <tr key={linha.profissional_id}>
                    <td>{linha.profissional}</td>
                    <td>{linha.atendimentos}</td>
                    <td>
                      {moeda.format(
                        Number(linha.faturamento)
                      )}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>

            <a
              className="botao"
              href={urlExportacaoExcel(inicio, fim)}
            >
              Baixar Excel
            </a>

            <a
              className="botao-secundario"
              href={urlExportacaoCsv(inicio, fim)}
            >
              Baixar CSV
            </a>

            <button onClick={carregar}>
              Atualizar
            </button>
          </>
        )
      )}
    </div>
  );
}

export default RelatorioFaturamento;