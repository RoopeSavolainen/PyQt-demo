from PyQt5 import uic
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene
from PyQt5.QtCore import pyqtSlot, QTimer

from math import sin

from circle import Circle

timer = QTimer()
scene = None
running = False
circle = Circle()
phase = 0.0


# Listeners for button events

@pyqtSlot()
def start():
    global running
    running = True

@pyqtSlot()
def pause():
    global running
    running = False

@pyqtSlot()
def reset():
    global phase
    phase = 0.0


# Listener for timer event
@pyqtSlot()
def refresh():
    global phase
    if running:
        phase += 0.05

    # Update the circle coordinates
    x = sin(phase) * 100
    circle.setX(x)
    scene.invalidate()


# Creates a window and returns it
def create_gui():
    global timer
    global scene
    global circle

    # Load layout from a Qt Designer file
    window = uic.loadUi('window.ui')
    
    # Set up the QGraphicsView in the window
    window.canvas.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)
    scene = QGraphicsScene()
    scene.addItem(circle)
    window.canvas.setScene(scene)

    # Set up a timer to update the QGraphicsView 60Hz
    timer.setInterval(1000/60)
    timer.timeout.connect(refresh)
    timer.start()

    # Set up the button listeners
    window.start_btn.clicked.connect(start)
    window.pause_btn.clicked.connect(pause)
    window.reset_btn.clicked.connect(reset)

    return window


