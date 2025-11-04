import json
from pathlib import  Path

PORT_FILE = Path('port.json')

def load_port() -> list[int]:
    if not PORT_FILE.exists():
        return []
    try:
        with open(PORT_FILE, 'r') as f:
            data = json.load(f)
            return data.get('ports', [])
    except (json.decoder.JSONDecodeError, FileNotFoundError):
        return []

def save_port(port: list[int]) -> None:
    with open(PORT_FILE, 'w') as f:
        json.dump({'ports': port}, f)

def add_port(port: int) -> None:
    ports = load_port()
    if port not in ports:
        ports.append(port)
        save_port(ports)

def remove_port(port: int) -> None:
    ports = load_port()
    if port in ports:
        ports.remove(port)
        save_port(ports)
        print(f"Port {port} removed.")
    else:
        print(f"Port {port} is not in the list.")