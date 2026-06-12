from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():

    dados = {
        "web": {
            "status": "🟢 Online",
            "latencia": 42,
            "rps": 315
        },

        "database": {
            "status": "🟢 Online",
            "cpu": 38,
            "memoria": 62
        },

        "dns": {
            "status": "🟡 Atenção",
            "tempo": 180
        },

        "smtp": {
            "status": "🔴 Offline",
            "falhas": 12
        }
    }

    resumo = {
        "online": 2,
        "atencao": 1,
        "offline": 1,
        "disponibilidade": 75
    }

    seguranca = {
        "requests": 315,
        "tentativas_login": 12,
        "vulnerabilidades": 0
    }

    # Detecção automática
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

    return render_template(
        "dashboard.html",
        dados=dados,
        resumo=resumo,
        alertas=alertas,
        seguranca=seguranca
    )

if __name__ == "__main__":
    app.run(debug=True)