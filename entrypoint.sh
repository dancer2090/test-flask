echo "Initializing - server will start in 10 sec"
sleep 10

echo "Force migrations"
flask db migrate
flask db upgrade

echo "Run the app"
python3 run.py