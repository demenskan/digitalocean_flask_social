from flask import Flask

from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    #app.config.from_object(Config)
    # Initialize Flask extensions here

    # Register blueprints here
    from main import bp as main_bp
    app.register_blueprint(main_bp)

    from posts import bp as posts_bp
    app.register_blueprint(posts_bp, url_prefix='/posts')

    @app.route('/test/')
    def test_page():
        return '<h1>testing the flask application factory pattern</h1>'

    return app

main_app = create_app()

if __name__ == '__main__':
    main_app.run(debug=True, host='0.0.0.0', port=8000)
