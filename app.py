from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():

    dados = {
        "web_status": "🟢 Online",
        "latencia": 42,
        "rps": 315,

        "db_status": "🟢 Online",
        "cpu": 38,
        "memoria": 62,

        "dns_status": "🟡 Atenção",
        "dns_tempo": 180,

        "smtp_status": "🔴 Offline",
        "smtp_falhas": 12


    }

    return render_template(
        "dashboard.html",
        dados=dados
    )

if __name__ == "__main__":
    app.run(debug=True)