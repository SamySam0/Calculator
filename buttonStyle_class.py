from tkinter import *

class NumButton(Button):

    def __init__(self, *args, **kwargs):
        Button.__init__(self, *args, **kwargs)
        self['bg'] = '#414141'
        self['fg'] = "white"
        self['height'] = 3
        self['width'] = 7
        self['relief'] = FLAT
        self['activebackground'] = "#616161"

class TopButton(Button):

    def __init__(self, *args, **kwargs):
        Button.__init__(self, *args, **kwargs)
        self['bg'] = 'lightgrey'
        self['fg'] = "#4C4C4C"
        self['height'] = 3
        self['width'] = 7
        self['relief'] = FLAT
        self['activebackground'] = "#eaeaea"

class SideButton(Button):

    def __init__(self, *args, **kwargs):
        Button.__init__(self, *args, **kwargs)
        self['bg'] = 'orange'
        self['fg'] = "white"
        self['height'] = 3
        self['width'] = 7
        self['relief'] = FLAT
        self['activebackground'] = "#ffac43"