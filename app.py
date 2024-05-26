from flask import Flask
from controllers.sentiment_controller import sentiment_bp
from controllers.home_controller import home_bp
from controllers.health_controller import health_bp

app = Flask(__name__)

app.register_blueprint(sentiment_bp)
app.register_blueprint(home_bp)
app.register_blueprint(health_bp)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
