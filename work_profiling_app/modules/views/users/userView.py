from ..baseView import baseView

class usersView(baseView):
    def __init__(self, returnFormat, data = {}):
        super().__init__(returnFormat, data)
        self.template = 'users/index.html'
