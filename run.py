from application import create_app
from constants import APP_PORT, FLASK_ENV


app, db, migrate = create_app()
if __name__ == '__main__':
    if FLASK_ENV == 'production':
        from waitress import serve
        serve(app, port=APP_PORT, host='0.0.0.0')
    else:
        app.run(debug=FLASK_ENV == 'development', port=APP_PORT, host='0.0.0.0')


