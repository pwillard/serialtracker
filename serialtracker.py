#-------------------------------------------------------------------------------
# Name:        SerialTracker.py
# Purpose:     Simple tracker for active serial ports attached to windows PC
#
# Author:      Pete Willard
#
# Created:     15/08/2023
# Copyright:   (c) willard 2023
# Licence:     CC BY-NC-SA
#-------------------------------------------------------------------------------
import serial.tools.list_ports
import time
import PySimpleGUI as sg

def main():
    layout = [
        [sg.Text("Available Serial Ports:")],
        [sg.Listbox(values=[], size=(40, 10), key="-PORTS-")],
        [sg.Button("Exit")]
    ]

    window = sg.Window("Port Tracker", layout)

    while True:
        event, values = window.read(timeout=1000)  # Auto-update every 1000 milliseconds

        if event == sg.WINDOW_CLOSED or event == "Exit":
            break

        refresh_ports(window)

    window.close()

def refresh_ports(window):
    ports = [port.device for port in serial.tools.list_ports.comports()]
    window["-PORTS-"].update(values=ports)

if __name__ == "__main__":
    main()
