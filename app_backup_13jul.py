from flask import Flask, render_template, jsonify
from supabase_client import obter_eventos_recentes

app = Flask(__name__)

@app.route('/')
def painel():
    eventos = obter_eventos_recentes()
    return render_template("painel.html", eventos=eventos)

@app.route('/dados')
def dados_em_json():
    eventos = obter_eventos_recentes()
    return jsonify(eventos)

if __name__ == '__main__':
    app.run(debug=True)