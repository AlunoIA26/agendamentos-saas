function Menu({ telaAtiva, aoTrocarTela }) {
  const telas = [
    { chave: "agenda", rotulo: "Agenda" },
    { chave: "clientes", rotulo: "Clientes" },
    { chave: "profissionais", rotulo: "Profissionais" },
    { chave: "servicos", rotulo: "Serviços" },
    { chave: "relatorios", rotulo: "Relatórios" },
  ];

  return (
    <nav>
      {telas.map((tela) => (
        <button
          key={tela.chave}
          onClick={() => aoTrocarTela(tela.chave)}
          style={{
            fontWeight:
              telaAtiva === tela.chave
                ? "bold"
                : "normal",
          }}
        >
          {tela.rotulo}
        </button>
      ))}
    </nav>
  );
}

export default Menu;