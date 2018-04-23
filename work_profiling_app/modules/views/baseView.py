from flask import jsonify
from flask import render_template

class baseView(object):
    def __init__(self, returnFormat, data = {}):
        self.VERSION = 'v0.1.0'
        self.template = 'index.html'
        self.returnFormat = returnFormat
        self.data = data

    def render(self):
        if self.returnFormat == 'json':
            return jsonify(self.data)
        else:
            return render_template(self.template, version=self.VERSION, **self.data)