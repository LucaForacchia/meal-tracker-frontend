import wx

from .panel_base import BasePanel

class HomePanel(BasePanel):
    def __init__(self, parent, switcher):
        super().__init__(parent, switcher, "home_panel")
        
        self.sizer.AddStretchSpacer()

        ## BUTTON 1
        # Create the button
        self.button = wx.Button(self, label="Insert")
        # Bind the button to the given callback
        self.button.Bind(wx.EVT_BUTTON, self.on_click_change_1)
        ## Add(window, proportion, flag(or set of flags), border(only if flag set))
        self.sizer.Add(self.button, 0, wx.ALL|wx.ALIGN_CENTER, border = 10)
        # Add space below the button
        self.sizer.Add((1, 1), 1, wx.EXPAND)

        ## BUTTON 2
        self.button_two = wx.Button(self, label="move to 3")
        self.button_two.Bind(wx.EVT_BUTTON, self.on_click_change_2)
        self.sizer.Add(self.button_two, 0, wx.ALL|wx.ALIGN_CENTER, border = 10)
        self.sizer.Add((1, 1), 1, wx.EXPAND)

        ## BUTTON 3
        self.button_two = wx.Button(self, label="grid")
        self.button_two.Bind(wx.EVT_BUTTON, self.go_grid)
        self.sizer.Add(self.button_two, 0, wx.ALL|wx.ALIGN_CENTER, border = 10)
        self.sizer.Add((1, 1), 1, wx.EXPAND)


    def on_click_change_1(self, event):
        self.switcher.show("insertion_panel")

    def on_click_change_2(self, event):
        # icon =  wx.Icon("./MealTracker/Smile_Image.png")
        wx.MessageBox("Still nothing to show!", 'Error', wx.OK | wx.ICON_ERROR)

# self.switcher.show("panel_win")


    def go_grid(self, event):
        self.switcher.show("panel_grid")