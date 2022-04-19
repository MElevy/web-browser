import PySimpleGUI as sg
import webbrowser as web
from threading import Thread
import webview as wv
import time

searchbarwindow = sg.Window('Web browser', [
    [sg.In(key = 'q'), sg.B('Search')],
    [sg.Radio('Open a new window', 'open-settings', key = 'window', default = True), sg.Radio('Open a new page on the web', 'open-settings', key = 'web')]
])

program_running = True
page = None

def open_window():
    wv.start()
    Thread(target = searchbarloop).start()

def searchbarloop():
    global program_running
    global page
    while 1:
        event, values = searchbarwindow.read(timeout = 100)
        if event == None:
            program_running = False
            break
        elif event == 'Search':
            if values['window']:
                wv.create_window(f'{values["q"]}', f'https://duckduckgo.com/?q={values["q"].replace(" ", "+")}')
                page = values['q']
            else:
               web.open(f'https://duckduckgo.com/?q={values["q"].replace(" ", "+")}')


Thread(target = searchbarloop).start()
while 1:
    try:
        if not program_running:
            break
        elif page:
            open_window()
            page = None
    finally:
        time.sleep(.01)
