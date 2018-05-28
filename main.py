#!/bin/env python3

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from textarea import TextArea

def main():
    window = Gtk.Window(title="Hello")

    widget = TextArea()
    window.add(widget)

    window.connect("destroy", Gtk.main_quit)
    window.show_all()
    Gtk.main()

if __name__ == "__main__":
    main()
