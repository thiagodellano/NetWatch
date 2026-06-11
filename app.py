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

    alertas = []

    if dados["web"]["latencia"] > 45:
        alertas.append("🟡 Latência acima do recomendado")

    if dados["smtp"]["status"] == "🔴 Offline":
        alertas.append("🔴 Serviço SMTP Offline")

    return render_template(
        "dashboard.html",
        dados=dados,
        resumo=resumo,
        alertas=alertas
    )

if __name__ == "__main__":
    app.run(debug=True)