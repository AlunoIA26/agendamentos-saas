export async function buscarStatus() {
  const resposta = await fetch("http://localhost:5000/api/status");
  return resposta.json();
}
