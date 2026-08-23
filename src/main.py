import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from ui.main_menu import Menu

menu = Menu()
while True:
    menu.menu()