import wx
from time import sleep

import mealtrackerfrontend.configuration as configuration
from .server_requests import ServerRequest

from .panels.panel_switcher import PanelsSwitcher
from .panels.home_panel import HomePanel
from .panels.insertion_panel import InsertionPanel

class MainFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, id=1, title='Meal Tracker')

        self.SetMinSize(wx.Size(500,500))
        self.SetMaxSize(wx.Size(800,800))

        panels_switcher = \
            PanelsSwitcher(self)

        self.panel_one = HomePanel(self, panels_switcher) 
        self.panel_two = InsertionPanel(self, panels_switcher)   

        panels_switcher.show("home_panel")


"""
First version of frontend for Windows
"""
if __name__ == "__main__":
    print("Starting the application")
    sleep(0.5)

    # Read config file
    configuration.app_config = configuration.read_config("config_file.ini")

    # Create a wx application
    app = wx.App()
    # Create the demo window
    win = MainFrame()
    # Show the window
    win.Show()
    # Start wx main loop
    app.MainLoop()
