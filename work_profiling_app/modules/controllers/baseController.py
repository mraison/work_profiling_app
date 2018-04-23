from ..views.baseView import baseView


class baseController(object):
    def __init__(self, appSession):
        self.appSession = appSession

    def index(self):
        view = baseView(self.appSession['returnFormat'])
        return view.render()