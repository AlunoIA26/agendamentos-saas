const BASE_URL = "http://localhost:5000";

export async function buscarStatus() {
  const resposta = await fetch(`${BASE_URL}/api/status`);
  return resposta.json();
}

export async function listarClientes() {
  const resposta = await fetch(`${BASE_URL}/api/clientes`);
  return resposta.json();
}

export async function criarCliente(cliente) {
  const resposta = await fetch(`${BASE_URL}/api/clientes`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(cliente),
  });

  const dados = await resposta.json();

  if (!resposta.ok) {
    throw new Error(dados.erro || "Erro ao criar cliente.");
  }

  return dados;
}

export async function listarAgendamentos() {
  const resposta = await fetch(`${BASE_URL}/api/agendamentos`, {
    headers: cabecalhoAutenticado(),
  });

  return resposta.json();
}

export async function criarAgendamento(agendamento) {
  const resposta = await fetch(`${BASE_URL}/api/agendamentos`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      ...cabecalhoAutenticado(),
    },
    body: JSON.stringify(agendamento),
  });

  const dados = await resposta.json();

  if (!resposta.ok) {
    throw new Error(dados.erro || "Erro ao criar agendamento.");
  }

  return dados;
}

export async function listarProfissionais() {
  const resposta = await fetch(`${BASE_URL}/api/profissionais`);
  return resposta.json();
}

export async function criarProfissional(profissional) {
  const resposta = await fetch(`${BASE_URL}/api/profissionais`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(profissional),
  });

  const dados = await resposta.json();

  if (!resposta.ok) {
    throw new Error(dados.erro || "Erro ao criar profissional.");
  }

  return dados;
}

export async function listarServicos() {
  const resposta = await fetch(`${BASE_URL}/api/servicos`);
  return resposta.json();
}

export async function criarServico(servico) {
  const resposta = await fetch(`${BASE_URL}/api/servicos`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(servico),
  });

  const dados = await resposta.json();

  if (!resposta.ok) {
    throw new Error(dados.erro || "Erro ao criar serviço.");
  }

  return dados;
}

export async function cancelarAgendamento(id) {
  const resposta = await fetch(
    `${BASE_URL}/api/agendamentos/${id}/cancelar`,
    {
      method: "POST",
      headers: cabecalhoAutenticado(),
    }
  );

  const dados = await resposta.json();

  if (!resposta.ok) {
    throw new Error(
      dados.erro || "Erro ao cancelar agendamento."
    );
  }

  return dados;
}

export async function concluirAgendamento(id) {
  const resposta = await fetch(
    `${BASE_URL}/api/agendamentos/${id}/concluir`,
    {
      method: "POST",
      headers: cabecalhoAutenticado(),
    }
  );

  const dados = await resposta.json();

  if (!resposta.ok) {
    throw new Error(
      dados.erro || "Erro ao concluir agendamento."
    );
  }

  return dados;
}

export async function login(email, senha) {
  const resposta = await fetch(`${BASE_URL}/api/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, senha }),
  });

  const dados = await resposta.json();

  if (!resposta.ok) {
    throw new Error(
      dados.erro || "Não foi possível entrar."
    );
  }

  localStorage.setItem("token", dados.token);

  return dados;
}

export function estaLogado() {
  return localStorage.getItem("token") !== null;
}

export function sair() {
  localStorage.removeItem("token");
}

export function cabecalhoAutenticado() {
  return {
    Authorization: `Bearer ${localStorage.getItem("token")}`,
  };
}

export async function buscarFaturamento(inicio, fim) {
  const params = new URLSearchParams();

  if (inicio) params.set("inicio", inicio);
  if (fim) params.set("fim", fim);

  const query = params.toString()
    ? `?${params.toString()}`
    : "";

  const resposta = await fetch(
    `${BASE_URL}/api/relatorios/faturamento${query}`,
    {
      headers: cabecalhoAutenticado(),
    }
  );

  const dados = await resposta.json();

  if (!resposta.ok) {
    throw new Error(
      dados.erro || "Erro ao buscar faturamento."
    );
  }

  return dados;
}


export function urlExportacaoCsv(inicio, fim) {
  const params = new URLSearchParams();

  if (inicio) params.set("inicio", inicio);
  if (fim) params.set("fim", fim);

  const query = params.toString()
    ? `?${params.toString()}`
    : "";

  return `${BASE_URL}/api/relatorios/faturamento/csv${query}`;
}


export function urlExportacaoExcel(inicio, fim) {
  const params = new URLSearchParams();

  if (inicio) params.set("inicio", inicio);
  if (fim) params.set("fim", fim);

  const query = params.toString()
    ? `?${params.toString()}`
    : "";

  return `${BASE_URL}/api/relatorios/faturamento/excel${query}`;
}