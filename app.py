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

    return render_template(
        "dashboard.html",
        dados=dados
    )

if __name__ == "__main__":
    app.run(debug=True)