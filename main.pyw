from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
from math import *
from mpmath import *

global lang
lang = "English"

class mainshape:
    shape = "Area - Square"

def is_number(s):
    try:
        float(s)  # Try converting the input to a float
        return True
    except ValueError:
        return False

class _2D:
    def square(sl):
        return float(sl) ** 2
    def rectangle(l, w):
        return float(l) * float(w)
    def circle(r):
        return pi*(float(r) ** 2)
    def isosceles_triangle(b, h):
        return (1/2) * float(b) * float(h)
    def scalene_triangle(a, b, c):
        float(a)
        float(b)
        float(c)
        s = (a + b + c) / 2
        sa = s - a
        sb = s - b
        sc = s - c
        return sqrt(s * sa * sb * sc)
    def equilateral_triangle(sl):
        return ((sqrt(3)) / 4) * (float(sl) ** 2)
    def pentagon(sl):
        n = 5
        return (n * (float(sl) ** 2)) / (4 * tan(pi/n))
    def hexagon(sl):
        n = 6
        return (n * (float(sl) ** 2)) / (4 * tan(pi/n))
    def heptagon(sl):
        n = 7
        return (n * (float(sl) ** 2)) / (4 * tan(pi/n))
    def octagon(sl):
        n = 8
        return (n * (float(sl) ** 2)) / (4 * tan(pi/n))
    def nonagon(sl):
        n = 9
        return (n * (float(sl) ** 2)) / (4 * tan(pi/n))
    def decagon(sl):
        n = 10
        return (n * (float(sl) ** 2)) / (4 * tan(pi/n))
    def undecagon(sl):
        n = 11
        return (n * (float(sl) ** 2)) / (4 * tan(pi/n))
    def dodecagon(sl):
        n = 12
        return (n * (float(sl) ** 2)) / (4 * tan(pi/n))
    def tridecagon(sl):
        n = 13
        return (n * (float(sl) ** 2)) / (4 * tan(pi/n))
    def tetradecagon(sl):
        n = 14
        return (n * (float(sl) ** 2)) / (4 * tan(pi/n))
    def pentadecagon(sl):
        n = 15
        return (n * (float(sl) ** 2)) / (4 * tan(pi/n))
    def trapezoid(a, b, h):
        return (1 / 2) * (float(a) + float(b)) * float(h)
    def ellipse(a, b):
        return (pi * float(a) * float(b))
    def polyomino(nos, ssl):
        return float(nos) * (float(ssl) ** 2)
    def star(nop, sl):
        return (1 / 4) * float(nop) * (float(sl) ** 2) * cot(pi / float(nop))
    def semicircle(r):
        return (pi * (float(r)) ** 2) / 2
    def squircle(bcttc, rr):
        return (_2D.square(float(bcttc)) - (_2D.square(float(rr)) * 4)) + _2D.circle(float(rr))
    def parallelogram(l, w):
        return float(l) * float(w)
    def annulus(ic, oc):
        return _2D.circle(float(oc)) - _2D.circle(float(ic))
    def kite(d1, d2):
        return (1 / 2) * (float(d1) * float(d2))
    def rhombus(d):
        return (1 / 2) * (float(d) ** 2)
class _3D:
    def tribonacci_constant():
        inner_term = 19 + 3 * sqrt(33)
        first_cube_root = inner_term ** (1/3)
        second_cube_root = (19 - 3 * sqrt(33)) ** (1/3)
        tribonacci_const = (1 + first_cube_root + second_cube_root) / 3
        return tribonacci_const
    tc = tribonacci_constant()
    def cube(el):
        return float(el) ** 3
    def rectangular_prism(l, w, h):
        return float(l) * float(w) * float(h)
    def sphere(r):
        return (4/3) * pi * (float(r) ** 3)
    def cylinder(r, h):
        return _2D.circle(float(r)) * float(h)
    def cone(r, h):
        return (1 / 3) * _2D.circle(float(r)) * float(h)
    def dodecahedron(el):
        return ((15 + 7 * sqrt(5)) / 4) * (float(el) ** 3)
    def isosceles_triangular_prism(bb, w, h):
        return _2D.isosceles_triangle(float(bb), float(w)) * float(h)
    def scalene_triangular_prism(ba, bb, bc, h):
        return _2D.scalene_triangle(float(ba), float(bb), float(bc)) * float(h)
    def equlateral_triangular_prism(bel, h):
        return _2D.equilateral_triangle(float(bel)) * float(h)
    def hemisphere(r):
        return _3D.sphere(float(r)) / 2
    def torus(R, r):
        return 2 * (pi ** 2) * (float(r) ** 2) * float(R)
    def rhombicosidodecahedron(el):
        return ((60 + 29 * sqrt(5)) / 3) * (float(el) ** 3)
    def snub_cube(el):
        return (float(el) ** 3) * ((8 * _3D.tc + 6) / (3 * sqrt(2 * ((_3D.tc ** 2) - 3))))
    def capsule(lwre, r):
        return _3D.cylinder(float(r), float(lwre)) + _3D.sphere(float(r))
    def tetrahedron(el):
        return(float(el) ** 3) / (6 * sqrt(2))
    def octahedron(el):
        return ((float(el) ** 3) * sqrt(2)) / 3
    def icosahedron(el):
        return (5 / 12) * (3 + sqrt(5)) * (float(el) ** 3)
    def isosceles_triangular_pyramid(bb, w, h):
        return (1 / 3) * _2D.isosceles_triangle(float(bb), float(w)) * float(h)
    def scalene_triangular_pyramid(ba, bb, bc, h):
        return (1 / 3) * _2D.scalene_triangle(float(ba), float(bb), float(bc)) * float(h)
    def equilateral_triangular_pyramid(bel, h):
        return (1 / 3) * _2D.equilateral_triangle(float(bel)) * float(h)
    def square_pyramid(bel, h):
        return (1 / 3) * _2D.square(float(bel)) * float(h)
    def pentagon_pyramid(bel, h):
        return (1 / 3) * _2D.pentagon(float(bel)) * float(h)
    def hexagon_pyramid(bel, h):
        return (1 / 3) * _2D.hexagon(float(bel)) * float(h)
    def heptagon_pyramid(bel, h):
        return (1 / 3) * _2D.heptagon(float(bel)) * float(h)
    def octagon_pyramid(bel, h):
        return (1 / 3) * _2D.octagon(float(bel)) * float(h)
    def nonagon_pyramid(bel, h):
        return (1 / 3) * _2D.nonagon(float(bel)) * float(h)
    def decagon_pyramid(bel, h):
        return (1 / 3) * _2D.decagon(float(bel)) * float(h)
    def star_prism(bnop, bel, h):
        return _2D.star(float(bnop), float(bel)) * float(h)
    def isosceles_triangular_bipyramid(mpb, w, cta):
        return ((1 / 3) * _2D.isosceles_triangle(float(mpb), float(w)) * float(cta)) * 2
    def scalene_triangular_bipyramid(mpa, mpb, mpc, cta):
        return ((1 / 3) * _2D.scalene_triangle(float(mpa), float(mpb), float(mpc)) * float(cta)) * 2
    def equilateral_triangular_bipyramid(mpel, cta):
        return ((1 / 3) * _2D.equilateral_triangle(float(mpel)) * float(cta)) * 2 

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(360, 640)
        MainWindow.setMinimumSize(QSize(360, 640))
        MainWindow.setMaximumSize(QSize(360, 640))
        icon = QIcon()
        icon.addFile(u"./assets/images/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setDocumentMode(False)
        self.actionSolve = QAction(MainWindow)
        self.actionSolve.setObjectName(u"actionSolve")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(0, 0, 361, 21))
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.title.setFont(font)
        self.title.setScaledContents(True)
        self.title.setAlignment(Qt.AlignCenter)
        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(0, 40, 361, 61))
        font1 = QFont()
        font1.setPointSize(12)
        self.comboBox_2.setFont(font1)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(-10, 100, 391, 20))
        self.line_2.setLineWidth(5)
        self.line_2.setMidLineWidth(1)
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(-20, 20, 391, 20))
        self.line_3.setLineWidth(5)
        self.line_3.setMidLineWidth(1)
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(-10, 160, 391, 20))
        self.line_4.setLineWidth(5)
        self.line_4.setMidLineWidth(1)
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.comboBox_3 = QComboBox(self.centralwidget)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(0, 181, 361, 21))
        font2 = QFont()
        font2.setPointSize(10)
        self.comboBox_3.setFont(font2)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(-1, 200, 362, 41))
        font3 = QFont()
        font3.setPointSize(15)
        self.pushButton_2.setFont(font3)
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(0, 530, 180, 110))
        self.graphicsView_2 = QGraphicsView(self.centralwidget)
        self.graphicsView_2.setObjectName(u"graphicsView_2")
        self.graphicsView_2.setGeometry(QRect(180, 530, 190, 110))
        self.line_5 = QFrame(self.centralwidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(170, 480, 20, 161))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Active, QPalette.Light, brush)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 128))
        brush1.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.line_5.setPalette(palette)
        self.line_5.setLineWidth(3)
        self.line_5.setMidLineWidth(1)
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.line_6 = QFrame(self.centralwidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(-20, 470, 400, 20))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush)
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush)
        palette1.setBrush(QPalette.Active, QPalette.Mid, brush)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Mid, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Mid, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.line_6.setPalette(palette1)
        self.line_6.setLineWidth(3)
        self.line_6.setMidLineWidth(1)
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)
        self.line_7 = QFrame(self.centralwidget)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setGeometry(QRect(-20, 510, 400, 30))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Light, brush)
        palette2.setBrush(QPalette.Active, QPalette.Dark, brush)
        palette2.setBrush(QPalette.Active, QPalette.Mid, brush)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Dark, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Mid, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Dark, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Mid, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.line_7.setPalette(palette2)
        self.line_7.setLineWidth(3)
        self.line_7.setMidLineWidth(1)
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 490, 180, 30))
        self.label.setFont(font3)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(180, 490, 180, 30))
        self.label_2.setFont(font3)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.answer = QLabel(self.centralwidget)
        self.answer.setObjectName(u"answer")
        self.answer.setGeometry(QRect(0, 260, 361, 41))
        font4 = QFont()
        font4.setPointSize(10)
        self.answer.setFont(font4)
        self.answer.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.Input1 = QPlainTextEdit(self.centralwidget)
        self.Input1.setObjectName(u"Input1")
        self.Input1.setGeometry(QRect(0, 130, 90, 31))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.Input1.setSizePolicy(sizePolicy)
        self.Input1.setInputMethodHints(Qt.ImhDialableCharactersOnly|Qt.ImhDigitsOnly|Qt.ImhPreferNumbers)
        self.Input2 = QPlainTextEdit(self.centralwidget)
        self.Input2.setObjectName(u"Input2")
        self.Input2.setGeometry(QRect(90, 130, 90, 31))
        sizePolicy.setHeightForWidth(self.Input2.sizePolicy().hasHeightForWidth())
        self.Input2.setSizePolicy(sizePolicy)
        self.Input2.setInputMethodHints(Qt.ImhDialableCharactersOnly|Qt.ImhDigitsOnly|Qt.ImhPreferNumbers)
        self.Input3 = QPlainTextEdit(self.centralwidget)
        self.Input3.setObjectName(u"Input3")
        self.Input3.setGeometry(QRect(180, 130, 90, 31))
        sizePolicy.setHeightForWidth(self.Input3.sizePolicy().hasHeightForWidth())
        self.Input3.setSizePolicy(sizePolicy)
        self.Input3.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.Input3.setInputMethodHints(Qt.ImhDialableCharactersOnly|Qt.ImhDigitsOnly|Qt.ImhPreferNumbers)
        self.Input3.setReadOnly(True)
        self.Input3Label = QLabel(self.centralwidget)
        self.Input3Label.setObjectName(u"Input3Label")
        self.Input3Label.setGeometry(QRect(180, 110, 91, 20))
        self.Input3Label.setAlignment(Qt.AlignCenter)
        self.Input2Label = QLabel(self.centralwidget)
        self.Input2Label.setObjectName(u"Input2Label")
        self.Input2Label.setGeometry(QRect(90, 110, 91, 20))
        self.Input2Label.setAlignment(Qt.AlignCenter)
        self.Input1Label = QLabel(self.centralwidget)
        self.Input1Label.setObjectName(u"Input1Label")
        self.Input1Label.setGeometry(QRect(0, 110, 91, 20))
        self.Input1Label.setAlignment(Qt.AlignCenter)
        self.Input4 = QPlainTextEdit(self.centralwidget)
        self.Input4.setObjectName(u"Input4")
        self.Input4.setGeometry(QRect(270, 130, 90, 31))
        sizePolicy.setHeightForWidth(self.Input4.sizePolicy().hasHeightForWidth())
        self.Input4.setSizePolicy(sizePolicy)
        self.Input4.setInputMethodHints(Qt.ImhDialableCharactersOnly|Qt.ImhDigitsOnly|Qt.ImhPreferNumbers)
        self.Input4Label = QLabel(self.centralwidget)
        self.Input4Label.setObjectName(u"Input4Label")
        self.Input4Label.setGeometry(QRect(270, 110, 91, 20))
        self.Input4Label.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Area and Volume Calculator", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"Area and Volume Calculator", None))

        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Area - Square", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Area - Rectangle", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Area - Circle", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"Area - Isosceles triangle", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"Area - Scalene triangle", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("MainWindow", u"Area - Equilateral triangle", None))
        self.comboBox_2.setItemText(6, QCoreApplication.translate("MainWindow", u"Area - Pentagon", None))
        self.comboBox_2.setItemText(7, QCoreApplication.translate("MainWindow", u"Area - Hexagon", None))
        self.comboBox_2.setItemText(8, QCoreApplication.translate("MainWindow", u"Area - Heptagon", None))
        self.comboBox_2.setItemText(9, QCoreApplication.translate("MainWindow", u"Area - Octagon", None))
        self.comboBox_2.setItemText(10, QCoreApplication.translate("MainWindow", u"Area - Nonagon", None))
        self.comboBox_2.setItemText(11, QCoreApplication.translate("MainWindow", u"Area - Decagon", None))
        self.comboBox_2.setItemText(12, QCoreApplication.translate("MainWindow", u"Area - Undecagon", None))
        self.comboBox_2.setItemText(13, QCoreApplication.translate("MainWindow", u"Area - Dodecagon", None))
        self.comboBox_2.setItemText(14, QCoreApplication.translate("MainWindow", u"Area - Tridecagon", None))
        self.comboBox_2.setItemText(15, QCoreApplication.translate("MainWindow", u"Area - Tetradecagon", None))
        self.comboBox_2.setItemText(16, QCoreApplication.translate("MainWindow", u"Area - Pentadecagon", None))
        self.comboBox_2.setItemText(17, QCoreApplication.translate("MainWindow", u"Area - Trapezoid", None))
        self.comboBox_2.setItemText(18, QCoreApplication.translate("MainWindow", u"Area - Ellipse", None))
        self.comboBox_2.setItemText(19, QCoreApplication.translate("MainWindow", u"Area - Polyomino", None))
        self.comboBox_2.setItemText(20, QCoreApplication.translate("MainWindow", u"Area - Star", None))
        self.comboBox_2.setItemText(21, QCoreApplication.translate("MainWindow", u"Area - Semicircle", None))
        self.comboBox_2.setItemText(22, QCoreApplication.translate("MainWindow", u"Area - Squircle", None))
        self.comboBox_2.setItemText(23, QCoreApplication.translate("MainWindow", u"Area - Parallelogram", None))
        self.comboBox_2.setItemText(24, QCoreApplication.translate("MainWindow", u"Area - Annulus", None))
        self.comboBox_2.setItemText(25, QCoreApplication.translate("MainWindow", u"Area - Kite", None))
        self.comboBox_2.setItemText(26, QCoreApplication.translate("MainWindow", u"Area - Rhombus", None))
        self.comboBox_2.setItemText(27, QCoreApplication.translate("MainWindow", u"Volume - Cube", None))
        self.comboBox_2.setItemText(28, QCoreApplication.translate("MainWindow", u"Volume - Rectangular prism", None))
        self.comboBox_2.setItemText(29, QCoreApplication.translate("MainWindow", u"Volume - Sphere", None))
        self.comboBox_2.setItemText(30, QCoreApplication.translate("MainWindow", u"Volume - Cylinder", None))
        self.comboBox_2.setItemText(31, QCoreApplication.translate("MainWindow", u"Volume - Cone", None))
        self.comboBox_2.setItemText(32, QCoreApplication.translate("MainWindow", u"Volume - Dodecahedron", None))
        self.comboBox_2.setItemText(33, QCoreApplication.translate("MainWindow", u"Volume - Isosceles triangular prism", None))
        self.comboBox_2.setItemText(34, QCoreApplication.translate("MainWindow", u"Volume - Scalene triangular prism", None))
        self.comboBox_2.setItemText(35, QCoreApplication.translate("MainWindow", u"Volume - Equilateral triangular prism", None))
        self.comboBox_2.setItemText(36, QCoreApplication.translate("MainWindow", u"Volume - Hemisphere", None))
        self.comboBox_2.setItemText(37, QCoreApplication.translate("MainWindow", u"Volume - Torus", None))
        self.comboBox_2.setItemText(38, QCoreApplication.translate("MainWindow", u"Volume - Rhombicosidodecahedron", None))
        self.comboBox_2.setItemText(39, QCoreApplication.translate("MainWindow", u"Volume - Snub cube", None))
        self.comboBox_2.setItemText(40, QCoreApplication.translate("MainWindow", u"Volume - Capsule", None))
        self.comboBox_2.setItemText(41, QCoreApplication.translate("MainWindow", u"Volume - Tetrahedron", None))
        self.comboBox_2.setItemText(42, QCoreApplication.translate("MainWindow", u"Volume - Octahedron", None))
        self.comboBox_2.setItemText(43, QCoreApplication.translate("MainWindow", u"Volume - Icosahedron", None))
        self.comboBox_2.setItemText(44, QCoreApplication.translate("MainWindow", u"Volume - Isosceles triangular pyramid", None))
        self.comboBox_2.setItemText(45, QCoreApplication.translate("MainWindow", u"Volume - Scalene triangular pyramid", None))
        self.comboBox_2.setItemText(46, QCoreApplication.translate("MainWindow", u"Volume - Equilateral triangular pyramid", None))
        self.comboBox_2.setItemText(47, QCoreApplication.translate("MainWindow", u"Volume - Square pyramid", None))
        self.comboBox_2.setItemText(48, QCoreApplication.translate("MainWindow", u"Volume - Pentagonal pyramid", None))
        self.comboBox_2.setItemText(49, QCoreApplication.translate("MainWindow", u"Volume - Hexagonal pyramid", None))
        self.comboBox_2.setItemText(50, QCoreApplication.translate("MainWindow", u"Volume - Heptagonal pyramid", None))
        self.comboBox_2.setItemText(51, QCoreApplication.translate("MainWindow", u"Volume - Octagonal pyramid", None))
        self.comboBox_2.setItemText(52, QCoreApplication.translate("MainWindow", u"Volume - Nonagonal pyramid", None))
        self.comboBox_2.setItemText(53, QCoreApplication.translate("MainWindow", u"Volume - Decagonal pyramid", None))
        self.comboBox_2.setItemText(54, QCoreApplication.translate("MainWindow", u"Volume - Star prism", None))
        self.comboBox_2.setItemText(55, QCoreApplication.translate("MainWindow", u"Volume - Isosceles triangular bipyramid", None))
        self.comboBox_2.setItemText(56, QCoreApplication.translate("MainWindow", u"Volume - Scalene triangular bipyramid", None))
        self.comboBox_2.setItemText(57, QCoreApplication.translate("MainWindow", u"Volume - Equilateral triangular bipyramid", None))

        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"Inches", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"Feet", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"Yards", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("MainWindow", u"Miles", None))
        self.comboBox_3.setItemText(4, QCoreApplication.translate("MainWindow", u"Millimeters", None))
        self.comboBox_3.setItemText(5, QCoreApplication.translate("MainWindow", u"Centimeters", None))
        self.comboBox_3.setItemText(6, QCoreApplication.translate("MainWindow", u"Meters", None))
        self.comboBox_3.setItemText(7, QCoreApplication.translate("MainWindow", u"Kilometers", None))

        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Solve", ))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Shape:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Formula:", None))
        self.answer.setText(QCoreApplication.translate("MainWindow", u"Answer", None))
        self.Input3Label.setText(QCoreApplication.translate("MainWindow", u"Input3Label", None))
        self.Input4Label.setText(QCoreApplication.translate("MainWindow", u"Input4Label", None))
        self.Input2Label.setText(QCoreApplication.translate("MainWindow", u"Input2Label", None))
        self.Input1Label.setText(QCoreApplication.translate("MainWindow", u"Input1Label", None))




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  # Instantiate your existing UI class
        self.ui.setupUi(self)  # Setup your UI

        # Connect signals to slots here if needed
        self.ui.comboBox_3.currentTextChanged.connect(self.update_units)
        self.ui.comboBox_2.currentTextChanged.connect(self.update_shape)
        self.ui.pushButton_2.clicked.connect(self.solve)
        # Add any additional setup or functionality here

    def solve(self):
        if mainshape.shape in u"Area - Square":
            a = is_number(self.ui.Input1.text())
            if a == True:
                pass
            else:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Side length is not a valid number", None))
        elif mainshape.shape in u"Area - Rectangle":
            a = is_number(self.ui.Input1.text())
            b = is_number(self.ui.Input2.text())
            if a == True and b == True:
                pass
            elif a == False and b == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Length is not a valid number", None))
            elif a == True and b == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Width is not a valid number", None))
            elif a == False and b == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Length nor width is a valid number", None))
        elif mainshape.shape in u"Area - Circle":
            a = is_number(self.ui.Input2.text())
            if a == True:
                pass
            else:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Radius is not a valid number", None))
        elif mainshape.shape in u"Area - Isosceles triangle":
            a = is_number(self.ui.Input1.text())
            b = is_number(self.ui.Input2.text())
            if a == True and b == True:
                pass
            elif a == False and b == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length is not a valid number", None))
            elif a == True and b == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Height is not a valiv number", None))
            elif a == False and b == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length nor height is a valid number", None))
        elif mainshape.shape in u"Area - Scalene triangle":
            a = is_number(self.ui.Input1.text())
            b = is_number(self.ui.Input2.text())
            c = is_number(self.ui.Input3.text())
            if a == True and b == True and c == True:
                pass
            elif a == False and b == True and c == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length is not a valid number", None))
            elif a == True and b == False and c == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Height is not a valiv number", None))
            elif a == True and b == True and c == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length nor height is a valid number", None))
            elif a == False and b == False and c == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length nor height is a valid number", None))
            elif a == False and b == True and c == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length", None))
            elif a == True and b == False and c == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Height", None))
            elif a == False and b == False and c == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length nor height is a valid number", None))
        elif mainshape.shape in u"Area - Equilateral triangle":
            a = is_number(self.ui.Input1.text())
            if a == True:
                pass
            else:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Side length is not a valid number", None))
        elif mainshape.shape in u"Area - Pentagon":
            a = is_number(self.ui.Input1.text())
            if a == True:
                pass
            else:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Side length is not a valid number", None))
        elif mainshape.shape in u"Area - Hexagon":
            a = is_number(self.ui.Input1.text())
            if a == True:
                pass
            else:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Side length is not a valid number", None))
        elif mainshape.shape in u"Area - Heptagon":
            a = is_number(self.ui.Input1.text())
            if a == True:
                pass
            else:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Side length is not a valid number", None))
        elif mainshape.shape in u"Area - Octagon":
            a = is_number(self.ui.Input1.text())
            if a == True:
                pass
            else:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Side length is not a valid number", None))
        elif mainshape.shape in u"Area - Nonagon":
            a = is_number(self.ui.Input1.text())
            if a == True:
                pass
            else:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Side length is not a valid number", None))
        elif mainshape.shape in u"Area - Decagon":
            a = is_number(self.ui.Input1.text())
            if a == True:
                pass
            else:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Side length is not a valid number", None))
        elif mainshape.shape in u"Area - Undecagon":
            a = is_number(self.ui.Input1.text())
            if a == True:
                pass
            else:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Side length is not a valid number", None))
        elif mainshape.shape in u"Area - Dodecagon":
            a = is_number(self.ui.Input1.text())
            if a == True:
                pass
            else:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Side length is not a valid number", None))
        elif mainshape.shape in u"Area - Tridecagon":
            a = is_number(self.ui.Input1.text())
            if a == True:
                pass
            else:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Side length is not a valid number", None))
        elif mainshape.shape in u"Area - Tetradecagon":
            a = is_number(self.ui.Input1.text())
            if a == True:
                pass
            else:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Side length is not a valid number", None))
        elif mainshape.shape in u"Area - Pentadecagon":
            a = is_number(self.ui.Input1.text())
            if a == True:
                pass
            else:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Side length is not a valid number", None))
        elif mainshape.shape in u"Area - Trapezoid":
            a = is_number(self.ui.Input1.text())
            b = is_number(self.ui.Input2.text())
            c = is_number(self.ui.Input3.text())
            if a == True and b == True and c == True:
                pass
            elif a == False and b == True and c == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length is not a valid number", None))
            elif a == True and b == False and c == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Height is not a valiv number", None))
            elif a == True and b == True and c == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length nor height is a valid number", None))
            elif a == False and b == False and c == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length nor height is a valid number", None))
            elif a == False and b == True and c == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length", None))
            elif a == True and b == False and c == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Height", None))
            elif a == False and b == False and c == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length nor height is a valid number", None))
        elif mainshape.shape in u"Area - Ellipse":
            a = is_number(self.ui.Input1.text())
            b = is_number(self.ui.Input2.text())
            if a == True and b == True:
                pass
            elif a == False and b == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Length is not a valid number", None))
            elif a == True and b == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Width is not a valid number", None))
            elif a == False and b == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Length nor width is a valid number", None))
        elif mainshape.shape in u"Area - Polyomino":
            a = is_number(self.ui.Input1.text())
            b = is_number(self.ui.Input2.text())
            if a == True and b == True:
                pass
            elif a == False and b == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Length is not a valid number", None))
            elif a == True and b == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Width is not a valid number", None))
            elif a == False and b == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Length nor width is a valid number", None))
        elif mainshape.shape in u"Area - Star":
            a = is_number(self.ui.Input1.text())
            b = is_number(self.ui.Input2.text())
            if a == True and b == True:
                pass
            elif a == False and b == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Length is not a valid number", None))
            elif a == True and b == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Width is not a valid number", None))
            elif a == False and b == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Length nor width is a valid number", None))
        elif mainshape.shape in u"Area - Semicircle":
            a = is_number(self.ui.Input1.text())
            if a == True:
                pass
            else:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Side length is not a valid number", None))
        elif mainshape.shape in u"Area - Squircle":
            a = is_number(self.ui.Input1.text())
            b = is_number(self.ui.Input2.text())
            if a == True and b == True:
                pass
            elif a == False and b == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Length is not a valid number", None))
            elif a == True and b == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Width is not a valid number", None))
            elif a == False and b == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Length nor width is a valid number", None))
        elif mainshape.shape in u"Area - Parallelogram":
            a = is_number(self.ui.Input1.text())
            b = is_number(self.ui.Input2.text())
            if a == True and b == True:
                pass
            elif a == False and b == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Length is not a valid number", None))
            elif a == True and b == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Width is not a valid number", None))
            elif a == False and b == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Length nor width is a valid number", None))
        elif mainshape.shape in u"Area - Annulus":
            a = is_number(self.ui.Input1.text())
            b = is_number(self.ui.Input2.text())
            if a == True and b == True:
                pass
            elif a == False and b == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Length is not a valid number", None))
            elif a == True and b == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Width is not a valid number", None))
            elif a == False and b == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Length nor width is a valid number", None))
        elif mainshape.shape in u"Area - Kite":
            a = is_number(self.ui.Input1.text())
            b = is_number(self.ui.Input2.text())
            if a == True and b == True:
                pass
            elif a == False and b == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Length is not a valid number", None))
            elif a == True and b == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Width is not a valid number", None))
            elif a == False and b == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Length nor width is a valid number", None))
        elif mainshape.shape in u"Area - Rhombus":
            a = is_number(self.ui.Input1.text())
            b = is_number(self.ui.Input2.text())
            if a == True and b == True:
                pass
            elif a == False and b == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Length is not a valid number", None))
            elif a == True and b == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Width is not a valid number", None))
            elif a == False and b == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Length nor width is a valid number", None))
        elif mainshape.shape in u"Volume - Cube":
            a = is_number(self.ui.Input1.text())
            if a == True:
                pass
            else:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Side length is not a valid number", None))
        elif mainshape.shape in u"Volume - Rectangular prism":
            a = is_number(self.ui.Input1.text())
            b = is_number(self.ui.Input2.text())
            c = is_number(self.ui.Input3.text())
            if a == True and b == True and c == True:
                pass
            elif a == False and b == True and c == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length is not a valid number", None))
            elif a == True and b == False and c == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Height is not a valiv number", None))
            elif a == True and b == True and c == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length nor height is a valid number", None))
            elif a == False and b == False and c == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length nor height is a valid number", None))
            elif a == False and b == True and c == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length", None))
            elif a == True and b == False and c == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Height", None))
            elif a == False and b == False and c == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length nor height is a valid number", None))
        elif mainshape.shape in u"Volume - Sphere":
            a = is_number(self.ui.Input1.text())
            if a == True:
                pass
            else:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Side length is not a valid number", None))
        elif mainshape.shape in u"Volume - Cylinder":
            a = is_number(self.ui.Input1.text())
            b = is_number(self.ui.Input2.text())
            if a == True and b == True:
                pass
            elif a == False and b == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Length is not a valid number", None))
            elif a == True and b == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Width is not a valid number", None))
            elif a == False and b == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Length nor width is a valid number", None))
        elif mainshape.shape in u"Volume - Cone":
            a = is_number(self.ui.Input1.text())
            b = is_number(self.ui.Input2.text())
            if a == True and b == True:
                pass
            elif a == False and b == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Length is not a valid number", None))
            elif a == True and b == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Width is not a valid number", None))
            elif a == False and b == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Length nor width is a valid number", None))
        elif mainshape.shape in u"Volume - Dodecahedron":
            a = is_number(self.ui.Input1.text())
            if a == True:
                pass
            else:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Side length is not a valid number", None))
        elif mainshape.shape in u"Volume - Isosceles triangular prism":
            a = is_number(self.ui.Input1.text())
            b = is_number(self.ui.Input2.text())
            c = is_number(self.ui.Input3.text())
            if a == True and b == True and c == True:
                pass
            elif a == False and b == True and c == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length is not a valid number", None))
            elif a == True and b == False and c == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Height is not a valiv number", None))
            elif a == True and b == True and c == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length nor height is a valid number", None))
            elif a == False and b == False and c == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length nor height is a valid number", None))
            elif a == False and b == True and c == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length", None))
            elif a == True and b == False and c == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Height", None))
            elif a == False and b == False and c == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length nor height is a valid number", None))
        elif mainshape.shape in u"Volume - Scalene triangular prism":
            a = is_number(self.ui.Input1.text())
            b = is_number(self.ui.Input2.text())
            c = is_number(self.ui.Input3.text())
            d = is_number(self.ui.Input4.text())
            if a == True and b == True and c == True and d == True:
                pass
            elif a == False and b == True and c == True and d == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length is not a valid number", None))
            elif a == True and b == False and c == True and d == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Height is not a valiv number", None))
            elif a == True and b == True and c == False and d == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length nor height is a valid number", None))
            elif a == True and b == True and c == True and d == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length nor height is a valid number", None))
            elif a == False and b == False and c == True and d == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length nor height is a valid number", None))
            elif a == True and b == False and c == False and d == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length", None))
            elif a == True and b == True and c == False and d == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Height", None))
            elif a == False and b == True and c == False and d == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length nor height is a valid number", None))
            elif a == True and b == False and c == True and d == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length nor height is a valid number", None))
            elif a == False and b == False and c == False and d == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length nor height is a valid number", None))
            elif a == True and b == False and c == False and d == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length nor height is a valid number", None))
            elif a == False and b == True and c == False and d == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length", None))
            elif a == False and b == False and c == True and d == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Height", None))
            elif a == False and b == False and c == False and d == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length nor height is a valid number", None))
            elif a == False and b == False and c == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length nor height is a valid number", None))
        elif mainshape.shape in u"Volume - Equilateral triangular prism":
            a = is_number(self.ui.Input1.text())
            b = is_number(self.ui.Input2.text())
            if a == True and b == True:
                pass
            elif a == False and b == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Length is not a valid number", None))
            elif a == True and b == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Width is not a valid number", None))
            elif a == False and b == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Length nor width is a valid number", None))
        elif mainshape.shape in u"Volume - Hemisphere":
            a = is_number(self.ui.Input1.text())
            if a == True:
                pass
            else:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Side length is not a valid number", None))
        elif mainshape.shape in u"Volume - Torus":
            a = is_number(self.ui.Input1.text())
            b = is_number(self.ui.Input2.text())
            if a == True and b == True:
                pass
            elif a == False and b == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Length is not a valid number", None))
            elif a == True and b == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Width is not a valid number", None))
            elif a == False and b == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Length nor width is a valid number", None))
        elif mainshape.shape in u"Volume - Rhombicosidodecahedron":
            a = is_number(self.ui.Input1.text())
            if a == True:
                pass
            else:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Side length is not a valid number", None))
        elif mainshape.shape in u"Volume - Snub cube":
            a = is_number(self.ui.Input1.text())
            if a == True:
                pass
            else:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Side length is not a valid number", None))
        elif mainshape.shape in u"Volume - Capsule":
            a = is_number(self.ui.Input1.text())
            b = is_number(self.ui.Input2.text())
            if a == True and b == True:
                pass
            elif a == False and b == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Length is not a valid number", None))
            elif a == True and b == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Width is not a valid number", None))
            elif a == False and b == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Length nor width is a valid number", None))
        elif mainshape.shape in u"Volume - Tetrahedron":
            a = is_number(self.ui.Input1.text())
            if a == True:
                pass
            else:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Side length is not a valid number", None))
        elif mainshape.shape in u"Volume - Octahedron":
            a = is_number(self.ui.Input1.text())
            if a == True:
                pass
            else:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Side length is not a valid number", None))
        elif mainshape.shape in u"Volume - Icosahedron":
            a = is_number(self.ui.Input1.text())
            if a == True:
                pass
            else:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Side length is not a valid number", None))
        elif mainshape.shape in u"Volume - Isosceles triangular pyramid":
            a = is_number(self.ui.Input1.text())
            b = is_number(self.ui.Input2.text())
            c = is_number(self.ui.Input3.text())
            if a == True and b == True and c == True:
                pass
            elif a == False and b == True and c == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length is not a valid number", None))
            elif a == True and b == False and c == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Height is not a valiv number", None))
            elif a == True and b == True and c == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length nor height is a valid number", None))
            elif a == False and b == False and c == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length nor height is a valid number", None))
            elif a == False and b == True and c == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length", None))
            elif a == True and b == False and c == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Height", None))
            elif a == False and b == False and c == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length nor height is a valid number", None))
        elif mainshape.shape in u"Volume - Scalene triangular pyramid":
            a = is_number(self.ui.Input1.text())
            b = is_number(self.ui.Input2.text())
            c = is_number(self.ui.Input3.text())
            d = is_number(self.ui.Input4.text())
            if a == True and b == True and c == True and d == True:
                pass
            elif a == False and b == True and c == True and d == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length is not a valid number", None))
            elif a == True and b == False and c == True and d == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Height is not a valiv number", None))
            elif a == True and b == True and c == False and d == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length nor height is a valid number", None))
            elif a == True and b == True and c == True and d == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length nor height is a valid number", None))
            elif a == False and b == False and c == True and d == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length nor height is a valid number", None))
            elif a == True and b == False and c == False and d == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length", None))
            elif a == True and b == True and c == False and d == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Height", None))
            elif a == False and b == True and c == False and d == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length nor height is a valid number", None))
            elif a == True and b == False and c == True and d == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length nor height is a valid number", None))
            elif a == False and b == False and c == False and d == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length nor height is a valid number", None))
            elif a == True and b == False and c == False and d == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length nor height is a valid number", None))
            elif a == False and b == True and c == False and d == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length", None))
            elif a == False and b == False and c == True and d == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Height", None))
            elif a == False and b == False and c == False and d == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length nor height is a valid number", None))
            elif a == False and b == False and c == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length nor height is a valid number", None))
        elif mainshape.shape in u"Volume - Equilateral triangular pyramid":
            a = is_number(self.ui.Input1.text())
            b = is_number(self.ui.Input2.text())
            if a == True and b == True:
                pass
            elif a == False and b == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Length is not a valid number", None))
            elif a == True and b == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Width is not a valid number", None))
            elif a == False and b == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Length nor width is a valid number", None))
        elif mainshape.shape in u"Volume - Square pyramid":
            a = is_number(self.ui.Input1.text())
            b = is_number(self.ui.Input2.text())
            if a == True and b == True:
                pass
            elif a == False and b == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Length is not a valid number", None))
            elif a == True and b == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Width is not a valid number", None))
            elif a == False and b == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Length nor width is a valid number", None))
        elif mainshape.shape in u"Volume - Pentagonal pyramid":
            a = is_number(self.ui.Input1.text())
            b = is_number(self.ui.Input2.text())
            if a == True and b == True:
                pass
            elif a == False and b == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Length is not a valid number", None))
            elif a == True and b == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Width is not a valid number", None))
            elif a == False and b == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Length nor width is a valid number", None))
        elif mainshape.shape in u"Volume - Hexagonal pyramid":
            a = is_number(self.ui.Input1.text())
            b = is_number(self.ui.Input2.text())
            if a == True and b == True:
                pass
            elif a == False and b == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Length is not a valid number", None))
            elif a == True and b == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Width is not a valid number", None))
            elif a == False and b == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Length nor width is a valid number", None))
        elif mainshape.shape in u"Volume - Heptagonal pyramid":
            a = is_number(self.ui.Input1.text())
            b = is_number(self.ui.Input2.text())
            if a == True and b == True:
                pass
            elif a == False and b == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Length is not a valid number", None))
            elif a == True and b == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Width is not a valid number", None))
            elif a == False and b == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Length nor width is a valid number", None))
        elif mainshape.shape in u"Volume - Octagonal pyramid":
            a = is_number(self.ui.Input1.text())
            b = is_number(self.ui.Input2.text())
            if a == True and b == True:
                pass
            elif a == False and b == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Length is not a valid number", None))
            elif a == True and b == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Width is not a valid number", None))
            elif a == False and b == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Length nor width is a valid number", None))
        elif mainshape.shape in u"Volume - Nonagonal pyramid":
            a = is_number(self.ui.Input1.text())
            b = is_number(self.ui.Input2.text())
            if a == True and b == True:
                pass
            elif a == False and b == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Length is not a valid number", None))
            elif a == True and b == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Width is not a valid number", None))
            elif a == False and b == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Length nor width is a valid number", None))
        elif mainshape.shape in u"Volume - Decagonal pyramid":
            a = is_number(self.ui.Input1.text())
            b = is_number(self.ui.Input2.text())
            if a == True and b == True:
                pass
            elif a == False and b == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Length is not a valid number", None))
            elif a == True and b == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Width is not a valid number", None))
            elif a == False and b == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Length nor width is a valid number", None))
        elif mainshape.shape in u"Volume - Star prism":
            a = is_number(self.ui.Input1.text())
            b = is_number(self.ui.Input2.text())
            c = is_number(self.ui.Input3.text())
            if a == True and b == True and c == True:
                pass
            elif a == False and b == True and c == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length is not a valid number", None))
            elif a == True and b == False and c == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Height is not a valiv number", None))
            elif a == True and b == True and c == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length nor height is a valid number", None))
            elif a == False and b == False and c == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length nor height is a valid number", None))
            elif a == False and b == True and c == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length", None))
            elif a == True and b == False and c == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Height", None))
            elif a == False and b == False and c == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length nor height is a valid number", None))
        elif mainshape.shape in u"Volume - Isosceles triangular bipyramid":
            a = is_number(self.ui.Input1.text())
            b = is_number(self.ui.Input2.text())
            c = is_number(self.ui.Input3.text())
            if a == True and b == True and c == True:
                pass
            elif a == False and b == True and c == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length is not a valid number", None))
            elif a == True and b == False and c == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Height is not a valiv number", None))
            elif a == True and b == True and c == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length nor height is a valid number", None))
            elif a == False and b == False and c == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length nor height is a valid number", None))
            elif a == False and b == True and c == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length", None))
            elif a == True and b == False and c == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Height", None))
            elif a == False and b == False and c == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length nor height is a valid number", None))
        elif mainshape.shape in u"Volume - Scalene triangular bipyramid":
            a = is_number(self.ui.Input1.text())
            b = is_number(self.ui.Input2.text())
            c = is_number(self.ui.Input3.text())
            d = is_number(self.ui.Input4.text())
            if a == True and b == True and c == True and d == True:
                pass
            elif a == False and b == True and c == True and d == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length is not a valid number", None))
            elif a == True and b == False and c == True and d == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Height is not a valiv number", None))
            elif a == True and b == True and c == False and d == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length nor height is a valid number", None))
            elif a == True and b == True and c == True and d == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length nor height is a valid number", None))
            elif a == False and b == False and c == True and d == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length nor height is a valid number", None))
            elif a == True and b == False and c == False and d == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length", None))
            elif a == True and b == True and c == False and d == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Height", None))
            elif a == False and b == True and c == False and d == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length nor height is a valid number", None))
            elif a == True and b == False and c == True and d == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length nor height is a valid number", None))
            elif a == False and b == False and c == False and d == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length nor height is a valid number", None))
            elif a == True and b == False and c == False and d == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length nor height is a valid number", None))
            elif a == False and b == True and c == False and d == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length", None))
            elif a == False and b == False and c == True and d == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Height", None))
            elif a == False and b == False and c == False and d == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length nor height is a valid number", None))
            elif a == False and b == False and c == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Base length nor height is a valid number", None))
        elif mainshape.shape in u"Volume - Equilateral triangular bipyramid":
            a = is_number(self.ui.Input1.text())
            b = is_number(self.ui.Input2.text())
            if a == True and b == True:
                pass
            elif a == False and b == True:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Length is not a valid number", None))
            elif a == True and b == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Width is not a valid number", None))
            elif a == False and b == False:
                self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Length nor width is a valid number", None))
        else:
            self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Error", None))
        
    def update_shape(self, shape):
        Curr_shape = shape
        mainshape.shape = Curr_shape
        print("Curr_shape updated to:", Curr_shape)

    def update_units(self, text):
        # Update the variable Units_ans with the selected units
        Units_ans = text
        print("Units_ans updated to:", Units_ans)  # Debugging purpose, you can remove this line

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())