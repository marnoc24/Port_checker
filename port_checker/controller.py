from .utils import load_port, add_port, remove_port
from .scanner import check_port

def get_ports() -> list[int]:
    return load_port()

def add_new_port(port: int) -> None:
    add_port(port)

def delete_port(port: int) -> None:
    remove_port(port)

def scan_ports(host: str) -> dict[int, bool]:
    ports = load_port()
    results = {}
    for p in ports:
        results[p] = check_port(host, p)
    return results