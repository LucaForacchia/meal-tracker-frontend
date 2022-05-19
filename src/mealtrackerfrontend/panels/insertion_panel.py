import wx
import wx._adv
import datetime

from .panel_base import BasePanel
from .confirmation_dialog import ConfirmationDialog

class InsertionPanel(BasePanel):
    def __init__(self, parent, switcher):
        # Initialize the base class
        super().__init__(parent, switcher, "insertion_panel")

        # DATE SELECTION
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        self.datepicker = wx._adv.DatePickerCtrl(self, style=wx._adv.DP_DROPDOWN)
        hbox1.Add(self.datepicker, 1, wx.ALL|wx.SHAPED|wx.ALIGN_LEFT, border = 10)
        # CHECKBOX START WEEK
        self.week_start = wx.CheckBox(self, label='Week start')
        hbox1.Add(self.week_start, 1, wx.ALL|wx.ALIGN_LEFT, border = 10)
        hbox1.Add((1,1), 1, wx.EXPAND)
        self.sizer.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)


        # MEAL TYPE
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        vbox1 = wx.BoxSizer(wx.VERTICAL)
        meal_type_label = wx.StaticText(self, label = "Meal type", style = wx.ALIGN_CENTRE) 
        vbox1.Add(meal_type_label, 0 ,wx.EXPAND) 
        self.meal_type = wx.ComboBox(self, choices = ["Pranzo", "Cena"]) 
        vbox1.Add(self.meal_type, 1, wx.ALL|wx.SHAPED|wx.EXPAND, border = 5)
        hbox2.Add(vbox1, flag = wx.ALL|wx.EXPAND, border = 10)

        # WHO
        vbox2 = wx.BoxSizer(wx.VERTICAL)
        participants_label = wx.StaticText(self, label = "Partecipanti", style = wx.ALIGN_CENTRE) 
        vbox2.Add(participants_label, 0 ,wx.EXPAND) 
        self.participants = wx.ComboBox(self, choices = ["Entrambi", "Luca", "Gioi"], value = "Entrambi") 
        vbox2.Add(self.participants, 1, wx.ALL|wx.SHAPED|wx.EXPAND, border = 5) 
        hbox2.Add(vbox2, flag = wx.ALL|wx.EXPAND, border = 10)
        
        self.sizer.Add(hbox2, flag = wx.ALL|wx.EXPAND, border = 10)

        # Meal
        self.meal = None
        meal_label = wx.StaticText(self, label = "Pasto", style = wx.ALIGN_CENTRE) 
        self.sizer.Add(meal_label, 0 ,wx.EXPAND|wx.ALL, 5) 
        self.meal_txt = wx.TextCtrl(self)
        self.sizer.Add(self.meal_txt, 1, wx.EXPAND)


        # NOTES      
        self.notes = None
        txt = wx.StaticText(self, label = "Notes", style = wx.ALIGN_CENTRE) 
        self.sizer.Add(txt, 0 ,wx.EXPAND|wx.ALL, 5) 
        self.notes_txt = wx.TextCtrl(self)
        # self.meal_txt.Bind(wx.EVT_TEXT, self.OnTextInserted)
        self.sizer.Add(self.notes_txt, 1, wx.EXPAND)      


        # BUTTONS
        button_box = wx.BoxSizer(wx.HORIZONTAL)
        back_button = wx.Button(self, label="back")
        back_button.Bind(wx.EVT_BUTTON, self.OnBack)


        button = wx.Button(self, label="insert")
        button.Bind(wx.EVT_BUTTON, self.OnEnterPressed)

        button_box.Add(back_button, 1, wx.ALL|wx.SHAPED|wx.ALIGN_LEFT, border = 10)
        button_box.Add((1,1), 1, wx.EXPAND)
        button_box.Add(button, 1, wx.ALL|wx.SHAPED, border = 10)
        
        # Add space above the button
        self.sizer.Add((1, 1), 1, wx.EXPAND)
        # Add the button at the middle
        self.sizer.Add(button_box, 0, wx.ALIGN_CENTER)
        # Add space below the button
        self.sizer.Add((1, 1), 1, wx.EXPAND)

    def OnBack(self, event):
        self.switcher.show("home_panel")

    def OnEnterPressed(self, event):
        # SHOULD OPEN A DIALOG SHOWING THE INSERTION AND REQUIRING FOR CONFIRMATION
        dt = self.datepicker.GetValue()
        date_meal = datetime.date(dt.GetYear(), dt.GetMonth()+1, dt.GetDay()).isoformat()
        start_week = bool(self.week_start.GetValue())
        meal = self.meal_txt.GetValue()
        meal_type = self.meal_type.GetValue()
        participants = self.participants.GetValue()
        notes = self.notes_txt.GetValue()       

        if participants not in ["Entrambi", "Luca", "Gioi"]:
            wx.MessageBox('Invalid participants %s!' % (participants), 'Error', wx.OK | wx.ICON_ERROR)
            return

        if meal_type not in ["Pranzo", "Cena"]:
            wx.MessageBox('Choose a meal type to insert a meal!', 'Error', wx.OK | wx.ICON_ERROR)
            return

        dial = ConfirmationDialog(self, date = date_meal, start_week = start_week, meal_type = meal_type, participants = participants, meal = meal, notes = notes)
        dial.ShowModal()



