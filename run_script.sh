if [ ! -d "venv" ]; then
    python -m venv venv 
fi

if [ -d "venv" ]; then
    source venv/bin/activate
fi

pip install -r requirements.txt

python user.py