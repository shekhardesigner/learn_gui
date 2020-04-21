import wx

class HelloWorld(wx.Frame):
    def __init__(self, parent, title):
        super(HelloWorld, self).__init__(parent, title=title)

        menuBar = wx.MenuBar()
        fileMenu = wx.Menu()

        fileMenu.Append(wx.ID_ABOUT, "About Us", "About App and Developers")
        fileMenu.Append(wx.ID_NEW, "&New", "Create New File")
        fileMenu.Append(wx.ID_OPEN, "&Open", "Open New File")
        fileMenu.AppendSeparator()

        quitMenuItem = fileMenu.Append(wx.ID_EXIT, "Quit", "Quit This Now!!")

        menuBar.Append(fileMenu, "&File")
        self.Bind(wx.EVT_MENU, self.handleMenuClick)

        """ Create App  """
        self.SetMenuBar(menuBar)
        self.widgets()
        self.SetSize(900, 600)
        self.Center()
        self.CreateStatusBar()
        self.Show()
    
    def handleMenuClick(self, event):
        id = event.GetId()

        if id == wx.ID_ABOUT:
            self.SetStatusText('About us set to status bar')

        if id == wx.ID_EXIT:        
            self.Close()

    def widgets(self):
        textbox = wx.BoxSizer(wx.VERTICAL)
        self.textbox = wx.TextCtrl(self, style=wx.TE_LEFT)
        textbox.Add(self.textbox, flag=wx.EXPAND | wx.TOP | wx.BOTTOM, border=5)
        
        grid = wx.GridSizer(5,5,100,10)
        textbox.Add(grid, proportion=2, flag=wx.EXPAND)

        self.SetSizer(textbox)    

def Main():
    app = wx.App()
    HelloWorld(None, title="Hello wxPython")
    app.MainLoop()

Main()