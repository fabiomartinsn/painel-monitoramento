from flask import Flask, render_template, jsonify
from supabase_client import obter_eventos_recentes

app = Flask(__name__)


@app.route("/confirmar/<id>", methods=["POST"])
def confirmar(id):
    print(f"Alerta confirmado: {id}")
    return f"Alerta {id} confirmado com sucesso!"

@app.route("/")
def painel():
    eventos = obter_eventos_recentes()
    return render_template("painel.html", eventos=eventos)

@app.route('/dados')
def dados_em_json():
    eventos = obter_eventos_recentes()
    return jsonify(eventos)

@app.route("/")
def index():
    return render_template("painel.html")

if __name__ == '__main__':
    app.run(debug=True)