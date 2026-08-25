import { useEffect, useState } from "react";
import Menu from "./components/Menu";
import AgendaList from "./components/AgendaList";
import NovoAgendamentoForm from "./components/NovoAgendamentoForm";
import ClienteList from "./components/ClienteList";
import ClienteForm from "./components/ClienteForm";
import ProfissionalList from "./components/ProfissionalList";
import ProfissionalForm from "./components/ProfissionalForm";
import ServicoList from "./components/ServicoList";
import ServicoForm from "./components/ServicoForm";
import LoginForm from "./components/LoginForm";
import RelatorioFaturamento from "./components/RelatorioFaturamento";

import {
  listarClientes,
  criarCliente,
  listarProfissionais,
  criarProfissional,
  listarServicos,
  criarServico,
  listarAgendamentos,
  criarAgendamento,
  cancelarAgendamento,
  concluirAgendamento,
  estaLogado,
  sair,
} from "./services/api";

function App() {
  const [telaAtiva, setTelaAtiva] = useState("agenda");
  const [clientes, setClientes] = useState([]);
  const [profissionais, setProfissionais] = useState([]);
  const [servicos, setServicos] = useState([]);
  const [agendamentos, setAgendamentos] = useState([]);
  const [erro, setErro] = useState(null);
  const [logado, setLogado] = useState(estaLogado());

  useEffect(() => {
    if (!logado) return;

    listarClientes().then(setClientes);
    listarProfissionais().then(setProfissionais);
    listarServicos().then(setServicos);
    listarAgendamentos().then(setAgendamentos);
  }, [logado]);

  if (!logado) {
    return <LoginForm aoEntrar={() => setLogado(true)} />;
  }

  async function adicionarCliente(novoCliente) {
    try {
      setErro(null);
      const criado = await criarCliente(novoCliente);
      setClientes([...clientes, criado]);
    } catch (e) {
      setErro(e.message);
    }
  }

  async function adicionarProfissional(novoProfissional) {
    try {
      setErro(null);
      const criado = await criarProfissional(novoProfissional);
      setProfissionais([...profissionais, criado]);
    } catch (e) {
      setErro(e.message);
    }
  }

  async function adicionarServico(novoServico) {
    try {
      setErro(null);
      const criado = await criarServico(novoServico);
      setServicos([...servicos, criado]);
    } catch (e) {
      setErro(e.message);
    }
  }

  async function adicionarAgendamento(novoAgendamento) {
    try {
      setErro(null);
      await criarAgendamento(novoAgendamento);
      listarAgendamentos().then(setAgendamentos);
    } catch (e) {
      setErro(e.message);
    }
  }

  async function cancelarAgendamentoNaTela(id) {
    try {
      setErro(null);
      await cancelarAgendamento(id);
      listarAgendamentos().then(setAgendamentos);
    } catch (e) {
      setErro(e.message);
    }
  }

  async function concluirAgendamentoNaTela(id) {
    try {
      setErro(null);
      await concluirAgendamento(id);
      listarAgendamentos().then(setAgendamentos);
    } catch (e) {
      setErro(e.message);
    }
  }

  return (
    <div>
      <Menu
        telaAtiva={telaAtiva}
        aoTrocarTela={setTelaAtiva}
      />

      <button
        className="botao-sair"
        onClick={() => {
          sair();
          setLogado(false);
        }}
      >
        Sair
      </button>

      {erro && <p style={{ color: "red" }}>{erro}</p>}

      {telaAtiva === "agenda" && (
        <div>
          <h1>Agenda</h1>

          <NovoAgendamentoForm
            clientes={clientes}
            profissionais={profissionais}
            servicos={servicos}
            aoSalvar={adicionarAgendamento}
          />

          <AgendaList
            agendamentos={agendamentos}
            aoCancelar={cancelarAgendamentoNaTela}
            aoConcluir={concluirAgendamentoNaTela}
          />
        </div>
      )}

      {telaAtiva === "clientes" && (
        <div>
          <h1>Clientes</h1>
          <ClienteForm aoSalvar={adicionarCliente} />
          <ClienteList clientes={clientes} />
        </div>
      )}

      {telaAtiva === "profissionais" && (
        <div>
          <h1>Profissionais</h1>
          <ProfissionalForm aoSalvar={adicionarProfissional} />
          <ProfissionalList profissionais={profissionais} />
        </div>
      )}

      {telaAtiva === "servicos" && (
        <div>
          <h1>Serviços</h1>
          <ServicoForm aoSalvar={adicionarServico} />
          <ServicoList servicos={servicos} />
        </div>
      )}

      {telaAtiva === "relatorios" && (
        <div>
          <h1>Relatório de Faturamento</h1>
          <RelatorioFaturamento />
        </div>
      )}
    </div>
  );
}

export default App;