from ..baseView import baseView

class skillsView(baseView):
    def __init__(self, returnFormat, data = {}):
        super().__init__(returnFormat, data)
        self.template = 'skills/index.html'
