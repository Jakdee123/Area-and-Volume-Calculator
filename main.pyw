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

square = [u"\u00c1rea - Cuadrado"]
rectangle = [u"\u00c1rea - Rect\u00e1ngulo"]
circle = [u"\u00c1rea - C\u00edrculo"]
isosceles_triangle = [u"\u00c1rea - Tri\u00e1ngulo Is\u00f3sceles"]
scalene_triangle = [u"\u00c1rea - Tri\u00e1ngulo Escaleno"]
equilateral_triangle = [u"\u00c1rea - Tri\u00e1ngulo Equil\u00e1tero"]
pentagon = [u"\u00c1rea - Pent\u00e1gono"]
hexagon = [u"\u00c1rea - Hex\u00e1gono"]
heptagon = [u"\u00c1rea - Hept\u00e1gono"]
octagon = [u"\u00c1rea - Oct\u00e1gono"]
nonagon = [u"\u00c1rea - Non\u00e1gono"]
decagon = [u"\u00c1rea - Dec\u00e1gono"]
undecagon = [u"\u00c1rea - Undec\u00e1gono"]
dodecagon = [ u"\u00c1rea - Dodec\u00e1gono"]
tridecagon = [u"\u00c1rea - Tridec\u00e1gono"]
tetradecagon = [u"\u00c1rea - Tetradec\u00e1gono"]
pentadecagon = [u"\u00c1rea - Pentadec\u00e1gono"]
trapezoid = [u"\u00c1rea - Trapecio"]
ellipse = [ u"\u00c1rea - Elipse"]
polyomino = [u"\u00c1rea - Poliomino"]
star = [ u"\u00c1rea - Estrella"]
semicircle = [u"\u00c1rea - Semic\u00edrculo"]
squircle = [u"\u00c1rea - Squircle"]
parallelogram = [ u"\u00c1rea - Paralelogramo"]
annulus = [ u"\u00c1rea - Anillo"]
kite = [ u"\u00c1rea - Cometa"]
rhombus = [u"\u00c1rea - Romboides"]
cube = []
recprism = []
sphere = []
cylinder = []
cone = []
dodecahedron = [ u"Volumen - Dodecaedro"]
isoscelestriprism = [u"Volumen - Prisma Triangular Is\u00f3sceles"] 
scalenetriprism = [u"Volumen - Prisma Triangular Escaleno"]
equlateraltriprism = [u"Volumen - Prisma Triangular Equil\u00e1tero"]
hemisphere = [u"Volumen - Hemisferio"]
torus = [u"Volumen - Toro"]
rhombicosidodecahedron = [u"Volumen - Romboicosidodecaedro"]
snubcube = [u"Volumen - Cubo romo"]
capsule = [u"Volumen - C\u00e1psula"]
tetrahedron = [u"Volumen - Tetraedro"]
octahedron = [u"Volumen - Octaedro"]
icosahedron = [u"Volumen - Icosaedro"]
isoscelestripyra = [u"Volumen - Pir\u00e1mide Triangular Is\u00f3sceles"]
scalenetripyra = [u"Volumen - Pir\u00e1mide Triangular Escaleno"]
equlateraltripyra = [u"Volumen - Pir\u00e1mide Triangular Equil\u00e1tero"]
squarepyra = [u"Volumen - Pir\u00e1mide Cuadrada"]
pentagonpyra = [u"Volumen - Pir\u00e1mide Pentagonal"]
hexagonpyra = [u"Volumen - Pir\u00e1mide Hexagonal"]
heptagonpyra = [u"Volumen - Pir\u00e1mide Heptagonal"]
octagonpyra = [u"Volumen - Pir\u00e1mide Octagonal"]
nonagonpyra = [u"Volumen - Pir\u00e1mide Nonagonal"]
decagonpyra =[u"Volumen - Pir\u00e1mide Decagonal"]
starprism = [u"Volumen - Prisma estelar"]
isoscelesbipyra = [u"Volumen - Bipir\u00e1mide Triangular Is\u00f3sceles"]
scalenebipyra = [u"Volumen - Bipir\u00e1mide Triangular Escaleno"]
equlateralbipyra = [u"Volumen - Bipir\u00e1mide Triangular Equil\u00e1tero"]

class mainshape:
    shape = "Area - Square"

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
        self.title.setGeometry(QRect(80, 0, 201, 21))
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.title.setFont(font)
        self.title.setScaledContents(True)
        self.title.setAlignment(Qt.AlignCenter)
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(280, 0, 81, 22))
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
        self.comboBox_3.setGeometry(QRect(0, 0, 81, 22))
        font2 = QFont()
        font2.setPointSize(8)
        self.comboBox_3.setFont(font2)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(0, 180, 361, 41))
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
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(0, 130, 90, 31))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        self.plainTextEdit.setInputMethodHints(Qt.ImhDialableCharactersOnly|Qt.ImhDigitsOnly|Qt.ImhPreferNumbers)
        self.plainTextEdit_2 = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setGeometry(QRect(90, 130, 90, 31))
        sizePolicy.setHeightForWidth(self.plainTextEdit_2.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_2.setSizePolicy(sizePolicy)
        self.plainTextEdit_2.setInputMethodHints(Qt.ImhDialableCharactersOnly|Qt.ImhDigitsOnly|Qt.ImhPreferNumbers)
        self.plainTextEdit_3 = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        self.plainTextEdit_3.setGeometry(QRect(180, 130, 90, 31))
        sizePolicy.setHeightForWidth(self.plainTextEdit_3.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_3.setSizePolicy(sizePolicy)
        self.plainTextEdit_3.viewport().setProperty("cursor", QCursor(Qt.ForbiddenCursor))
        self.plainTextEdit_3.setInputMethodHints(Qt.ImhDialableCharactersOnly|Qt.ImhDigitsOnly|Qt.ImhPreferNumbers)
        self.plainTextEdit_3.setReadOnly(True)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(180, 110, 91, 20))
        self.label_6.setAlignment(Qt.AlignCenter)
        self.Input2 = QLabel(self.centralwidget)
        self.Input2.setObjectName(u"Input2")
        self.Input2.setGeometry(QRect(90, 110, 91, 20))
        self.Input2.setAlignment(Qt.AlignCenter)
        self.Inpu1 = QLabel(self.centralwidget)
        self.Inpu1.setObjectName(u"Inpu1")
        self.Inpu1.setGeometry(QRect(0, 110, 91, 20))
        self.Inpu1.setAlignment(Qt.AlignCenter)
        self.plainTextEdit_4 = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_4.setObjectName(u"plainTextEdit_4")
        self.plainTextEdit_4.setGeometry(QRect(270, 130, 90, 31))
        sizePolicy.setHeightForWidth(self.plainTextEdit_4.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_4.setSizePolicy(sizePolicy)
        self.plainTextEdit_4.setInputMethodHints(Qt.ImhDialableCharactersOnly|Qt.ImhDigitsOnly|Qt.ImhPreferNumbers)
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(270, 110, 91, 20))
        self.label_9.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Area and Volume Calculator", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"Area and Volume Calculator", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"English", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Espa\u00f1ol", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Fran\u00e7ais", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\u0420\u0443\u0441\u0441\u043a\u0438\u0439", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Deutsch", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"\u05e2\u05d1\u05e8\u05d9\u05ea", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"\u307b\u3093 ", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Portugu\u00eas", None))

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
        self.comboBox_2.setItemText(54, QCoreApplication.translate("MainWindow", u"Volume - Star prism pyramid", None))
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
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Input3", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Input4", None))
        self.Input2.setText(QCoreApplication.translate("MainWindow", u"Input2", None))
        self.Inpu1.setText(QCoreApplication.translate("MainWindow", u"Input1", None))




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  # Instantiate your existing UI class
        self.ui.setupUi(self)  # Setup your UI

        # Connect signals to slots here if needed
        self.ui.comboBox_3.currentTextChanged.connect(self.update_units)
        self.ui.comboBox_2.currentTextChanged.connect(self.update_shape)
        self.ui.pushButton_2.clicked.connect(self.solve)
        self.ui.comboBox.currentTextChanged.connect(self.lang_change_plz)
        # Add any additional setup or functionality here

    def solve(self):
        if mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
        elif mainshape.shape in square:
            pass
    def lang_change_plz(self, langu):
        global lang
        lang = langu
        if langu == "Español":
            self.ui.title.setText(QCoreApplication.translate("MainWindow", u"Calculadora de \u00c1rea y Volumen", None))
            self.ui.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"\u00c1rea - Cuadrado", None))
            self.ui.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"\u00c1rea - Rect\u00e1ngulo", None))
            self.ui.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"\u00c1rea - C\u00edrculo", None))
            self.ui.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"\u00c1rea - Tri\u00e1ngulo Is\u00f3sceles", None))
            self.ui.comboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"\u00c1rea - Tri\u00e1ngulo Escaleno", None))
            self.ui.comboBox_2.setItemText(5, QCoreApplication.translate("MainWindow", u"\u00c1rea - Tri\u00e1ngulo Equil\u00e1tero", None))
            self.ui.comboBox_2.setItemText(6, QCoreApplication.translate("MainWindow", u"\u00c1rea - Pent\u00e1gono", None))
            self.ui.comboBox_2.setItemText(7, QCoreApplication.translate("MainWindow", u"\u00c1rea - Hex\u00e1gono", None))
            self.ui.comboBox_2.setItemText(8, QCoreApplication.translate("MainWindow", u"\u00c1rea - Hept\u00e1gono", None))
            self.ui.comboBox_2.setItemText(9, QCoreApplication.translate("MainWindow", u"\u00c1rea - Oct\u00e1gono", None))
            self.ui.comboBox_2.setItemText(10, QCoreApplication.translate("MainWindow", u"\u00c1rea - Non\u00e1gono", None))
            self.ui.comboBox_2.setItemText(11, QCoreApplication.translate("MainWindow", u"\u00c1rea - Dec\u00e1gono", None))
            self.ui.comboBox_2.setItemText(12, QCoreApplication.translate("MainWindow", u"\u00c1rea - Undec\u00e1gono", None))
            self.ui.comboBox_2.setItemText(13, QCoreApplication.translate("MainWindow", u"\u00c1rea - Dodec\u00e1gono", None))
            self.ui.comboBox_2.setItemText(14, QCoreApplication.translate("MainWindow", u"\u00c1rea - Tridec\u00e1gono", None))
            self.ui.comboBox_2.setItemText(15, QCoreApplication.translate("MainWindow", u"\u00c1rea - Tetradec\u00e1gono", None))
            self.ui.comboBox_2.setItemText(16, QCoreApplication.translate("MainWindow", u"\u00c1rea - Pentadec\u00e1gono", None))
            self.ui.comboBox_2.setItemText(17, QCoreApplication.translate("MainWindow", u"\u00c1rea - Trapecio", None))
            self.ui.comboBox_2.setItemText(18, QCoreApplication.translate("MainWindow", u"\u00c1rea - Elipse", None))
            self.ui.comboBox_2.setItemText(19, QCoreApplication.translate("MainWindow", u"\u00c1rea - Poliomino", None))
            self.ui.comboBox_2.setItemText(20, QCoreApplication.translate("MainWindow", u"\u00c1rea - Estrella", None))
            self.ui.comboBox_2.setItemText(21, QCoreApplication.translate("MainWindow", u"\u00c1rea - Semic\u00edrculo", None))
            self.ui.comboBox_2.setItemText(22, QCoreApplication.translate("MainWindow", u"\u00c1rea - Squircle", None))
            self.ui.comboBox_2.setItemText(23, QCoreApplication.translate("MainWindow", u"\u00c1rea - Paralelogramo", None))
            self.ui.comboBox_2.setItemText(24, QCoreApplication.translate("MainWindow", u"\u00c1rea - Anillo", None))
            self.ui.comboBox_2.setItemText(25, QCoreApplication.translate("MainWindow", u"\u00c1rea - Cometa", None))
            self.ui.comboBox_2.setItemText(26, QCoreApplication.translate("MainWindow", u"\u00c1rea - Romboides", None))
            self.ui.comboBox_2.setItemText(27, QCoreApplication.translate("MainWindow", u"Volumen - Cubo", None))
            self.ui.comboBox_2.setItemText(28, QCoreApplication.translate("MainWindow", u"Volumen - Prisma Rectangular", None))
            self.ui.comboBox_2.setItemText(29, QCoreApplication.translate("MainWindow", u"Volumen - Esfera", None))
            self.ui.comboBox_2.setItemText(30, QCoreApplication.translate("MainWindow", u"Volumen - Cilindro", None))
            self.ui.comboBox_2.setItemText(31, QCoreApplication.translate("MainWindow", u"Volumen - Cono", None))
            self.ui.comboBox_2.setItemText(32, QCoreApplication.translate("MainWindow", u"Volumen - Dodecaedro", None))
            self.ui.comboBox_2.setItemText(33, QCoreApplication.translate("MainWindow", u"Volumen - Prisma Triangular Is\u00f3sceles", None))
            self.ui.comboBox_2.setItemText(34, QCoreApplication.translate("MainWindow", u"Volumen - Prisma Triangular Escaleno", None))
            self.ui.comboBox_2.setItemText(35, QCoreApplication.translate("MainWindow", u"Volumen - Prisma Triangular Equil\u00e1tero", None))
            self.ui.comboBox_2.setItemText(36, QCoreApplication.translate("MainWindow", u"Volumen - Hemisferio", None))
            self.ui.comboBox_2.setItemText(37, QCoreApplication.translate("MainWindow", u"Volumen - Toro", None))
            self.ui.comboBox_2.setItemText(38, QCoreApplication.translate("MainWindow", u"Volumen - Romboicosidodecaedro", None))
            self.ui.comboBox_2.setItemText(39, QCoreApplication.translate("MainWindow", u"Volumen - Cubo romo", None))
            self.ui.comboBox_2.setItemText(40, QCoreApplication.translate("MainWindow", u"Volumen - C\u00e1psula", None))
            self.ui.comboBox_2.setItemText(41, QCoreApplication.translate("MainWindow", u"Volumen - Tetraedro", None))
            self.ui.comboBox_2.setItemText(42, QCoreApplication.translate("MainWindow", u"Volumen - Octaedro", None))
            self.ui.comboBox_2.setItemText(43, QCoreApplication.translate("MainWindow", u"Volumen - Icosaedro", None))
            self.ui.comboBox_2.setItemText(44, QCoreApplication.translate("MainWindow", u"Volumen - Pir\u00e1mide Triangular Is\u00f3sceles", None))
            self.ui.comboBox_2.setItemText(45, QCoreApplication.translate("MainWindow", u"Volumen - Pir\u00e1mide Triangular Escaleno", None))
            self.ui.comboBox_2.setItemText(46, QCoreApplication.translate("MainWindow", u"Volumen - Pir\u00e1mide Triangular Equil\u00e1tero", None))
            self.ui.comboBox_2.setItemText(47, QCoreApplication.translate("MainWindow", u"Volumen - Pir\u00e1mide Cuadrada", None))
            self.ui.comboBox_2.setItemText(48, QCoreApplication.translate("MainWindow", u"Volumen - Pir\u00e1mide Pentagonal", None))
            self.ui.comboBox_2.setItemText(49, QCoreApplication.translate("MainWindow", u"Volumen - Pir\u00e1mide Hexagonal", None))
            self.ui.comboBox_2.setItemText(50, QCoreApplication.translate("MainWindow", u"Volumen - Pir\u00e1mide Heptagonal", None))
            self.ui.comboBox_2.setItemText(51, QCoreApplication.translate("MainWindow", u"Volumen - Pir\u00e1mide Octagonal", None))
            self.ui.comboBox_2.setItemText(52, QCoreApplication.translate("MainWindow", u"Volumen - Pir\u00e1mide Nonagonal", None))
            self.ui.comboBox_2.setItemText(53, QCoreApplication.translate("MainWindow", u"Volumen - Pir\u00e1mide Decagonal", None))
            self.ui.comboBox_2.setItemText(54, QCoreApplication.translate("MainWindow", u"Volumen - Prisma estelar", None))
            self.ui.comboBox_2.setItemText(55, QCoreApplication.translate("MainWindow", u"Volumen - Bipir\u00e1mide Triangular Is\u00f3sceles", None))
            self.ui.comboBox_2.setItemText(56, QCoreApplication.translate("MainWindow", u"Volumen - Bipir\u00e1mide Triangular Escaleno", None))
            self.ui.comboBox_2.setItemText(57, QCoreApplication.translate("MainWindow", u"Volumen - Bipir\u00e1mide Triangular Equil\u00e1tero", None))

            self.ui.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"Pulgadas", None))
            self.ui.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"Pies", None))
            self.ui.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"Yardas", None))
            self.ui.comboBox_3.setItemText(3, QCoreApplication.translate("MainWindow", u"Millas", None))
            self.ui.comboBox_3.setItemText(4, QCoreApplication.translate("MainWindow", u"Milímetros", None))
            self.ui.comboBox_3.setItemText(5, QCoreApplication.translate("MainWindow", u"Centímetros", None))
            self.ui.comboBox_3.setItemText(6, QCoreApplication.translate("MainWindow", u"Metros", None))
            self.ui.comboBox_3.setItemText(7, QCoreApplication.translate("MainWindow", u"Kilómetros", None))


            self.ui.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Calcular", ))
            self.ui.label.setText(QCoreApplication.translate("MainWindow", u"Forma:", None))
            self.ui.label_2.setText(QCoreApplication.translate("MainWindow", u"Fórmula:", None))
            self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Answer", None))
            self.ui.label_9.setText(QCoreApplication.translate("MainWindow", u"Input4", None))
            self.ui.label_6.setText(QCoreApplication.translate("MainWindow", u"Input3", None))
            self.ui.Input2.setText(QCoreApplication.translate("MainWindow", u"Input2", None))
            self.ui.Inpu1.setText(QCoreApplication.translate("MainWindow", u"Input1", None))
            
        elif langu == "Français":
            self.ui.title.setText(QCoreApplication.translate("MainWindow", u"Calculatrice de Surface et de Volume", None))
            self.ui.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Surface - Carré", None))
            self.ui.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Surface - Rectangle", None))
            self.ui.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Surface - Cercle", None))
            self.ui.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"Surface - Triangle Isocèle", None))
            self.ui.comboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"Surface - Triangle Scalène", None))
            self.ui.comboBox_2.setItemText(5, QCoreApplication.translate("MainWindow", u"Surface - Triangle Équilatéral", None))
            self.ui.comboBox_2.setItemText(6, QCoreApplication.translate("MainWindow", u"Surface - Pentagone", None))
            self.ui.comboBox_2.setItemText(7, QCoreApplication.translate("MainWindow", u"Surface - Hexagone", None))
            self.ui.comboBox_2.setItemText(8, QCoreApplication.translate("MainWindow", u"Surface - Heptagone", None))
            self.ui.comboBox_2.setItemText(9, QCoreApplication.translate("MainWindow", u"Surface - Octogone", None))
            self.ui.comboBox_2.setItemText(10, QCoreApplication.translate("MainWindow", u"Surface - Nonagone", None))
            self.ui.comboBox_2.setItemText(11, QCoreApplication.translate("MainWindow", u"Surface - Décagone", None))
            self.ui.comboBox_2.setItemText(12, QCoreApplication.translate("MainWindow", u"Surface - Undécagone", None))
            self.ui.comboBox_2.setItemText(13, QCoreApplication.translate("MainWindow", u"Surface - Dodécagone", None))
            self.ui.comboBox_2.setItemText(14, QCoreApplication.translate("MainWindow", u"Surface - Tridécagone", None))
            self.ui.comboBox_2.setItemText(15, QCoreApplication.translate("MainWindow", u"Surface - Tétradécagone", None))
            self.ui.comboBox_2.setItemText(16, QCoreApplication.translate("MainWindow", u"Surface - Pentadécagone", None))
            self.ui.comboBox_2.setItemText(17, QCoreApplication.translate("MainWindow", u"Surface - Trapèze", None))
            self.ui.comboBox_2.setItemText(18, QCoreApplication.translate("MainWindow", u"Surface - Ellipse", None))
            self.ui.comboBox_2.setItemText(19, QCoreApplication.translate("MainWindow", u"Surface - Polyomino", None))
            self.ui.comboBox_2.setItemText(20, QCoreApplication.translate("MainWindow", u"Surface - Étoile", None))
            self.ui.comboBox_2.setItemText(21, QCoreApplication.translate("MainWindow", u"Surface - Semicercle", None))
            self.ui.comboBox_2.setItemText(22, QCoreApplication.translate("MainWindow", u"Surface - Carré arrondi", None))
            self.ui.comboBox_2.setItemText(23, QCoreApplication.translate("MainWindow", u"Surface - Parallélogramme", None))
            self.ui.comboBox_2.setItemText(24, QCoreApplication.translate("MainWindow", u"Surface - Anneau", None))
            self.ui.comboBox_2.setItemText(25, QCoreApplication.translate("MainWindow", u"Surface - Cerf-volant", None))
            self.ui.comboBox_2.setItemText(26, QCoreApplication.translate("MainWindow", u"Surface - Losange", None))
            self.ui.comboBox_2.setItemText(27, QCoreApplication.translate("MainWindow", u"Volume - Cube", None))
            self.ui.comboBox_2.setItemText(28, QCoreApplication.translate("MainWindow", u"Volume - Prisme Rectangulaire", None))
            self.ui.comboBox_2.setItemText(29, QCoreApplication.translate("MainWindow", u"Volume - Sphère", None))
            self.ui.comboBox_2.setItemText(30, QCoreApplication.translate("MainWindow", u"Volume - Cylindre", None))
            self.ui.comboBox_2.setItemText(31, QCoreApplication.translate("MainWindow", u"Volume - Cône", None))
            self.ui.comboBox_2.setItemText(32, QCoreApplication.translate("MainWindow", u"Volume - Dodécaèdre", None))
            self.ui.comboBox_2.setItemText(33, QCoreApplication.translate("MainWindow", u"Volume - Prisme Triangulaire Isocèle", None))
            self.ui.comboBox_2.setItemText(34, QCoreApplication.translate("MainWindow", u"Volume - Prisme Triangulaire Scalène", None))
            self.ui.comboBox_2.setItemText(35, QCoreApplication.translate("MainWindow", u"Volume - Prisme Triangulaire Équilatéral", None))
            self.ui.comboBox_2.setItemText(36, QCoreApplication.translate("MainWindow", u"Volume - Hémisphère", None))
            self.ui.comboBox_2.setItemText(37, QCoreApplication.translate("MainWindow", u"Volume - Tore", None))
            self.ui.comboBox_2.setItemText(38, QCoreApplication.translate("MainWindow", u"Volume - Rhombicosidodécaèdre", None))
            self.ui.comboBox_2.setItemText(39, QCoreApplication.translate("MainWindow", u"Volume - Cube tronqué", None))
            self.ui.comboBox_2.setItemText(40, QCoreApplication.translate("MainWindow", u"Volume - Capsule", None))
            self.ui.comboBox_2.setItemText(41, QCoreApplication.translate("MainWindow", u"Volume - Tétraèdre", None))
            self.ui.comboBox_2.setItemText(42, QCoreApplication.translate("MainWindow", u"Volume - Octaèdre", None))
            self.ui.comboBox_2.setItemText(43, QCoreApplication.translate("MainWindow", u"Volume - Icosaèdre", None))
            self.ui.comboBox_2.setItemText(44, QCoreApplication.translate("MainWindow", u"Volume - Pyramide Triangulaire Isocèle", None))
            self.ui.comboBox_2.setItemText(45, QCoreApplication.translate("MainWindow", u"Volume - Pyramide Triangulaire Scalène", None))
            self.ui.comboBox_2.setItemText(46, QCoreApplication.translate("MainWindow", u"Volume - Pyramide Triangulaire Équilatérale", None))
            self.ui.comboBox_2.setItemText(47, QCoreApplication.translate("MainWindow", u"Volume - Pyramide Carrée", None))
            self.ui.comboBox_2.setItemText(48, QCoreApplication.translate("MainWindow", u"Volume - Pyramide Pentagonale", None))
            self.ui.comboBox_2.setItemText(49, QCoreApplication.translate("MainWindow", u"Volume - Pyramide Hexagonale", None))
            self.ui.comboBox_2.setItemText(50, QCoreApplication.translate("MainWindow", u"Volume - Pyramide Heptagonale", None))
            self.ui.comboBox_2.setItemText(51, QCoreApplication.translate("MainWindow", u"Volume - Pyramide Octogonale", None))
            self.ui.comboBox_2.setItemText(52, QCoreApplication.translate("MainWindow", u"Volume - Pyramide Nonagonale", None))
            self.ui.comboBox_2.setItemText(53, QCoreApplication.translate("MainWindow", u"Volume - Pyramide Décagonale", None))
            self.ui.comboBox_2.setItemText(54, QCoreApplication.translate("MainWindow", u"Volume - Pyramide Prismatique en Étoile", None))
            self.ui.comboBox_2.setItemText(55, QCoreApplication.translate("MainWindow", u"Volume - Bipyramide Triangulaire Isocèle", None))
            self.ui.comboBox_2.setItemText(56, QCoreApplication.translate("MainWindow", u"Volume - Bipyramide Triangulaire Scalène", None))
            self.ui.comboBox_2.setItemText(57, QCoreApplication.translate("MainWindow", u"Volume - Bipyramide Triangulaire Équilatérale", None))
            self.ui.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"Pouces", None))
            self.ui.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"Pieds", None))
            self.ui.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"Yards", None))
            self.ui.comboBox_3.setItemText(3, QCoreApplication.translate("MainWindow", u"Miles", None))
            self.ui.comboBox_3.setItemText(4, QCoreApplication.translate("MainWindow", u"Millimètres", None))
            self.ui.comboBox_3.setItemText(5, QCoreApplication.translate("MainWindow", u"Centimètres", None))
            self.ui.comboBox_3.setItemText(6, QCoreApplication.translate("MainWindow", u"Mètres", None))
            self.ui.comboBox_3.setItemText(7, QCoreApplication.translate("MainWindow", u"Kilomètres", None))
            self.ui.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Résoudre", None))
            self.ui.label.setText(QCoreApplication.translate("MainWindow", u"Forme:", None))
            self.ui.label_2.setText(QCoreApplication.translate("MainWindow", u"Formule:", None))
            self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Réponse", None))
            self.ui.label_6.setText(QCoreApplication.translate("MainWindow", u"Entrée 3", None))
            self.ui.label_9.setText(QCoreApplication.translate("MainWindow", u"Entrée 4", None))
            self.ui.Input2.setText(QCoreApplication.translate("MainWindow", u"Entrée 2", None))
            self.ui.Inpu1.setText(QCoreApplication.translate("MainWindow", u"Entrée 1", None))
        elif langu == "Русский":
            self.ui.title.setText(QCoreApplication.translate("MainWindow", u"Калькулятор Площади и Объема", None))
            self.ui.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Площадь - Квадрат", None))
            self.ui.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Площадь - Прямоугольник", None))
            self.ui.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Площадь - Круг", None))
            self.ui.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"Площадь - Равнобедренный треугольник", None))
            self.ui.comboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"Площадь - Неравносторонний треугольник", None))
            self.ui.comboBox_2.setItemText(5, QCoreApplication.translate("MainWindow", u"Площадь - Равносторонний треугольник", None))
            self.ui.comboBox_2.setItemText(6, QCoreApplication.translate("MainWindow", u"Площадь - Пятиугольник", None))
            self.ui.comboBox_2.setItemText(7, QCoreApplication.translate("MainWindow", u"Площадь - Шестиугольник", None))
            self.ui.comboBox_2.setItemText(8, QCoreApplication.translate("MainWindow", u"Площадь - Семиугольник", None))
            self.ui.comboBox_2.setItemText(9, QCoreApplication.translate("MainWindow", u"Площадь - Восьмиугольник", None))
            self.ui.comboBox_2.setItemText(10, QCoreApplication.translate("MainWindow", u"Площадь - Девятиугольник", None))
            self.ui.comboBox_2.setItemText(11, QCoreApplication.translate("MainWindow", u"Площадь - Десятиугольник", None))
            self.ui.comboBox_2.setItemText(12, QCoreApplication.translate("MainWindow", u"Площадь - Одиннадцатиугольник", None))
            self.ui.comboBox_2.setItemText(13, QCoreApplication.translate("MainWindow", u"Площадь - Двенадцатиугольник", None))
            self.ui.comboBox_2.setItemText(14, QCoreApplication.translate("MainWindow", u"Площадь - Тринадцатиугольник", None))
            self.ui.comboBox_2.setItemText(15, QCoreApplication.translate("MainWindow", u"Площадь - Четырнадцатиугольник", None))
            self.ui.comboBox_2.setItemText(16, QCoreApplication.translate("MainWindow", u"Площадь - Пятнадцатиугольник", None))
            self.ui.comboBox_2.setItemText(17, QCoreApplication.translate("MainWindow", u"Площадь - Трапеция", None))
            self.ui.comboBox_2.setItemText(18, QCoreApplication.translate("MainWindow", u"Площадь - Эллипс", None))
            self.ui.comboBox_2.setItemText(19, QCoreApplication.translate("MainWindow", u"Площадь - Полиомино", None))
            self.ui.comboBox_2.setItemText(20, QCoreApplication.translate("MainWindow", u"Площадь - Звезда", None))
            self.ui.comboBox_2.setItemText(21, QCoreApplication.translate("MainWindow", u"Площадь - Полукруг", None))
            self.ui.comboBox_2.setItemText(22, QCoreApplication.translate("MainWindow", u"Площадь - Квадрокруг", None))
            self.ui.comboBox_2.setItemText(23, QCoreApplication.translate("MainWindow", u"Площадь - Параллелограмм", None))
            self.ui.comboBox_2.setItemText(24, QCoreApplication.translate("MainWindow", u"Площадь - Кольцо", None))
            self.ui.comboBox_2.setItemText(25, QCoreApplication.translate("MainWindow", u"Площадь - Ромб", None))
            self.ui.comboBox_2.setItemText(26, QCoreApplication.translate("MainWindow", u"Площадь - Косинус", None))
            self.ui.comboBox_2.setItemText(27, QCoreApplication.translate("MainWindow", u"Объем - Куб", None))
            self.ui.comboBox_2.setItemText(28, QCoreApplication.translate("MainWindow", u"Объем - Параллелепипед", None))
            self.ui.comboBox_2.setItemText(29, QCoreApplication.translate("MainWindow", u"Объем - Сфера", None))
            self.ui.comboBox_2.setItemText(30, QCoreApplication.translate("MainWindow", u"Объем - Цилиндр", None))
            self.ui.comboBox_2.setItemText(31, QCoreApplication.translate("MainWindow", u"Объем - Конус", None))
            self.ui.comboBox_2.setItemText(32, QCoreApplication.translate("MainWindow", u"Объем - Додекаэдр", None))
            self.ui.comboBox_2.setItemText(33, QCoreApplication.translate("MainWindow", u"Объем - Равнобедренная треугольная призма", None))
            self.ui.comboBox_2.setItemText(34, QCoreApplication.translate("MainWindow", u"Объем - Неравнобедренная треугольная призма", None))
            self.ui.comboBox_2.setItemText(35, QCoreApplication.translate("MainWindow", u"Объем - Равносторонняя треугольная призма", None))
            self.ui.comboBox_2.setItemText(36, QCoreApplication.translate("MainWindow", u"Объем - Полусфера", None))
            self.ui.comboBox_2.setItemText(37, QCoreApplication.translate("MainWindow", u"Объем - Тор", None))
            self.ui.comboBox_2.setItemText(38, QCoreApplication.translate("MainWindow", u"Объем - Ромбокубоносиосидодекаэдр", None))
            self.ui.comboBox_2.setItemText(39, QCoreApplication.translate("MainWindow", u"Объем - Срубленный куб", None))
            self.ui.comboBox_2.setItemText(40, QCoreApplication.translate("MainWindow", u"Объем - Капсула", None))
            self.ui.comboBox_2.setItemText(41, QCoreApplication.translate("MainWindow", u"Объем - Тетраэдр", None))
            self.ui.comboBox_2.setItemText(42, QCoreApplication.translate("MainWindow", u"Объем - Октаэдр", None))
            self.ui.comboBox_2.setItemText(43, QCoreApplication.translate("MainWindow", u"Объем - Икосаэдр", None))
            self.ui.comboBox_2.setItemText(44, QCoreApplication.translate("MainWindow", u"Объем - Равнобедренная треугольная пирамида", None))
            self.ui.comboBox_2.setItemText(45, QCoreApplication.translate("MainWindow", u"Объем - Неравнобедренная треугольная пирамида", None))
            self.ui.comboBox_2.setItemText(46, QCoreApplication.translate("MainWindow", u"Объем - Равносторонняя треугольная пирамида", None))
            self.ui.comboBox_2.setItemText(47, QCoreApplication.translate("MainWindow", u"Объем - Квадратная пирамида", None))
            self.ui.comboBox_2.setItemText(48, QCoreApplication.translate("MainWindow", u"Объем - Пятиугольная пирамида", None))
            self.ui.comboBox_2.setItemText(49, QCoreApplication.translate("MainWindow", u"Объем - Шестиугольная пирамида", None))
            self.ui.comboBox_2.setItemText(50, QCoreApplication.translate("MainWindow", u"Объем - Семиугольная пирамида", None))
            self.ui.comboBox_2.setItemText(51, QCoreApplication.translate("MainWindow", u"Объем - Восьмиугольная пирамида", None))
            self.ui.comboBox_2.setItemText(52, QCoreApplication.translate("MainWindow", u"Объем - Девятиугольная пирамида", None))
            self.ui.comboBox_2.setItemText(53, QCoreApplication.translate("MainWindow", u"Объем - Десятиугольная пирамида", None))
            self.ui.comboBox_2.setItemText(54, QCoreApplication.translate("MainWindow", u"Объем - Пирамида звезды", None))
            self.ui.comboBox_2.setItemText(55, QCoreApplication.translate("MainWindow", u"Объем - Равнобедренная треугольная бипирамида", None))
            self.ui.comboBox_2.setItemText(56, QCoreApplication.translate("MainWindow", u"Объем - Неравнобедренная треугольная бипирамида", None))
            self.ui.comboBox_2.setItemText(57, QCoreApplication.translate("MainWindow", u"Объем - Равносторонняя треугольная бипирамида", None))
            self.ui.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"Дюймы", None))
            self.ui.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"Футы", None))
            self.ui.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"Ярды", None))
            self.ui.comboBox_3.setItemText(3, QCoreApplication.translate("MainWindow", u"Мили", None))
            self.ui.comboBox_3.setItemText(4, QCoreApplication.translate("MainWindow", u"Миллиметры", None))
            self.ui.comboBox_3.setItemText(5, QCoreApplication.translate("MainWindow", u"Сантиметры", None))
            self.ui.comboBox_3.setItemText(6, QCoreApplication.translate("MainWindow", u"Метры", None))
            self.ui.comboBox_3.setItemText(7, QCoreApplication.translate("MainWindow", u"Километры", None))
            self.ui.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Решить", ))
            self.ui.label.setText(QCoreApplication.translate("MainWindow", u"Фигура:", None))
            self.ui.label_2.setText(QCoreApplication.translate("MainWindow", u"Формула:", None))
            self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Ответ", None))
            self.ui.label_6.setText(QCoreApplication.translate("MainWindow", u"Ввод3", None))
            self.ui.label_9.setText(QCoreApplication.translate("MainWindow", u"Ввод4", None))
            self.ui.Input2.setText(QCoreApplication.translate("MainWindow", u"Ввод2", None))
            self.ui.Inpu1.setText(QCoreApplication.translate("MainWindow", u"Ввод1", None))
        elif langu == "Deutsch":
            self.ui.title.setText(QCoreApplication.translate("MainWindow", u"Flächen- und Volumenrechner", None))
            self.ui.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Fläche - Quadrat", None))
            self.ui.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Fläche - Rechteck", None))
            self.ui.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Fläche - Kreis", None))
            self.ui.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"Fläche - gleichschenkliges Dreieck", None))
            self.ui.comboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"Fläche - ungleichseitiges Dreieck", None))
            self.ui.comboBox_2.setItemText(5, QCoreApplication.translate("MainWindow", u"Fläche - gleichseitiges Dreieck", None))
            self.ui.comboBox_2.setItemText(6, QCoreApplication.translate("MainWindow", u"Fläche - Fünfeck", None))
            self.ui.comboBox_2.setItemText(7, QCoreApplication.translate("MainWindow", u"Fläche - Sechseck", None))
            self.ui.comboBox_2.setItemText(8, QCoreApplication.translate("MainWindow", u"Fläche - Siebeneck", None))
            self.ui.comboBox_2.setItemText(9, QCoreApplication.translate("MainWindow", u"Fläche - Achteck", None))
            self.ui.comboBox_2.setItemText(10, QCoreApplication.translate("MainWindow", u"Fläche - Neuneck", None))
            self.ui.comboBox_2.setItemText(11, QCoreApplication.translate("MainWindow", u"Fläche - Zehneck", None))
            self.ui.comboBox_2.setItemText(12, QCoreApplication.translate("MainWindow", u"Fläche - Elfeneck", None))
            self.ui.comboBox_2.setItemText(13, QCoreApplication.translate("MainWindow", u"Fläche - Zwölfeck", None))
            self.ui.comboBox_2.setItemText(14, QCoreApplication.translate("MainWindow", u"Fläche - Dreizehneck", None))
            self.ui.comboBox_2.setItemText(15, QCoreApplication.translate("MainWindow", u"Fläche - Vierzehneck", None))
            self.ui.comboBox_2.setItemText(16, QCoreApplication.translate("MainWindow", u"Fläche - Fünfzehneck", None))
            self.ui.comboBox_2.setItemText(17, QCoreApplication.translate("MainWindow", u"Fläche - Trapezoid", None))
            self.ui.comboBox_2.setItemText(18, QCoreApplication.translate("MainWindow", u"Fläche - Ellipse", None))
            self.ui.comboBox_2.setItemText(19, QCoreApplication.translate("MainWindow", u"Fläche - Polyomino", None))
            self.ui.comboBox_2.setItemText(20, QCoreApplication.translate("MainWindow", u"Fläche - Stern", None))
            self.ui.comboBox_2.setItemText(21, QCoreApplication.translate("MainWindow", u"Fläche - Halbkreis", None))
            self.ui.comboBox_2.setItemText(22, QCoreApplication.translate("MainWindow", u"Fläche - Squircle", None))
            self.ui.comboBox_2.setItemText(23, QCoreApplication.translate("MainWindow", u"Fläche - Parallelogramm", None))
            self.ui.comboBox_2.setItemText(24, QCoreApplication.translate("MainWindow", u"Fläche - Ring", None))
            self.ui.comboBox_2.setItemText(25, QCoreApplication.translate("MainWindow", u"Fläche - Drachen", None))
            self.ui.comboBox_2.setItemText(26, QCoreApplication.translate("MainWindow", u"Fläche - Rhombus", None))
            self.ui.comboBox_2.setItemText(27, QCoreApplication.translate("MainWindow", u"Volumen - Würfel", None))
            self.ui.comboBox_2.setItemText(28, QCoreApplication.translate("MainWindow", u"Volumen - Quader", None))
            self.ui.comboBox_2.setItemText(29, QCoreApplication.translate("MainWindow", u"Volumen - Kugel", None))
            self.ui.comboBox_2.setItemText(30, QCoreApplication.translate("MainWindow", u"Volumen - Zylinder", None))
            self.ui.comboBox_2.setItemText(31, QCoreApplication.translate("MainWindow", u"Volumen - Kegel", None))
            self.ui.comboBox_2.setItemText(32, QCoreApplication.translate("MainWindow", u"Volumen - Dodekaeder", None))
            self.ui.comboBox_2.setItemText(33, QCoreApplication.translate("MainWindow", u"Volumen - gleichschenkliges Dreiecksprisma", None))
            self.ui.comboBox_2.setItemText(34, QCoreApplication.translate("MainWindow", u"Volumen - ungleichseitiges Dreiecksprisma", None))
            self.ui.comboBox_2.setItemText(35, QCoreApplication.translate("MainWindow", u"Volumen - gleichseitiges Dreiecksprisma", None))
            self.ui.comboBox_2.setItemText(36, QCoreApplication.translate("MainWindow", u"Volumen - Halbkugel", None))
            self.ui.comboBox_2.setItemText(37, QCoreApplication.translate("MainWindow", u"Volumen - Torus", None))
            self.ui.comboBox_2.setItemText(38, QCoreApplication.translate("MainWindow", u"Volumen - Rhombicosidodecaeder", None))
            self.ui.comboBox_2.setItemText(39, QCoreApplication.translate("MainWindow", u"Volumen - Schubscheibe", None))
            self.ui.comboBox_2.setItemText(40, QCoreApplication.translate("MainWindow", u"Volumen - Kapsel", None))
            self.ui.comboBox_2.setItemText(41, QCoreApplication.translate("MainWindow", u"Volumen - Tetraeder", None))
            self.ui.comboBox_2.setItemText(42, QCoreApplication.translate("MainWindow", u"Volumen - Oktaeder", None))
            self.ui.comboBox_2.setItemText(43, QCoreApplication.translate("MainWindow", u"Volumen - Ikosaeder", None))
            self.ui.comboBox_2.setItemText(44, QCoreApplication.translate("MainWindow", u"Volumen - gleichschenkliges Dreieckspyramid", None))
            self.ui.comboBox_2.setItemText(45, QCoreApplication.translate("MainWindow", u"Volumen - ungleichseitiges Dreieckspyramid", None))
            self.ui.comboBox_2.setItemText(46, QCoreApplication.translate("MainWindow", u"Volumen - gleichseitiges Dreieckspyramid", None))
            self.ui.comboBox_2.setItemText(47, QCoreApplication.translate("MainWindow", u"Volumen - Quadratpyramid", None))
            self.ui.comboBox_2.setItemText(48, QCoreApplication.translate("MainWindow", u"Volumen - Fünfeckpyramid", None))
            self.ui.comboBox_2.setItemText(49, QCoreApplication.translate("MainWindow", u"Volumen - Sechseckpyramid", None))
            self.ui.comboBox_2.setItemText(50, QCoreApplication.translate("MainWindow", u"Volumen - Siebeneckpyramid", None))
            self.ui.comboBox_2.setItemText(51, QCoreApplication.translate("MainWindow", u"Volumen - Achteckpyramid", None))
            self.ui.comboBox_2.setItemText(52, QCoreApplication.translate("MainWindow", u"Volumen - Neuneckpyramid", None))
            self.ui.comboBox_2.setItemText(53, QCoreApplication.translate("MainWindow", u"Volumen - Zehneckpyramid", None))
            self.ui.comboBox_2.setItemText(54, QCoreApplication.translate("MainWindow", u"Volumen - Sternprismapyramid", None))
            self.ui.comboBox_2.setItemText(55, QCoreApplication.translate("MainWindow", u"Volumen - gleichschenkliges Dreiecksbipyramid", None))
            self.ui.comboBox_2.setItemText(56, QCoreApplication.translate("MainWindow", u"Volumen - ungleichseitiges Dreiecksbipyramid", None))
            self.ui.comboBox_2.setItemText(57, QCoreApplication.translate("MainWindow", u"Volumen - gleichseitiges Dreiecksbipyramid", None))
            self.ui.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"Zoll", None))
            self.ui.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"Füße", None))
            self.ui.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"Yards", None))
            self.ui.comboBox_3.setItemText(3, QCoreApplication.translate("MainWindow", u"Meilen", None))
            self.ui.comboBox_3.setItemText(4, QCoreApplication.translate("MainWindow", u"Millimeter", None))
            self.ui.comboBox_3.setItemText(5, QCoreApplication.translate("MainWindow", u"Zentimeter", None))
            self.ui.comboBox_3.setItemText(6, QCoreApplication.translate("MainWindow", u"Meter", None))
            self.ui.comboBox_3.setItemText(7, QCoreApplication.translate("MainWindow", u"Kilometer", None))
            self.ui.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Lösen", None))
            self.ui.label.setText(QCoreApplication.translate("MainWindow", u"Form:", None))
            self.ui.label_2.setText(QCoreApplication.translate("MainWindow", u"Formel:", None))
            self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Antwort", None))
            self.ui.label_6.setText(QCoreApplication.translate("MainWindow", u"Eingabe3", None))
            self.ui.label_9.setText(QCoreApplication.translate("MainWindow", u"Eingabe4", None))
            self.ui.Input2.setText(QCoreApplication.translate("MainWindow", u"Eingabe2", None))
            self.ui.Inpu1.setText(QCoreApplication.translate("MainWindow", u"Eingabe1", None))
        elif langu == "עברית":
            self.ui.title.setText(QCoreApplication.translate("MainWindow", u"מחשבון שטח ונפח", None))
            self.ui.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"שטח - ריבוע", None))
            self.ui.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"שטח - מלבן", None))
            self.ui.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"שטח - מעגל", None))
            self.ui.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"שטח - משולש שווה צלעות", None))
            self.ui.comboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"שטח - משולש לא שווה צלעות", None))
            self.ui.comboBox_2.setItemText(5, QCoreApplication.translate("MainWindow", u"שטח - משולש שווה צלעות", None))
            self.ui.comboBox_2.setItemText(6, QCoreApplication.translate("MainWindow", u"שטח - פנטגון", None))
            self.ui.comboBox_2.setItemText(7, QCoreApplication.translate("MainWindow", u"שטח - הקסגון", None))
            self.ui.comboBox_2.setItemText(8, QCoreApplication.translate("MainWindow", u"שטח - הפטגון", None))
            self.ui.comboBox_2.setItemText(9, QCoreApplication.translate("MainWindow", u"שטח - אוקטגון", None))
            self.ui.comboBox_2.setItemText(10, QCoreApplication.translate("MainWindow", u"שטח - נונגון", None))
            self.ui.comboBox_2.setItemText(11, QCoreApplication.translate("MainWindow", u"שטח - דקאגון", None))
            self.ui.comboBox_2.setItemText(12, QCoreApplication.translate("MainWindow", u"שטח - אונדקאגון", None))
            self.ui.comboBox_2.setItemText(13, QCoreApplication.translate("MainWindow", u"שטח - דודקאגון", None))
            self.ui.comboBox_2.setItemText(14, QCoreApplication.translate("MainWindow", u"שטח - טרידקאגון", None))
            self.ui.comboBox_2.setItemText(15, QCoreApplication.translate("MainWindow", u"שטח - טטראדקאגון", None))
            self.ui.comboBox_2.setItemText(16, QCoreApplication.translate("MainWindow", u"שטח - פנטאדקאגון", None))
            self.ui.comboBox_2.setItemText(17, QCoreApplication.translate("MainWindow", u"שטח - משולש טרפז", None))
            self.ui.comboBox_2.setItemText(18, QCoreApplication.translate("MainWindow", u"שטח - אליפסה", None))
            self.ui.comboBox_2.setItemText(19, QCoreApplication.translate("MainWindow", u"שטח - פוליומינו", None))
            self.ui.comboBox_2.setItemText(20, QCoreApplication.translate("MainWindow", u"שטח - כוכב", None))
            self.ui.comboBox_2.setItemText(21, QCoreApplication.translate("MainWindow", u"שטח - חצי מעגל", None))
            self.ui.comboBox_2.setItemText(22, QCoreApplication.translate("MainWindow", u"שטח - ריבוע מעגלי", None))
            self.ui.comboBox_2.setItemText(23, QCoreApplication.translate("MainWindow", u"שטח - מקבילית", None))
            self.ui.comboBox_2.setItemText(24, QCoreApplication.translate("MainWindow", u"שטח - תסתורת", None))
            self.ui.comboBox_2.setItemText(25, QCoreApplication.translate("MainWindow", u"שטח - עפרון", None))
            self.ui.comboBox_2.setItemText(26, QCoreApplication.translate("MainWindow", u"שטח - מעוי", None))
            self.ui.comboBox_2.setItemText(27, QCoreApplication.translate("MainWindow", u"נפח - קובייה", None))
            self.ui.comboBox_2.setItemText(28, QCoreApplication.translate("MainWindow", u"נפח - פריזמה מלבנית", None))
            self.ui.comboBox_2.setItemText(29, QCoreApplication.translate("MainWindow", u"נפח - כדור", None))
            self.ui.comboBox_2.setItemText(30, QCoreApplication.translate("MainWindow", u"נפח - גליל", None))
            self.ui.comboBox_2.setItemText(31, QCoreApplication.translate("MainWindow", u"נפח - חפץ", None))
            self.ui.comboBox_2.setItemText(32, QCoreApplication.translate("MainWindow", u"נפח - דודקהדרון", None))
            self.ui.comboBox_2.setItemText(33, QCoreApplication.translate("MainWindow", u"נפח - פריזמה משולשת שווה צלעות", None))
            self.ui.comboBox_2.setItemText(34, QCoreApplication.translate("MainWindow", u"נפח - פריזמה משולשת לא שווה צלעות", None))
            self.ui.comboBox_2.setItemText(35, QCoreApplication.translate("MainWindow", u"נפח - פריזמה משולשת שווה צלעות", None))
            self.ui.comboBox_2.setItemText(36, QCoreApplication.translate("MainWindow", u"נפח - חצי כדור", None))
            self.ui.comboBox_2.setItemText(37, QCoreApplication.translate("MainWindow", u"נפח - טורוס", None))
            self.ui.comboBox_2.setItemText(38, QCoreApplication.translate("MainWindow", u"נפח - רומביקוסידודקהדרון", None))
            self.ui.comboBox_2.setItemText(39, QCoreApplication.translate("MainWindow", u"נפח - קובה מנוכרית", None))
            self.ui.comboBox_2.setItemText(40, QCoreApplication.translate("MainWindow", u"נפח - קפסולה", None))
            self.ui.comboBox_2.setItemText(41, QCoreApplication.translate("MainWindow", u"נפח - טטרהדרון", None))
            self.ui.comboBox_2.setItemText(42, QCoreApplication.translate("MainWindow", u"נפח - אוקטהדרון", None))
            self.ui.comboBox_2.setItemText(43, QCoreApplication.translate("MainWindow", u"נפח - איקוסהדרון", None))
            self.ui.comboBox_2.setItemText(44, QCoreApplication.translate("MainWindow", u"נפח - פירמידה משולשת שווה צלעות", None))
            self.ui.comboBox_2.setItemText(45, QCoreApplication.translate("MainWindow", u"נפח - פירמידה משולשת לא שווה צלעות", None))
            self.ui.comboBox_2.setItemText(46, QCoreApplication.translate("MainWindow", u"נפח - פירמידה משולשת שווה צלעות", None))
            self.ui.comboBox_2.setItemText(47, QCoreApplication.translate("MainWindow", u"נפח - פירמידת ריבוע", None))
            self.ui.comboBox_2.setItemText(48, QCoreApplication.translate("MainWindow", u"נפח - פירמידת חמש", None))
            self.ui.comboBox_2.setItemText(49, QCoreApplication.translate("MainWindow", u"נפח - פירמידת שש", None))
            self.ui.comboBox_2.setItemText(50, QCoreApplication.translate("MainWindow", u"נפח - פירמידת שבע", None))
            self.ui.comboBox_2.setItemText(51, QCoreApplication.translate("MainWindow", u"נפח - פירמידת שמונה", None))
            self.ui.comboBox_2.setItemText(52, QCoreApplication.translate("MainWindow", u"נפח - פירמידת תשע", None))
            self.ui.comboBox_2.setItemText(53, QCoreApplication.translate("MainWindow", u"נפח - פירמידת עשר", None))
            self.ui.comboBox_2.setItemText(54, QCoreApplication.translate("MainWindow", u"נפח - פירמידת כוכב", None))
            self.ui.comboBox_2.setItemText(55, QCoreApplication.translate("MainWindow", u"נפח - ביפירמידה משולשת שווה צלעות", None))
            self.ui.comboBox_2.setItemText(56, QCoreApplication.translate("MainWindow", u"נפח - ביפירמידה משולשת לא שווה צלעות", None))
            self.ui.comboBox_2.setItemText(57, QCoreApplication.translate("MainWindow", u"נפח - ביפירמידה משולשת שווה צלעות", None))
            self.ui.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"אינצ׳ים", None))
            self.ui.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"רגליים", None))
            self.ui.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"יארדים", None))
            self.ui.comboBox_3.setItemText(3, QCoreApplication.translate("MainWindow", u"מיילים", None))
            self.ui.comboBox_3.setItemText(4, QCoreApplication.translate("MainWindow", u"מילימטרים", None))
            self.ui.comboBox_3.setItemText(5, QCoreApplication.translate("MainWindow", u"סנטימטרים", None))
            self.ui.comboBox_3.setItemText(6, QCoreApplication.translate("MainWindow", u"מטרים", None))
            self.ui.comboBox_3.setItemText(7, QCoreApplication.translate("MainWindow", u"קילומטרים", None))
            self.ui.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"פתור", ))
            self.ui.label.setText(QCoreApplication.translate("MainWindow", u"צורה:", None))
            self.ui.label_2.setText(QCoreApplication.translate("MainWindow", u"נוסחא:", None))
            self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"תשובה", None))
            self.ui.label_6.setText(QCoreApplication.translate("MainWindow", u"הזן 3", None))
            self.ui.label_9.setText(QCoreApplication.translate("MainWindow", u"הזן 4", None))
            self.ui.Input2.setText(QCoreApplication.translate("MainWindow", u"הזן 2", None))
            self.ui.Inpu1.setText(QCoreApplication.translate("MainWindow", u"הזן 1", None))
        elif langu == u"ほん":
            self.ui.title.setText(QCoreApplication.translate("MainWindow", u"面積と体積の計算機", None))
            self.ui.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"面積 - 正方形", None))
            self.ui.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"面積 - 長方形", None))
            self.ui.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"面積 - 円", None))
            self.ui.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"面積 - 二等辺三角形", None))
            self.ui.comboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"面積 - 不等辺三角形", None))
            self.ui.comboBox_2.setItemText(5, QCoreApplication.translate("MainWindow", u"面積 - 正三角形", None))
            self.ui.comboBox_2.setItemText(6, QCoreApplication.translate("MainWindow", u"面積 - 五角形", None))
            self.ui.comboBox_2.setItemText(7, QCoreApplication.translate("MainWindow", u"面積 - 六角形", None))
            self.ui.comboBox_2.setItemText(8, QCoreApplication.translate("MainWindow", u"面積 - 七角形", None))
            self.ui.comboBox_2.setItemText(9, QCoreApplication.translate("MainWindow", u"面積 - 八角形", None))
            self.ui.comboBox_2.setItemText(10, QCoreApplication.translate("MainWindow", u"面積 - 九角形", None))
            self.ui.comboBox_2.setItemText(11, QCoreApplication.translate("MainWindow", u"面積 - 十角形", None))
            self.ui.comboBox_2.setItemText(12, QCoreApplication.translate("MainWindow", u"面積 - 十一角形", None))
            self.ui.comboBox_2.setItemText(13, QCoreApplication.translate("MainWindow", u"面積 - 十二角形", None))
            self.ui.comboBox_2.setItemText(14, QCoreApplication.translate("MainWindow", u"面積 - 十三角形", None))
            self.ui.comboBox_2.setItemText(15, QCoreApplication.translate("MainWindow", u"面積 - 十四角形", None))
            self.ui.comboBox_2.setItemText(16, QCoreApplication.translate("MainWindow", u"面積 - 十五角形", None))
            self.ui.comboBox_2.setItemText(17, QCoreApplication.translate("MainWindow", u"面積 - 台形", None))
            self.ui.comboBox_2.setItemText(18, QCoreApplication.translate("MainWindow", u"面積 - 楕円", None))
            self.ui.comboBox_2.setItemText(19, QCoreApplication.translate("MainWindow", u"面積 - ポリオミノ", None))
            self.ui.comboBox_2.setItemText(20, QCoreApplication.translate("MainWindow", u"面積 - 星形", None))
            self.ui.comboBox_2.setItemText(21, QCoreApplication.translate("MainWindow", u"面積 - 半円", None))
            self.ui.comboBox_2.setItemText(22, QCoreApplication.translate("MainWindow", u"面積 - スクイアクル", None))
            self.ui.comboBox_2.setItemText(23, QCoreApplication.translate("MainWindow", u"面積 - 平行四辺形", None))
            self.ui.comboBox_2.setItemText(24, QCoreApplication.translate("MainWindow", u"面積 - 環状", None))
            self.ui.comboBox_2.setItemText(25, QCoreApplication.translate("MainWindow", u"面積 - 凧", None))
            self.ui.comboBox_2.setItemText(26, QCoreApplication.translate("MainWindow", u"面積 - ひし形", None))
            self.ui.comboBox_2.setItemText(27, QCoreApplication.translate("MainWindow", u"体積 - 立方体", None))
            self.ui.comboBox_2.setItemText(28, QCoreApplication.translate("MainWindow", u"体積 - 直方体", None))
            self.ui.comboBox_2.setItemText(29, QCoreApplication.translate("MainWindow", u"体積 - 球", None))
            self.ui.comboBox_2.setItemText(30, QCoreApplication.translate("MainWindow", u"体積 - 円柱", None))
            self.ui.comboBox_2.setItemText(31, QCoreApplication.translate("MainWindow", u"体積 - 円錐", None))
            self.ui.comboBox_2.setItemText(32, QCoreApplication.translate("MainWindow", u"体積 - 正十二面体", None))
            self.ui.comboBox_2.setItemText(33, QCoreApplication.translate("MainWindow", u"体積 - 二等辺三角柱", None))
            self.ui.comboBox_2.setItemText(34, QCoreApplication.translate("MainWindow", u"体積 - 不等辺三角柱", None))
            self.ui.comboBox_2.setItemText(35, QCoreApplication.translate("MainWindow", u"体積 - 正三角形柱", None))
            self.ui.comboBox_2.setItemText(36, QCoreApplication.translate("MainWindow", u"体積 - 半球", None))
            self.ui.comboBox_2.setItemText(37, QCoreApplication.translate("MainWindow", u"体積 - トーラス", None))
            self.ui.comboBox_2.setItemText(38, QCoreApplication.translate("MainWindow", u"体積 - ロンビコシドデカヘドロン", None))
            self.ui.comboBox_2.setItemText(39, QCoreApplication.translate("MainWindow", u"体積 - スナブキューブ", None))
            self.ui.comboBox_2.setItemText(40, QCoreApplication.translate("MainWindow", u"体積 - カプセル", None))
            self.ui.comboBox_2.setItemText(41, QCoreApplication.translate("MainWindow", u"体積 - 正四面体", None))
            self.ui.comboBox_2.setItemText(42, QCoreApplication.translate("MainWindow", u"体積 - 正八面体", None))
            self.ui.comboBox_2.setItemText(43, QCoreApplication.translate("MainWindow", u"体積 - 正二十面体", None))
            self.ui.comboBox_2.setItemText(44, QCoreApplication.translate("MainWindow", u"体積 - 二等辺三角錐", None))
            self.ui.comboBox_2.setItemText(45, QCoreApplication.translate("MainWindow", u"体積 - 不等辺三角錐", None))
            self.ui.comboBox_2.setItemText(46, QCoreApplication.translate("MainWindow", u"体積 - 正三角形錐", None))
            self.ui.comboBox_2.setItemText(47, QCoreApplication.translate("MainWindow", u"体積 - 正方錐", None))
            self.ui.comboBox_2.setItemText(48, QCoreApplication.translate("MainWindow", u"体積 - 五角錐", None))
            self.ui.comboBox_2.setItemText(49, QCoreApplication.translate("MainWindow", u"体積 - 六角錐", None))
            self.ui.comboBox_2.setItemText(50, QCoreApplication.translate("MainWindow", u"体積 - 七角錐", None))
            self.ui.comboBox_2.setItemText(51, QCoreApplication.translate("MainWindow", u"体積 - 八角錐", None))
            self.ui.comboBox_2.setItemText(52, QCoreApplication.translate("MainWindow", u"体積 - 九角錐", None))
            self.ui.comboBox_2.setItemText(53, QCoreApplication.translate("MainWindow", u"体積 - 十角錐", None))
            self.ui.comboBox_2.setItemText(54, QCoreApplication.translate("MainWindow", u"体積 - 星柱錐", None))
            self.ui.comboBox_2.setItemText(55, QCoreApplication.translate("MainWindow", u"体積 - 二等辺三角二重錐", None))
            self.ui.comboBox_2.setItemText(56, QCoreApplication.translate("MainWindow", u"体積 - 不等辺三角二重錐", None))
            self.ui.comboBox_2.setItemText(57, QCoreApplication.translate("MainWindow", u"体積 - 正三角形二重錐", None))
            self.ui.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"インチ", None))
            self.ui.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"フィート", None))
            self.ui.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"ヤード", None))
            self.ui.comboBox_3.setItemText(3, QCoreApplication.translate("MainWindow", u"マイル", None))
            self.ui.comboBox_3.setItemText(4, QCoreApplication.translate("MainWindow", u"ミリメートル", None))
            self.ui.comboBox_3.setItemText(5, QCoreApplication.translate("MainWindow", u"センチメートル", None))
            self.ui.comboBox_3.setItemText(6, QCoreApplication.translate("MainWindow", u"メートル", None))
            self.ui.comboBox_3.setItemText(7, QCoreApplication.translate("MainWindow", u"キロメートル", None))
            self.ui.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"解決", ))
            self.ui.label.setText(QCoreApplication.translate("MainWindow", u"形状:", None))
            self.ui.label_2.setText(QCoreApplication.translate("MainWindow", u"式:", None))
            self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"答え", None))
            self.ui.label_6.setText(QCoreApplication.translate("MainWindow", u"入力3", None))
            self.ui.label_9.setText(QCoreApplication.translate("MainWindow", u"入力4", None))
            self.ui.Input2.setText(QCoreApplication.translate("MainWindow", u"入力2", None))
            self.ui.Inpu1.setText(QCoreApplication.translate("MainWindow", u"入力1", None))
        elif langu == "Português":
            self.ui.title.setText(QCoreApplication.translate("MainWindow", u"Calculadora de Área e Volume", None))
            self.ui.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Área - Quadrado", None))
            self.ui.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Área - Retângulo", None))
            self.ui.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Área - Círculo", None))
            self.ui.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"Área - Triângulo Isósceles", None))
            self.ui.comboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"Área - Triângulo Escaleno", None))
            self.ui.comboBox_2.setItemText(5, QCoreApplication.translate("MainWindow", u"Área - Triângulo Equilátero", None))
            self.ui.comboBox_2.setItemText(6, QCoreApplication.translate("MainWindow", u"Área - Pentágono", None))
            self.ui.comboBox_2.setItemText(7, QCoreApplication.translate("MainWindow", u"Área - Hexágono", None))
            self.ui.comboBox_2.setItemText(8, QCoreApplication.translate("MainWindow", u"Área - Heptágono", None))
            self.ui.comboBox_2.setItemText(9, QCoreApplication.translate("MainWindow", u"Área - Octógono", None))
            self.ui.comboBox_2.setItemText(10, QCoreApplication.translate("MainWindow", u"Área - Enenágono", None))
            self.ui.comboBox_2.setItemText(11, QCoreApplication.translate("MainWindow", u"Área - Decágono", None))
            self.ui.comboBox_2.setItemText(12, QCoreApplication.translate("MainWindow", u"Área - Undecágono", None))
            self.ui.comboBox_2.setItemText(13, QCoreApplication.translate("MainWindow", u"Área - Dodecágono", None))
            self.ui.comboBox_2.setItemText(14, QCoreApplication.translate("MainWindow", u"Área - Tridecágono", None))
            self.ui.comboBox_2.setItemText(15, QCoreApplication.translate("MainWindow", u"Área - Tetradecágono", None))
            self.ui.comboBox_2.setItemText(16, QCoreApplication.translate("MainWindow", u"Área - Pentadecágono", None))
            self.ui.comboBox_2.setItemText(17, QCoreApplication.translate("MainWindow", u"Área - Trapézio", None))
            self.ui.comboBox_2.setItemText(18, QCoreApplication.translate("MainWindow", u"Área - Elipse", None))
            self.ui.comboBox_2.setItemText(19, QCoreApplication.translate("MainWindow", u"Área - Poliomino", None))
            self.ui.comboBox_2.setItemText(20, QCoreApplication.translate("MainWindow", u"Área - Estrela", None))
            self.ui.comboBox_2.setItemText(21, QCoreApplication.translate("MainWindow", u"Área - Semicírculo", None))
            self.ui.comboBox_2.setItemText(22, QCoreApplication.translate("MainWindow", u"Área - Esquicírculo", None))
            self.ui.comboBox_2.setItemText(23, QCoreApplication.translate("MainWindow", u"Área - Paralelogramo", None))
            self.ui.comboBox_2.setItemText(24, QCoreApplication.translate("MainWindow", u"Área - Anel", None))
            self.ui.comboBox_2.setItemText(25, QCoreApplication.translate("MainWindow", u"Área - Pipa", None))
            self.ui.comboBox_2.setItemText(26, QCoreApplication.translate("MainWindow", u"Área - Losango", None))
            self.ui.comboBox_2.setItemText(27, QCoreApplication.translate("MainWindow", u"Volume - Cubo", None))
            self.ui.comboBox_2.setItemText(28, QCoreApplication.translate("MainWindow", u"Volume - Prisma Retangular", None))
            self.ui.comboBox_2.setItemText(29, QCoreApplication.translate("MainWindow", u"Volume - Esfera", None))
            self.ui.comboBox_2.setItemText(30, QCoreApplication.translate("MainWindow", u"Volume - Cilindro", None))
            self.ui.comboBox_2.setItemText(31, QCoreApplication.translate("MainWindow", u"Volume - Cone", None))
            self.ui.comboBox_2.setItemText(32, QCoreApplication.translate("MainWindow", u"Volume - Dodecaedro", None))
            self.ui.comboBox_2.setItemText(33, QCoreApplication.translate("MainWindow", u"Volume - Prisma Triangular Isósceles", None))
            self.ui.comboBox_2.setItemText(34, QCoreApplication.translate("MainWindow", u"Volume - Prisma Triangular Escaleno", None))
            self.ui.comboBox_2.setItemText(35, QCoreApplication.translate("MainWindow", u"Volume - Prisma Triangular Equilátero", None))
            self.ui.comboBox_2.setItemText(36, QCoreApplication.translate("MainWindow", u"Volume - Hemisfério", None))
            self.ui.comboBox_2.setItemText(37, QCoreApplication.translate("MainWindow", u"Volume - Tórax", None))
            self.ui.comboBox_2.setItemText(38, QCoreApplication.translate("MainWindow", u"Volume - Rombicosidodecaedro", None))
            self.ui.comboBox_2.setItemText(39, QCoreApplication.translate("MainWindow", u"Volume - Cubo Truncado", None))
            self.ui.comboBox_2.setItemText(40, QCoreApplication.translate("MainWindow", u"Volume - Cápsula", None))
            self.ui.comboBox_2.setItemText(41, QCoreApplication.translate("MainWindow", u"Volume - Tetraedro", None))
            self.ui.comboBox_2.setItemText(42, QCoreApplication.translate("MainWindow", u"Volume - Octaedro", None))
            self.ui.comboBox_2.setItemText(43, QCoreApplication.translate("MainWindow", u"Volume - Icosaedro", None))
            self.ui.comboBox_2.setItemText(44, QCoreApplication.translate("MainWindow", u"Volume - Pirâmide Triangular Isósceles", None))
            self.ui.comboBox_2.setItemText(45, QCoreApplication.translate("MainWindow", u"Volume - Pirâmide Triangular Escaleno", None))
            self.ui.comboBox_2.setItemText(46, QCoreApplication.translate("MainWindow", u"Volume - Pirâmide Triangular Equilátero", None))
            self.ui.comboBox_2.setItemText(47, QCoreApplication.translate("MainWindow", u"Volume - Pirâmide Quadrangular", None))
            self.ui.comboBox_2.setItemText(48, QCoreApplication.translate("MainWindow", u"Volume - Pirâmide Pentagonal", None))
            self.ui.comboBox_2.setItemText(49, QCoreApplication.translate("MainWindow", u"Volume - Pirâmide Hexagonal", None))
            self.ui.comboBox_2.setItemText(50, QCoreApplication.translate("MainWindow", u"Volume - Pirâmide Heptagonal", None))
            self.ui.comboBox_2.setItemText(51, QCoreApplication.translate("MainWindow", u"Volume - Pirâmide Octagonal", None))
            self.ui.comboBox_2.setItemText(52, QCoreApplication.translate("MainWindow", u"Volume - Pirâmide Nonagonal", None))
            self.ui.comboBox_2.setItemText(53, QCoreApplication.translate("MainWindow", u"Volume - Pirâmide Decagonal", None))
            self.ui.comboBox_2.setItemText(54, QCoreApplication.translate("MainWindow", u"Volume - Pirâmide Prismática Estrelada", None))
            self.ui.comboBox_2.setItemText(55, QCoreApplication.translate("MainWindow", u"Volume - Bipirâmide Triangular Isósceles", None))
            self.ui.comboBox_2.setItemText(56, QCoreApplication.translate("MainWindow", u"Volume - Bipirâmide Triangular Escaleno", None))
            self.ui.comboBox_2.setItemText(57, QCoreApplication.translate("MainWindow", u"Volume - Bipirâmide Triangular Equilátero", None))
            self.ui.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"Polegadas", None))
            self.ui.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"Pés", None))
            self.ui.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"Jardas", None))
            self.ui.comboBox_3.setItemText(3, QCoreApplication.translate("MainWindow", u"Milhas", None))
            self.ui.comboBox_3.setItemText(4, QCoreApplication.translate("MainWindow", u"Milímetros", None))
            self.ui.comboBox_3.setItemText(5, QCoreApplication.translate("MainWindow", u"Centímetros", None))
            self.ui.comboBox_3.setItemText(6, QCoreApplication.translate("MainWindow", u"Metros", None))
            self.ui.comboBox_3.setItemText(7, QCoreApplication.translate("MainWindow", u"Quilômetros", None))
            self.ui.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Resolver", ))
            self.ui.label.setText(QCoreApplication.translate("MainWindow", u"Forma:", None))
            self.ui.label_2.setText(QCoreApplication.translate("MainWindow", u"Fórmula:", None))
            self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Resposta", None))
            self.ui.label_6.setText(QCoreApplication.translate("MainWindow", u"Entrada 3", None))
            self.ui.label_9.setText(QCoreApplication.translate("MainWindow", u"Entrada 4", None))
            self.ui.Input2.setText(QCoreApplication.translate("MainWindow", u"Entrada 2", None))
            self.ui.Input1.setText(QCoreApplication.translate("MainWindow", u"Entrada 1", None))
        elif langu == "Português (Portugal)":
            self.ui.title.setText(QCoreApplication.translate("MainWindow", u"Calculadora de Área e Volume", None))
            self.ui.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Área - Quadrado", None))
            self.ui.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Área - Retângulo", None))
            self.ui.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Área - Círculo", None))
            self.ui.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"Área - Triângulo Isósceles", None))
            self.ui.comboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"Área - Triângulo Escaleno", None))
            self.ui.comboBox_2.setItemText(5, QCoreApplication.translate("MainWindow", u"Área - Triângulo Equilátero", None))
            self.ui.comboBox_2.setItemText(6, QCoreApplication.translate("MainWindow", u"Área - Pentágono", None))
            self.ui.comboBox_2.setItemText(7, QCoreApplication.translate("MainWindow", u"Área - Hexágono", None))
            self.ui.comboBox_2.setItemText(8, QCoreApplication.translate("MainWindow", u"Área - Heptágono", None))
            self.ui.comboBox_2.setItemText(9, QCoreApplication.translate("MainWindow", u"Área - Octógono", None))
            self.ui.comboBox_2.setItemText(10, QCoreApplication.translate("MainWindow", u"Área - Enenágono", None))
            self.ui.comboBox_2.setItemText(11, QCoreApplication.translate("MainWindow", u"Área - Decágono", None))
            self.ui.comboBox_2.setItemText(12, QCoreApplication.translate("MainWindow", u"Área - Undecágono", None))
            self.ui.comboBox_2.setItemText(13, QCoreApplication.translate("MainWindow", u"Área - Dodecágono", None))
            self.ui.comboBox_2.setItemText(14, QCoreApplication.translate("MainWindow", u"Área - Tridecágono", None))
            self.ui.comboBox_2.setItemText(15, QCoreApplication.translate("MainWindow", u"Área - Tetradecágono", None))
            self.ui.comboBox_2.setItemText(16, QCoreApplication.translate("MainWindow", u"Área - Pentadecágono", None))
            self.ui.comboBox_2.setItemText(17, QCoreApplication.translate("MainWindow", u"Área - Trapézio", None))
            self.ui.comboBox_2.setItemText(18, QCoreApplication.translate("MainWindow", u"Área - Elipse", None))
            self.ui.comboBox_2.setItemText(19, QCoreApplication.translate("MainWindow", u"Área - Poliomino", None))
            self.ui.comboBox_2.setItemText(20, QCoreApplication.translate("MainWindow", u"Área - Estrela", None))
            self.ui.comboBox_2.setItemText(21, QCoreApplication.translate("MainWindow", u"Área - Semicírculo", None))
            self.ui.comboBox_2.setItemText(22, QCoreApplication.translate("MainWindow", u"Área - Esquicírculo", None))
            self.ui.comboBox_2.setItemText(23, QCoreApplication.translate("MainWindow", u"Área - Paralelogramo", None))
            self.ui.comboBox_2.setItemText(24, QCoreApplication.translate("MainWindow", u"Área - Anel", None))
            self.ui.comboBox_2.setItemText(25, QCoreApplication.translate("MainWindow", u"Área - Pipa", None))
            self.ui.comboBox_2.setItemText(26, QCoreApplication.translate("MainWindow", u"Área - Losango", None))
            self.ui.comboBox_2.setItemText(27, QCoreApplication.translate("MainWindow", u"Volume - Cubo", None))
            self.ui.comboBox_2.setItemText(28, QCoreApplication.translate("MainWindow", u"Volume - Prisma Retangular", None))
            self.ui.comboBox_2.setItemText(29, QCoreApplication.translate("MainWindow", u"Volume - Esfera", None))
            self.ui.comboBox_2.setItemText(30, QCoreApplication.translate("MainWindow", u"Volume - Cilindro", None))
            self.ui.comboBox_2.setItemText(31, QCoreApplication.translate("MainWindow", u"Volume - Cone", None))
            self.ui.comboBox_2.setItemText(32, QCoreApplication.translate("MainWindow", u"Volume - Dodecaedro", None))
            self.ui.comboBox_2.setItemText(33, QCoreApplication.translate("MainWindow", u"Volume - Prisma Triangular Isósceles", None))
            self.ui.comboBox_2.setItemText(34, QCoreApplication.translate("MainWindow", u"Volume - Prisma Triangular Escaleno", None))
            self.ui.comboBox_2.setItemText(35, QCoreApplication.translate("MainWindow", u"Volume - Prisma Triangular Equilátero", None))
            self.ui.comboBox_2.setItemText(36, QCoreApplication.translate("MainWindow", u"Volume - Hemisfério", None))
            self.ui.comboBox_2.setItemText(37, QCoreApplication.translate("MainWindow", u"Volume - Tórax", None))
            self.ui.comboBox_2.setItemText(38, QCoreApplication.translate("MainWindow", u"Volume - Rombicosidodecaedro", None))
            self.ui.comboBox_2.setItemText(39, QCoreApplication.translate("MainWindow", u"Volume - Cubo Truncado", None))
            self.ui.comboBox_2.setItemText(40, QCoreApplication.translate("MainWindow", u"Volume - Cápsula", None))
            self.ui.comboBox_2.setItemText(41, QCoreApplication.translate("MainWindow", u"Volume - Tetraedro", None))
            self.ui.comboBox_2.setItemText(42, QCoreApplication.translate("MainWindow", u"Volume - Octaedro", None))
            self.ui.comboBox_2.setItemText(43, QCoreApplication.translate("MainWindow", u"Volume - Icosaedro", None))
            self.ui.comboBox_2.setItemText(44, QCoreApplication.translate("MainWindow", u"Volume - Pirâmide Triangular Isósceles", None))
            self.ui.comboBox_2.setItemText(45, QCoreApplication.translate("MainWindow", u"Volume - Pirâmide Triangular Escaleno", None))
            self.ui.comboBox_2.setItemText(46, QCoreApplication.translate("MainWindow", u"Volume - Pirâmide Triangular Equilátero", None))
            self.ui.comboBox_2.setItemText(47, QCoreApplication.translate("MainWindow", u"Volume - Pirâmide Quadrangular", None))
            self.ui.comboBox_2.setItemText(48, QCoreApplication.translate("MainWindow", u"Volume - Pirâmide Pentagonal", None))
            self.ui.comboBox_2.setItemText(49, QCoreApplication.translate("MainWindow", u"Volume - Pirâmide Hexagonal", None))
            self.ui.comboBox_2.setItemText(50, QCoreApplication.translate("MainWindow", u"Volume - Pirâmide Heptagonal", None))
            self.ui.comboBox_2.setItemText(51, QCoreApplication.translate("MainWindow", u"Volume - Pirâmide Octogonal", None))
            self.ui.comboBox_2.setItemText(52, QCoreApplication.translate("MainWindow", u"Volume - Pirâmide Nonagonal", None))
            self.ui.comboBox_2.setItemText(53, QCoreApplication.translate("MainWindow", u"Volume - Pirâmide Decagonal", None))
            self.ui.comboBox_2.setItemText(54, QCoreApplication.translate("MainWindow", u"Volume - Pirâmide Prismática Estrelada", None))
            self.ui.comboBox_2.setItemText(55, QCoreApplication.translate("MainWindow", u"Volume - Bipirâmide Triangular Isósceles", None))
            self.ui.comboBox_2.setItemText(56, QCoreApplication.translate("MainWindow", u"Volume - Bipirâmide Triangular Escaleno", None))
            self.ui.comboBox_2.setItemText(57, QCoreApplication.translate("MainWindow", u"Volume - Bipirâmide Triangular Equilátero", None))
            self.ui.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"Polegadas", None))
            self.ui.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"Pés", None))
            self.ui.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"Jardas", None))
            self.ui.comboBox_3.setItemText(3, QCoreApplication.translate("MainWindow", u"Milhas", None))
            self.ui.comboBox_3.setItemText(4, QCoreApplication.translate("MainWindow", u"Milímetros", None))
            self.ui.comboBox_3.setItemText(5, QCoreApplication.translate("MainWindow", u"Centímetros", None))
            self.ui.comboBox_3.setItemText(6, QCoreApplication.translate("MainWindow", u"Metros", None))
            self.ui.comboBox_3.setItemText(7, QCoreApplication.translate("MainWindow", u"Quilómetros", None))
            self.ui.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Resolver", ))
            self.ui.label.setText(QCoreApplication.translate("MainWindow", u"Forma:", None))
            self.ui.label_2.setText(QCoreApplication.translate("MainWindow", u"Fórmula:", None))
            self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Resposta", None))
            self.ui.label_6.setText(QCoreApplication.translate("MainWindow", u"Entrada 3", None))
            self.ui.label_9.setText(QCoreApplication.translate("MainWindow", u"Entrada 4", None))
            self.ui.Input2.setText(QCoreApplication.translate("MainWindow", u"Entrada 2", None))
            self.ui.Input1.setText(QCoreApplication.translate("MainWindow", u"Entrada 1", None))
        elif langu == "English":
            self.ui.title.setText(QCoreApplication.translate("MainWindow", u"Area and Volume Calculator", None))
            self.ui.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"English", None))
            self.ui.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Espa\u00f1ol", None))
            self.ui.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Fran\u00e7ais", None))
            self.ui.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\u0420\u0443\u0441\u0441\u043a\u0438\u0439", None))
            self.ui.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Deutsch", None))
            self.ui.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"\u05e2\u05d1\u05e8\u05d9\u05ea", None))
            self.ui.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"\u307b\u3093 ", None))
            self.ui.comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Portugu\u00eas", None))

            self.ui.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Area - Square", None))
            self.ui.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Area - Rectangle", None))
            self.ui.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Area - Circle", None))
            self.ui.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"Area - Isosceles triangle", None))
            self.ui.comboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"Area - Scalene triangle", None))
            self.ui.comboBox_2.setItemText(5, QCoreApplication.translate("MainWindow", u"Area - Equilateral triangle", None))
            self.ui.comboBox_2.setItemText(6, QCoreApplication.translate("MainWindow", u"Area - Pentagon", None))
            self.ui.comboBox_2.setItemText(7, QCoreApplication.translate("MainWindow", u"Area - Hexagon", None))
            self.ui.comboBox_2.setItemText(8, QCoreApplication.translate("MainWindow", u"Area - Heptagon", None))
            self.ui.comboBox_2.setItemText(9, QCoreApplication.translate("MainWindow", u"Area - Octagon", None))
            self.ui.comboBox_2.setItemText(10, QCoreApplication.translate("MainWindow", u"Area - Nonagon", None))
            self.ui.comboBox_2.setItemText(11, QCoreApplication.translate("MainWindow", u"Area - Decagon", None))
            self.ui.comboBox_2.setItemText(12, QCoreApplication.translate("MainWindow", u"Area - Undecagon", None))
            self.ui.comboBox_2.setItemText(13, QCoreApplication.translate("MainWindow", u"Area - Dodecagon", None))
            self.ui.comboBox_2.setItemText(14, QCoreApplication.translate("MainWindow", u"Area - Tridecagon", None))
            self.ui.comboBox_2.setItemText(15, QCoreApplication.translate("MainWindow", u"Area - Tetradecagon", None))
            self.ui.comboBox_2.setItemText(16, QCoreApplication.translate("MainWindow", u"Area - Pentadecagon", None))
            self.ui.comboBox_2.setItemText(17, QCoreApplication.translate("MainWindow", u"Area - Trapezoid", None))
            self.ui.comboBox_2.setItemText(18, QCoreApplication.translate("MainWindow", u"Area - Ellipse", None))
            self.ui.comboBox_2.setItemText(19, QCoreApplication.translate("MainWindow", u"Area - Polyomino", None))
            self.ui.comboBox_2.setItemText(20, QCoreApplication.translate("MainWindow", u"Area - Star", None))
            self.ui.comboBox_2.setItemText(21, QCoreApplication.translate("MainWindow", u"Area - Semicircle", None))
            self.ui.comboBox_2.setItemText(22, QCoreApplication.translate("MainWindow", u"Area - Squircle", None))
            self.ui.comboBox_2.setItemText(23, QCoreApplication.translate("MainWindow", u"Area - Parallelogram", None))
            self.ui.comboBox_2.setItemText(24, QCoreApplication.translate("MainWindow", u"Area - Annulus", None))
            self.ui.comboBox_2.setItemText(25, QCoreApplication.translate("MainWindow", u"Area - Kite", None))
            self.ui.comboBox_2.setItemText(26, QCoreApplication.translate("MainWindow", u"Area - Rhombus", None))
            self.ui.comboBox_2.setItemText(27, QCoreApplication.translate("MainWindow", u"Volume - Cube", None))
            self.ui.comboBox_2.setItemText(28, QCoreApplication.translate("MainWindow", u"Volume - Rectangular prism", None))
            self.ui.comboBox_2.setItemText(29, QCoreApplication.translate("MainWindow", u"Volume - Sphere", None))
            self.ui.comboBox_2.setItemText(30, QCoreApplication.translate("MainWindow", u"Volume - Cylinder", None))
            self.ui.comboBox_2.setItemText(31, QCoreApplication.translate("MainWindow", u"Volume - Cone", None))
            self.ui.comboBox_2.setItemText(32, QCoreApplication.translate("MainWindow", u"Volume - Dodecahedron", None))
            self.ui.comboBox_2.setItemText(33, QCoreApplication.translate("MainWindow", u"Volume - Isosceles triangular prism", None))
            self.ui.comboBox_2.setItemText(34, QCoreApplication.translate("MainWindow", u"Volume - Scalene triangular prism", None))
            self.ui.comboBox_2.setItemText(35, QCoreApplication.translate("MainWindow", u"Volume - Equilateral triangular prism", None))
            self.ui.comboBox_2.setItemText(36, QCoreApplication.translate("MainWindow", u"Volume - Hemisphere", None))
            self.ui.comboBox_2.setItemText(37, QCoreApplication.translate("MainWindow", u"Volume - Torus", None))
            self.ui.comboBox_2.setItemText(38, QCoreApplication.translate("MainWindow", u"Volume - Rhombicosidodecahedron", None))
            self.ui.comboBox_2.setItemText(39, QCoreApplication.translate("MainWindow", u"Volume - Snub cube", None))
            self.ui.comboBox_2.setItemText(40, QCoreApplication.translate("MainWindow", u"Volume - Capsule", None))
            self.ui.comboBox_2.setItemText(41, QCoreApplication.translate("MainWindow", u"Volume - Tetrahedron", None))
            self.ui.comboBox_2.setItemText(42, QCoreApplication.translate("MainWindow", u"Volume - Octahedron", None))
            self.ui.comboBox_2.setItemText(43, QCoreApplication.translate("MainWindow", u"Volume - Icosahedron", None))
            self.ui.comboBox_2.setItemText(44, QCoreApplication.translate("MainWindow", u"Volume - Isosceles triangular pyramid", None))
            self.ui.comboBox_2.setItemText(45, QCoreApplication.translate("MainWindow", u"Volume - Scalene triangular pyramid", None))
            self.ui.comboBox_2.setItemText(46, QCoreApplication.translate("MainWindow", u"Volume - Equilateral triangular pyramid", None))
            self.ui.comboBox_2.setItemText(47, QCoreApplication.translate("MainWindow", u"Volume - Square pyramid", None))
            self.ui.comboBox_2.setItemText(48, QCoreApplication.translate("MainWindow", u"Volume - Pentagonal pyramid", None))
            self.ui.comboBox_2.setItemText(49, QCoreApplication.translate("MainWindow", u"Volume - Hexagonal pyramid", None))
            self.ui.comboBox_2.setItemText(50, QCoreApplication.translate("MainWindow", u"Volume - Heptagonal pyramid", None))
            self.ui.comboBox_2.setItemText(51, QCoreApplication.translate("MainWindow", u"Volume - Octagonal pyramid", None))
            self.ui.comboBox_2.setItemText(52, QCoreApplication.translate("MainWindow", u"Volume - Nonagonal pyramid", None))
            self.ui.comboBox_2.setItemText(53, QCoreApplication.translate("MainWindow", u"Volume - Decagonal pyramid", None))
            self.ui.comboBox_2.setItemText(54, QCoreApplication.translate("MainWindow", u"Volume - Star prism pyramid", None))
            self.ui.comboBox_2.setItemText(55, QCoreApplication.translate("MainWindow", u"Volume - Isosceles triangular bipyramid", None))
            self.ui.comboBox_2.setItemText(56, QCoreApplication.translate("MainWindow", u"Volume - Scalene triangular bipyramid", None))
            self.ui.comboBox_2.setItemText(57, QCoreApplication.translate("MainWindow", u"Volume - Equilateral triangular bipyramid", None))

            self.ui.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"Inches", None))
            self.ui.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"Feet", None))
            self.ui.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"Yards", None))
            self.ui.comboBox_3.setItemText(3, QCoreApplication.translate("MainWindow", u"Miles", None))
            self.ui.comboBox_3.setItemText(4, QCoreApplication.translate("MainWindow", u"Millimeters", None))
            self.ui.comboBox_3.setItemText(5, QCoreApplication.translate("MainWindow", u"Centimeters", None))
            self.ui.comboBox_3.setItemText(6, QCoreApplication.translate("MainWindow", u"Meters", None))
            self.ui.comboBox_3.setItemText(7, QCoreApplication.translate("MainWindow", u"Kilometers", None))

            self.ui.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Solve", ))
            self.ui.label.setText(QCoreApplication.translate("MainWindow", u"Shape:", None))
            self.ui.label_2.setText(QCoreApplication.translate("MainWindow", u"Formula:", None))
            self.ui.answer.setText(QCoreApplication.translate("MainWindow", u"Answer", None))
            self.ui.label_6.setText(QCoreApplication.translate("MainWindow", u"Input3", None))
            self.ui.label_9.setText(QCoreApplication.translate("MainWindow", u"Input4", None))
            self.ui.Input2.setText(QCoreApplication.translate("MainWindow", u"Input2", None))
            self.ui.Inpu1.setText(QCoreApplication.translate("MainWindow", u"Input1", None))
        print("Lang updated to:", lang)

        
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
    