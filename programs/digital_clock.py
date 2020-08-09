"""
Digital clock program made by using the tkinter library.

Displays a digital clock when run.
"""

from time import strftime  # String formats time
from tkinter import Label, Tk, mainloop


def helloworld(object):
    """
    Print a line
    args:
        object (str): name of the object
    returns:
        None
    """
    if type(object) != str:
        raise TypeError

    print("I am a {}.".format(object))


def label_config(root):
    """
    Label configuration.

    Args:
        root (TK object instance) : Toplevel widget of Tk which represents
        mostly the main window of an application.

    Returns:
        clock_label (Label object instance) : Label widget which can display
        text and bitmaps. Configures the font, and background and foreground
        colors of root.
    """
    clock_label = Label(
        root, font=("Calibri", 40, "bold"), background="#186C8F", foreground="#F3A548"
    )
    clock_label.pack(anchor="center")

    return clock_label


def root_config():
    """Create and configure a top level window.

    Args:
        None

    Returns:
        root (TK object instance) : Toplevel widget of Tk which represents
        mostly the main window of an application. It has an associated Tcl
        interpreter.
    """

    # Create top level window
    root = Tk()

    # Window title
    root.title("Digital Clock")

    return root


def time():
    """
    Function to set the time label.

    Args:
        None

    Returns:
        None
    """
    # Set the time format
    time_string = strftime("%H:%M:%S")

    # Set the date format
    date_string = strftime("%B  %d  %Y")

    # Create concatenated string
    display_string = time_string + "\n" + date_string

    # Configure label
    label.config(text=display_string)
    label.after(1000, time)


root = root_config()
label = label_config(root)
time()
mainloop()
