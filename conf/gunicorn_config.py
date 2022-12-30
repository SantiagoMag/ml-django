import os

command = os.path.abspath(os.getcwd()) + r'/.venv/bin/gunicorn'
pythonpath = os.path.abspath(os.getcwd())
bind = "localhost"
workers = 3