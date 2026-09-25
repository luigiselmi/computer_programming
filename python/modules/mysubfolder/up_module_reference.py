import sys
from pathlib import Path

# 1. Trova la cartella in cui si trova QUESTO specifico script .py
script_dir = Path(__file__).resolve().parent

# 2. Risali alla cartella superiore (la radice del progetto)
project_root = script_dir.parent

# 3. Aggiunge la radice a sys.path se non è già presente
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))  # Utilizziamo insert(0) per dare la priorità a questa cartella

# 4. Ora puoi fare l'import assoluto
from fibo import fib

def call_fibo(n):
    return fib(n)
