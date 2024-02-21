from flask import Flask
from extensions import db
from config import Config

# Factory function
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    #app.config.from_object(Config)

    # Initialize Flask extensions here
    db.init_app(app)

    # Register blueprints here
    from main import bp as main_bp
    app.register_blueprint(main_bp)

    from posts import bp as posts_bp
    app.register_blueprint(posts_bp, url_prefix='/posts')

    from questions import bp as questions_bp
    app.register_blueprint(questions_bp, url_prefix='/questions')

    @app.route('/create/')
    def create_skeleton():
        db.create_all()
        return '<h1>initial migration...</h1>'

    @app.route('/test/')
    def test_page():
        return '<h1>testing the flask application factory pattern</h1>'

    return app

main_app = create_app()

if __name__ == '__main__':
    main_app.run(debug=True, host='0.0.0.0', port=8000)
