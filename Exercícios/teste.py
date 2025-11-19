# generate_logs.py
"""
Gera 15k logs onde TODAS as mensagens estão corrompidas (mojibake).
- Não altera timestamp/IP/origem.
- Sem NUL.
Saída: dados/logs_corrompidos.txt
"""

from datetime import datetime, timedelta
from pathlib import Path
import random

# ---------- CONFIG ----------
TOTAL_LINES = 187564
OUT_PATH = Path("dados/logs_corrompidos.txt")
# ---------------------------

LEVELS  = ["LEVEL=INFO", "LEVEL=WARN", "LEVEL=ERROR", "LEVEL=DEBUG"]
ORIGINS = ["ORIGIN=app/web", "ORIGIN=proxy/edge", "ORIGIN=auth/service", "ORIGIN=worker/job"]
USERS   = ["ricardo", "ana", "joao", "maria", "luis", "catarina", "bruno", "ines"]

# Lista ÚNICA: todas as mensagens já com os erros (mojibake) pedidos
# Mapa aplicado previamente:
# 'á'→'Ã¡', 'à'→'Ã ', 'ã'→'Ã£', 'â'→'Ã¢',
# 'é'→'Ã©', 'ê'→'Ãª',
# 'í'→'Ã\xad', 'ó'→'Ã³', 'ô'→'Ã´', 'õ'→'Ãµ',
# 'ú'→'Ãº', 'ç'→'Ã§', 'Á'→'Ã\x81', 'É'→'Ã\x89'
MSG_TEMPLATES_BAD = [
    "Login efetuado",                      # (sem acentos afetados, fica igual)
    "Senha invÃ¡lida",
    "Token expirado",                      # (sem acentos afetados, fica igual)
    "Pagamento recusado",                  # (sem acentos afetados, fica igual)
    "Perfil atualizado",                   # (sem acentos afetados, fica igual)
    "RequisiÃ§Ã£o recebida",
    "Ficheiro nÃ£o encontrado",
    "I/O timeout",
    "Acesso negado",                       # (sem acentos afetados, fica igual)
    "OperaÃ§Ã£o concluÃ­da com sucesso",
    "CriaÃ§Ã£o de usuÃ¡rio",
    "AtualizaÃ§Ã£o de relatÃ³rio",
    "ConexÃ£o estabelecida",
    "SessÃ£o iniciada",
    "SessÃ£o terminada",
    "RelatÃ³rio gerado",
    "Erro de validaÃ§Ã£o",
    "ConfiguraÃ§Ãµes salvas",
    "SessÃ£o expirada",
    "AtualizaÃ§Ã£o pendente"
]

def random_ip():
    return "{}.{}.{}.{}".format(
        random.randint(1, 223),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(1, 254),
    )

def canonical_log(ts: datetime, level: str, ip: str, origin: str, msg: str, user: str) -> str:
    return f"{ts.strftime('%Y-%m-%dT%H:%M:%SZ')} {level} {ip} {origin} \"{msg}\" USER={user}"

def generate(total_lines: int):
    out = []
    now = datetime.utcnow()
    for i in range(total_lines):
        ts     = now + timedelta(seconds=i % 86400)
        level  = random.choice(LEVELS)
        ip     = random_ip()
        origin = random.choice(ORIGINS)
        user   = random.choice(USERS)
        msg    = random.choice(MSG_TEMPLATES_BAD)  # SEMPRE mensagem com erro
        line   = canonical_log(ts, level, ip, origin, msg, user)
        out.append(line)  # uso explícito de lista + append
    return out

def save(path: Path, lines):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', encoding='utf-8', newline='\n') as f:
        for l in lines:
            f.write(l + '\n')

if __name__ == "__main__":
    logs = generate(TOTAL_LINES)
    save(OUT_PATH, logs)
    print(f"Gerado {len(logs)} linhas em {OUT_PATH}")
