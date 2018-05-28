import gi
gi.require_version("Gtk", "3.0")
gi.require_version("PangoCairo", "1.0")
from gi.repository import Gtk, GObject, PangoCairo

import datetime

class TextArea(Gtk.DrawingArea):

    def __init__(self):
        self.repeat_period_msec = 1000

        Gtk.DrawingArea.__init__(self)
        self.context = None

        #create a pango layout. Leave text argument to be empty string since we want to use markup
        self.pango_context = self.create_pango_context()
        self.pango_layout = self.create_pango_layout('')

        #Use pango markup to set the text within the pango layout
        self.pango_layout.set_markup('<span foreground=\"blue\">This is some sample markup</span> <sup>text</sup> that <u>is displayed with pango</u>')

        self.connect("draw", self.draw_cb)
        self.set_size_request(450, -1)
        self.repeatedly_update_time()

    # The draw_cb is called when the widget is asked to draw itself
    # with the 'draw' as opposed to old function 'expose event' 
    def draw_cb(self, widget, event):
        #create a CAIRO context (to use with pango)
        self.context = widget.get_window().cairo_create()

        #Show the pango_layout in the Cairo context just created.
        PangoCairo.show_layout(self.context, self.pango_layout)

    #This method calls itself every 1 second and updates the time displayed.
    def repeatedly_update_time(self):
        pass
        #now = datetime.datetime.now()
        #self.pango_layout.set_markup("<u>Current time:</u> " + str(now))
        #self.queue_draw()
        #GObject.timeout_add(self.repeat_period_msec, self.repeatedly_update_time)
