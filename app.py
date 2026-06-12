from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def home():

    with open("metrics.json", "r", encoding="utf-8") as arquivo:
        metrics = json.load(arquivo)

    dados = {
        "web": metrics["web"],
        "database": metrics["database"],
        "dns": metrics["dns"],
        "smtp": metrics["smtp"]
    }

    resumo = {
        "online": 2,
        "atencao": 1,
        "offline": 1,
        "disponibilidade": 75
    }

    seguranca = metrics["seguranca"]

    seguranca["ddos"] = (
        "Sim" if seguranca["requests"] > 1000 else "Não"
    )

    seguranca["bruteforce"] = (
        "Sim" if seguranca["tentativas_login"] > 50 else "Não"
    )

    alertas = []

    if dados["web"]["latencia"] > 45:
        alertas.append("🟡 Latência acima do recomendado")

    if dados["smtp"]["status"] == "🔴 Offline":
        alertas.append("🔴 Serviço SMTP Offline")

    if seguranca["ddos"] == "Sim":
        alertas.append("🛡️ Possível ataque DDoS detectado")

    if seguranca["bruteforce"] == "Sim":
        alertas.append("🛡️ Possível ataque de força bruta detectado")
    notificacao = {
    "destinatario": "admin@netwatch.local",
    "mensagem": alertas[0] if alertas else "Nenhum alerta",
    "status": "Enviado"
}
    return render_template(
        "dashboard.html",
        dados=dados,
        resumo=resumo,
        alertas=alertas,
        seguranca=seguranca,
        notificacao=notificacao
    )

if __name__ == "__main__":
    app.run(debug=True)