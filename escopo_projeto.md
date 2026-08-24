# Escopo do projeto: SaaS de Agendamentos
 
## Entidades
- Cliente: id, nome, telefone, email
- Profissional: id, nome, especialidade
- Servico: id, nome, duracao_minutos, preco
- Agendamento: id, cliente_id, profissional_id, servico_id, data_hora, status
 
## Regras de negocio
- Um profissional nao pode ter dois agendamentos no mesmo horario.
- O horario do agendamento respeita a duracao do servico escolhido.
- Um agendamento cancelado libera o horario para outro cliente.
 
## Fora do escopo (versao futura)
- Pagamento online
- Notificacoes por e-mail/SMS
- Atendimento a mais de um negocio (multi-tenant)
