from flask import Flask, jsonify, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

# Configuração do Limiter
limiter = Limiter(
    get_remote_address,  # Identifica o cliente pelo endereço IP
    app=app,
    default_limits=["10000 per hour"],  # Limite padrão por ip em horas
)

# Função personalizada para lidar com erro 429
@app.errorhandler(429)
def ratelimit_error(e):
    return jsonify({
        "error": "Too Many Requests",
        "message": "Você excedeu o limite de solicitações permitido. Aguarde 1 minuto."
    }), 429

@app.route("/login")
@limiter.limit("10/minute") #limita por minuto a quantidade de login por 1 usuario
def minha_rota():
    ip_cliente = request.remote_addr  # Obtém o IP do cliente
    return jsonify({"message": "Bem-vindo à rota limitada!", "ip": ip_cliente})

if __name__ == "__main__":
    app.run(debug=True)