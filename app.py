from flask import Flask, render_template
from database import db
from config import Config
from flask_jwt_extended import JWTManager
from auth import auth_bp
from routes import routes_bp

app = Flask(__name__, static_folder="static", template_folder="templates")
app.config.from_object(Config)

db.init_app(app)
jwt = JWTManager(app)

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(routes_bp, url_prefix="/api")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/bemvindo")
def bemvindo():
    return render_template("bemvindo.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app.route("/trocar_senha")
def trocar_senha():
    return render_template("trocar_senha.html")

@app.route("/esqueci_senha")
def esqueci_senha():
    return render_template("esqueci_senha.html")

@app.route("/redefinir_senha")
def redefinir_senha():
    return render_template("redefinir_senha.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5001)
