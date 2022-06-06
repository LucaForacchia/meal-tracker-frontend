import wx

from utils.server_requests import ServerRequest

class ConfirmationDialog(wx.Dialog):

    def __init__(self, *args, **kwargs):
        super(ConfirmationDialog, self).__init__(*args)
        
        self.meal_info = kwargs
        self.date = kwargs["date"]
        self.start_week = kwargs["start_week"]
        self.meal_type = kwargs["meal_type"]
        self.participants = kwargs["participants"]
        self.meal = kwargs["meal"]
        self.notes = kwargs["notes"]

        self.InitUI()

        self.SetSize((500, 500))
        self.SetTitle("Confirm Insertion")

    def InitUI(self):
        vbox = wx.BoxSizer(wx.VERTICAL)

        text_showed = '''
        date: %s (start_week: %s)
        %s, %s 
        meal: %s
        %s
        
        Proceed with the insertion?
        ''' % (str(self.date), str(self.start_week), self.meal_type, self.participants, str(self.meal), self.notes)

        txt = wx.StaticText(self, label = text_showed, style = wx.ALIGN_CENTRE) 

        vbox.Add(txt, proportion = 1, flag=wx.ALL|wx.EXPAND, border=5)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        okButton = wx.Button(self, id=wx.ID_OK, label='Ok')
        closeButton = wx.Button(self, id=wx.ID_CANCEL, label='Close')
        hbox2.Add(closeButton, flag=wx.RIGHT, border=5)
        hbox2.Add((1,1), 1, flag=wx.EXPAND)
        hbox2.Add(okButton, flag=wx.LEFT, border=5)
        vbox.Add(hbox2, flag=wx.ALIGN_CENTER|wx.TOP|wx.BOTTOM, border=10)

        self.SetSizer(vbox)

        okButton.Bind(wx.EVT_BUTTON, self.OnInsert)
        closeButton.Bind(wx.EVT_BUTTON, self.OnClose)


    def OnClose(self, e):
        self.Destroy()

    def OnInsert(self, event):
        print("Ho scelto di inserire il pasto. Faccio la chiamata a backend")
        # diventa un try/catch questo
        # chiama backend
        inserted = ServerRequest().insert_meal(self.meal_info)
        
        # Apre le modali di ok o di errore?
        if inserted:
            wx.MessageBox('Meal Inserted', 'Outcome', 
                wx.OK | wx.ICON_INFORMATION)
        else:
            error_message = "Not True!"
            wx.MessageBox('Error while inserting meal:\n%s' % (error_message), 'Outcome', wx.OK | wx.ICON_ERROR)
        
        self.Destroy()
        
