from flask import jsonify
from app.dao.db import get_db
import hashlib

def login_cliente(cpf, senha, otp):
    db = get_db()
    cursor = db.cursor()

    senha_hash = hashlib.md5(senha.encode()).hexdigest()
    cursor.execute("""
        SELECT * FROM usuario
        WHERE cpf = %s AND senha_hash = %s AND tipo_usuario = 'CLIENTE'
    """, (cpf, senha_hash))
    usuario = cursor.fetchone()

    if usuario and usuario['otp_ativo'] == otp:
        return jsonify({"mensagem": "Login bem-sucedido", "usuario": usuario['nome']}), 200
    return jsonify({"erro": "Login inválido"}), 401
