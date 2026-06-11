from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():

    dados = {
        "web_status": "🟢 Online"
    }

    return render_template(
        "dashboard.html",
        dados=dados
    )

if __name__ == "__main__":
    app.run(debug=True)