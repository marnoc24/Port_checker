import dearpygui.dearpygui as dpg
from .controller import get_ports, add_new_port, delete_port, scan_ports


def update_port_list():
    ports = get_ports()
    dpg.delete_item("ports_list", children_only=True)
    for p in ports:
        dpg.add_text(f"{p}", parent="ports_list")


def on_add_port(sender, app_data):
    value = dpg.get_value("new_port_input")
    if value.isdigit() and 0 < int(value) < 1024:
        add_new_port(int(value))
        update_port_list()


def on_remove_port(sender, app_data):
    value = dpg.get_value("new_port_input")
    if value.isdigit():
        delete_port(int(value))
        update_port_list()


def on_scan(sender, app_data):
    host = dpg.get_value("host_input")
    results = scan_ports(host)
    dpg.delete_item("result_list", children_only=True)
    for port, opened in results.items():
        txt = f"{port}: {'OPEN' if opened else 'CLOSED'}"
        dpg.add_text(txt, parent="result_list")


def run_gui():
    dpg.create_context()

    with dpg.window(label="Port Checker by Emes", width=650, height=550, no_move=True, no_collapse=True, no_close=True,):
        dpg.add_text("Host address(127.0.0.1 = localhost):")
        dpg.add_input_text(tag="host_input", default_value="127.0.0.1", width=200)

        dpg.add_separator()
        dpg.add_text("Port to add / remove port:")
        dpg.add_input_text(tag="new_port_input", width=100)
        with dpg.group(horizontal=False):
            dpg.add_button(label="Add port", callback=on_add_port)
            dpg.add_button(label="Remove port", callback=on_remove_port)

        dpg.add_separator()
        dpg.add_button(label="Scan", callback=on_scan)

        dpg.add_separator()
        dpg.add_text("Saved ports:")
        dpg.add_child_window(tag="ports_list", width=180, height=100)

        dpg.add_separator()
        dpg.add_text("Scan results:")
        dpg.add_child_window(tag="result_list", width=200, height=120)

    dpg.create_viewport(title="Port Checker", width=650, height=550, resizable=False)
    dpg.set_viewport_small_icon("assets/icon16.ico")
    dpg.set_viewport_large_icon("assets/icon32.ico")
    dpg.setup_dearpygui()
    dpg.show_viewport()
    update_port_list()
    dpg.start_dearpygui()
    dpg.destroy_context()