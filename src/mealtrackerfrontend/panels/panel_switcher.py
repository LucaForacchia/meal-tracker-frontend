import wx

# PanelsSwitcher is a type of BoxSizer which allows
# switching between panels
class PanelsSwitcher(wx.BoxSizer):
    # The constructor a parent window
    # and a list of panels for switch between them
    def __init__(self, parent):
        # Initialize the base class
        wx.BoxSizer.__init__(self)
        # Attach this sizer to the parent window
        parent.SetSizer(self)
        # Save the parent windows
        self.parent = parent
        self.panels = {}

    def add_panel(self, panel, panel_name):
        # CATCH EVENTUAL panel double insertion
        self.panels[panel_name] = panel
        self.Add(panel, 1, wx.EXPAND)
        panel.Hide()
            
   # Show one panel and hide the rest
    def show(self, panel_name):
        # Check the required panel is in the list, throw error otherwise
        panel_name_list = list(self.panels.keys())
        if panel_name not in panel_name_list:
            wx.MessageBox("Still nothing to show!", 'Error', wx.OK | wx.ICON_ERROR)

            raise MissingPanel("Required panel not known by the switcher")

        # For each panel in the list of panels, hide it
        for panel in panel_name_list:
            self.panels[panel].Hide()

        # Then show the given panel
        self.panels[panel_name].Show()
            
        # Rearrange the window
        self.parent.Layout()

class MissingPanel(KeyError):
    pass