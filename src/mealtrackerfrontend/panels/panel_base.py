import wx

class BasePanel(wx.Panel):
    def __init__(self, parent, switcher, name):
        # Initialize the base class
        wx.Panel.__init__(self, parent=parent)

        # Add himself to the switcher
        self.switcher = switcher
        self.switcher.add_panel(self, name)

        # Create a vertical layout
        self.sizer = wx.BoxSizer(orient=wx.VERTICAL)
        self.SetSizer(self.sizer)