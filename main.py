import wx

class MainPanel(wx.Panel):
    def __init__(self, parent):
        pass

class MainFrame(wx.Frame):

    def __init__(self):
        super().__init__(None, title='Be Debt Free')
        self.Show()


if __name__ == '__main__':
    app = wx.App(redirect=False)
    frame = MainFrame()
    app.MainLoop()


