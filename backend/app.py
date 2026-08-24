from flask import Flask, jsonify
from flask_cors import CORS

from routes.cliente_routes import cliente_bp
from routes.profissional_routes import profissional_bp
from routes.servico_routes import servico_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(cliente_bp)
app.register_blueprint(profissional_bp)
app.register_blueprint(servico_bp)


@app.route("/api/status")
def status():
    return jsonify({
        "status": "ok",
        "sistema": "Agendamentos SaaS"
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000)