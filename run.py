from application import create_app
from constants import APP_PORT, FLASK_ENV

print(FLASK_ENV)

# Press the green button in the gutter to run the script.
app, db, migrate = create_app()
if __name__ == '__main__':
    app.run(debug=FLASK_ENV == 'development', port=APP_PORT, host='0.0.0.0')


