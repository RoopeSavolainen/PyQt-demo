from PyQt5.QtCore import QPointF, QRectF, Qt
from PyQt5.QtWidgets import QGraphicsItem
from PyQt5.QtGui import QColor, QPainter

class Circle(QGraphicsItem):

    def __init__(self, radius=10, color=Qt.white):
        # Initialize parent class
        super().__init__()

        self.radius = radius
        self.color = color


    # paint() and boundingRect() are needed for all QGraphicsItems

    # paint() is called every time the QGraphicsScene containing the QGraphicsItem is refreshed
    def paint(self, painter, options, widget):
        painter.setBrush(self.color)
        painter.setPen(Qt.black)
        painter.setRenderHint(QPainter.Antialiasing)
        rect = self.boundingRect()
        painter.drawEllipse(rect)

    def boundingRect(self):
        return QRectF(-self.radius, -self.radius, 2*self.radius, 2*self.radius)

    # Toggle circle fill color when it's clicked
    def mousePressEvent(self, evt):
        if self.color == Qt.white:
            self.color = Qt.red
        else:
            self.color = Qt.white
