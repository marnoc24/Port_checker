# Port_Checker

Lightweight TCP port scanner with a simple graphical user interface (GUI) written in Python using Dear PyGui. The application scans a given host/IP for open ports and displays results in the GUI.

## Features
- Scan a specified TCP port range
- Simple Dear PyGui interface for starting scans and viewing results
- Application icons included in `port_checker/assets`

## Requirements
- Python 3.10+ (Windows)
- Dear PyGui (GUI library)
- Socket

## Installation (Windows)
1. Clone or copy the project to:
   `c:\Users\Marcin\Desktop\Programowanie\Python_DS\Port_Checker`
2. (Optional) Create and activate a virtual environment:
   - python -m venv venv
   - .\venv\Scripts\activate
3. Install Dear PyGui:
   - pip install dearpygui
   - (Optionally add to requirements.txt: `dearpygui`)
4. Run the application:
   - python main.py

## Usage
1. Enter a hostname or IP address in the GUI.
2. Enter a port range to scan (e.g., `1-1024`).
3. Start the scan and wait for results — open ports will be listed in the interface.

## Project structure
- main.py — application entry point (starts the GUI)
- port_checker/
  - gui.py — Dear PyGui user interface logic
  - controller.py — coordination between GUI and scanner
  - scanner.py — port scanning functions
  - utils.py — helper utilities
  - assets/ — application icons
  - __init__.py

## Notes
- Dear PyGui is required for the GUI; without it the application will not run.
- Consider adding command-line mode or unit tests under a `tests/` directory for headless testing.
- Add a LICENSE file (e.g., MIT) if you plan to publish the project.