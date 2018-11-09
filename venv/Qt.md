# Pyqt5
> 写在前面

> 本文原作者是追逐阳光的风，文章源于CSDN。
> 作者写得相当详细，我在原文的基础上进行了一部分的删改润色。作者的环境是Python3.35，事实证明Python2.7也能跑通。

[toc]
## Pyqt5系列(一)-Pyqt5的安装
由于在实际的工作中需要使用到python来进行GUI的开发，基于python的GUI开发，只是去考虑具体使用依赖那个GUI库来进行开发。

### GUI库的选择
1. TKinter，python配备的标准gui库，但是功能比较弱，似乎只适合开发非常简单的界面。
2. Wxpython，目前官方网站还没有release针对python3.0以上版本的库，虽然在国外的博客上有针对python3的版本。
3. Pyqt，Pyqt基于QT,在GUI开发上可以参考QT的开发 。

对比了Tkinter,Wxpython,Pyqt之后，选择使用Pyqt来进行GUI的开发，PyQt基于GPL许可开发。
### PyQt安装
整体安装的步骤比较简单，首先下载与自己python版本和开发环境一致的PyQt版本。
1. 开发环境：
> python3.35
> win7 32bit

2. 官网下载：
官网上之后对应的source package。需要自己编译生成。
3. OSDN下载：
OSDN上罗列了所有released的PyQt安装程序，根据开发环境下载了PyQt5-5.2.1-gpl-Py3.3-Qt5.2.0-x32.exe 安装程序。

##### Note
> 1. 下载PyQt时注意选择匹配的Python版本和系统的位数；
> 2、直接通过exe文件安装PyQt，Pip安装的方式比较复杂；

### 功能验证
安装之后简单写个测试程序验证一下
```python
#!/user/bin/python3
#-*- coding:utf-8 -*-
'''
Creat a simple window
'''
__author__ = 'Tony Zhu'

import sys
from PyQt5.QtWidgets import QWidget, QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.show()
    w.setWindowTitle("Hello PyQt5")
    sys.exit(app.exec_())
```
运行之后会直接显示一个标题为“Hello PyQt5”的空白窗口。

---
## Pyqt5系列(二)-第一个PyQt程序
通过下面的一个PyQt5简单例子，来简单了解一下关于如何创建PyQt5的。具体代码如下：
```python
#-*- coding:utf-8 -*-
'''
Frist PyQt5 program
'''
__author__ = 'Tony Zhu'

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QPushButton, QLineEdit, QVBoxLayout,QMessageBox
import sys

class ShowWindow(QWidget):

    def __init__(self):
        super(ShowWindow,self).__init__()      
        self.initUI()

    def initUI(self):
        self.inputLabel = QLabel("Input your text")
        self.editLine = QLineEdit()
        self.printButton = QPushButton("Print")
        self.clearButton = QPushButton("Clear")

        self.printButton.clicked.connect(self.printText)
        self.clearButton.clicked.connect(self.clearText)

        inputLayout = QHBoxLayout()
        inputLayout.addWidget(self.inputLabel)
        inputLayout.addWidget(self.editLine)

        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.printButton)
        buttonLayout.addWidget(self.clearButton)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(inputLayout)
        mainLayout.addLayout(buttonLayout)

        self.setLayout(mainLayout)
        self.setWindowTitle('FristWindow')
        self.show()
    def printText(self):
        text = self.editLine.text()

        if text == '':
            QMessageBox.information(self, "Empty Text",
                                    "Please enter the letter.")
        else :
            QMessageBox.information(self, "Print Success",
                                    "Text: %s" % text)
    def clearText(self):
        text = self.editLine.text()

        if text == '':
            return
        else :
            self.editLine.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ShowWindow()
    sys.exit(app.exec_())
```
结合代码和运行的结果，分析代码：
Line7~8：
```python
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QPushButton, QLineEdit, QVBoxLayout,QMessageBox
import sys
```
导入了程序运行所必须的模块

Line10：
```python
class ShowWindow(QWidget):
```
创建一个ShowWindow类继承QWidget，其中PyQt中非常重要的通用窗口类，是所有用户界面对象的基类，所有和用户界面相关的控件类都是继承自QWidger类。

Line12~14：
```python
def __init__(self):
        super(ShowWindow,self).__init__()      
        self.initUI()
```
定义了ShowWindow类的构造函数 init，由于ShowWindow继承自QWidgert类，因此在构造函数中调用父类QWidget的构造函数super.init()。
同时在构造函数中调用自定义的初始化函数initUI()，在该函数中初始化GUI中所需各个控件。

Line17~20：
```python
self.inputLabel = QLabel("Input your text")
self.editLine = QLineEdit()
self.printButton = QPushButton("Print")
self.clearButton = QPushButton("Clear")
```
创建成员：一个标签（inputLabel），输入框（editLine），两个按钮（printButton ，clearButton）

Line22~23：
```python
self.printButton.clicked.connect(self.printText)
self.clearButton.clicked.connect(self.clearText)
```
printButton和clearButton点击事件处理的逻辑：点击printButton之后会调用自定义函数printText()中的处理逻辑；点击clearButton之后调用自定义函数clearText()中的处理逻辑。通过connect()方法将点击事件和处理逻辑关联起来。

这个涉及到PyQt信号与槽的概念，信号和槽用于对象之间的通信。当指定事件发生，一个事件信号会被发射。槽可以被任何Python脚本调用。当和槽连接的信号被发射时，槽会被调用。有关信号与槽的概念，在后续的文章中会专门讲解。

Line25~26:
```python
inputLayout = QHBoxLayout()
inputLayout.addWidget(self.inputLabel)
inputLayout.addWidget(self.editLine)
```
创建一个inputLayout的水平布局(QHBoxLayout)，在inputLayout中添加已定义的控件inputLabel和editLine。QHBoxLayout让添加的控件水平排布

Line29~31:
```python
buttonLayout = QHBoxLayout()
buttonLayout.addWidget(self.printButton)
buttonLayout.addWidget(self.clearButton)
```
同上创建一个buttonLayout 的水平布局(QHBoxLayout)，在buttonLayout 中添加printButton和clearButton

Line33~35：
```python
mainLayout = QVBoxLayout()
mainLayout.addLayout(inputLayout)
mainLayout.addLayout(buttonLayout)
```
创建一个mainLayout 的垂直布局(QVBoxLayout)，在mainLayout 中嵌套子布局inputLayout和buttonLayout。

通过如下的布局图，进一步了解一下该程序中layout是如何布局的。


有layout的概念，在后续的文章中会专门讲解。

Line37：
```python
self.setLayout(mainLayout)
```
通过将setLayout()方法，将mainLayout设置为窗口layout。

Line38：
```python
self.setWindowTitle('FristWindow')
```
通过setWindowTitle()方法设置窗口的标题

Line39：
```python
self.show()
```
通过show()方法将窗口显示到屏幕上

Line40~48：
```python
    def printText(self):
        text = self.editLine.text()

        if text == '':
            QMessageBox.information(self, "Empty Text",
                                    "Please enter the letter.")
        else :
            QMessageBox.information(self, "Print Success",
                                    "Text: %s" % text)
```

定义了处理printButton点击信号的槽函数，当editLine输入框中的文本为空的时候弹出消息框(QMessageBox)，提示“Please enter the letter.”；当editLine输入框中的文本不为空时候弹出消息框，显示editLine中的文本。

触发槽函数printText()之后，当editLine输入框内容为空时界面显示如下：


Line49~55:
```python
    def clearText(self):
        text = self.editLine.text()

        if text == '':
            return
        else :
            self.editLine.clear()
```
定义了处理clearButton点击信号的槽函数,清空editLine输入框中的文本信息。

Line 57~60：
```python
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ShowWindow()
    sys.exit(app.exec_())
```
程序运行的入口函数类似C语言中的main()方法。

app = QApplication(sys.argv)，每一个pyqt程序必须创建一个application对象，sys.argv是命令行参数，可以通过命令启动的时候传递参数。

ex = ShowWindow()，创建ShowWindow对象。

sys.exit(app.exec_())，app.exec_() 事件处理开始，进入程序主循环。主循环等待时间，并把事件发送给指定处理的任务中。当调用app.exit()或者程序因为各种原因被破坏后，使用sys.exit()关闭程序，并释放内存资源。

到此为止，第一个PyQt程序分析结束，可能会存在输入框，布局，等各类控件如何使用，如何确定对应的控件在那个模块中？在后续的文章中会详细进行介绍。

---
## Pyqt5系列(三)-基本界面组件之Button(1)
> Button，作为界面中触发动作请求或者命令的一种方式，作为与用户进行的交互操作。PyQt中的Button根据不同的使用场景划分为不同的表现形式。Button的基类QAbstractButton，提供button的通用性功能，此类为抽象类，从因此不能实例化，由其他的Button类继承来实现不同的功能，不同的表现形式。 常见的Button包括，QPushButton，QToolButton，QRadioButton及QCheckBox。这些Button类均继承自QAbstractButton类，根据各自的使用场景通过图形展现出来。

---
### QAbstractButton抽象类
QAbstractButton作为抽象类，提供button的通用功能，可按按钮（push button）和可选择按钮（checkable button）。可选择按钮实现有QRadioButton和QCheckBox；可按按钮实现有QPushButton和QToolButton。 任何一种button可以显示带文本(.setText()方法设置文本)和图标(.setIcon()设置图标)的标签。

QAbstractButton 提供的状态： 1、isDown() 提示button是否按下 2、isChecked()提示button是否已经标记 3、isEnable()提示button是否可以被用户点击 4、isCheckAble()提示button是否为可标记 5、setAutoRepeat()设置button是否在用户长按按钮的时候可以自动重复执行。

QAbstractButton 提供的信号： 1、pressed(),当鼠标在button上并点击左键的时候 触发信号 2、released(),当鼠标左键被释放的时候触发信号 3、clicked(),当鼠标首次按下，然后释放，或者快捷键被释放的时候触发信号 4、toggled(),当button的标记状态发生改变的时候触发信号

接下来会针对每一种button进行介绍：

---
### QPushButton
```python
class QPushButton(QAbstractButton)
 |  QPushButton(QWidget parent=None)
 |  QPushButton(str, QWidget parent=None)
 |  QPushButton(QIcon, str, QWidget parent=None)
```
由此可见QPushButton继承自QAbstractButton,是一种command按钮。点击执行一些命令，或者响应一些问题。常见的诸如“确认”，“申请”，“取消”，“关闭”，“是”，“否”等按钮。 Command Button经常通过文本来描述执行的动作。有时候我们也会通过快捷键来执行对应按钮的命令。

通过一个示例对QPushButton来进行说明：

```python
'''
PushButton
'''
__author__ = 'Tony Zhu'

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import sys

class PushButton(QWidget):
    def __init__(self):
        super(PushButton,self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("PushButton")
        self.setGeometry(400,400,300,260)

        self.closeButton = QPushButton(self)
        self.closeButton.setText("Close")          
        self.closeButton.setIcon(QIcon("close.png"))
        self.closeButton.setShortcut('Ctrl+D')  
        self.closeButton.clicked.connect(self.close)
        self.closeButton.setToolTip("Close the widget")
        self.closeButton.move(100,100)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PushButton()
    ex.show()
    sys.exit(app.exec_())
```
##### 控件说明
| 控件类型    | 控件名称    | 文本  | 图标      |
| ----------- | ----------- | ----- | --------- |
| QPushButton | closeButton | Close | close.png |
##### 示例说明
名称为“Close”的 Buttton，点击该Button之后关闭该窗口。或者通过快捷键“Ctrl+C”的快捷方式亦可关闭该窗口。
##### 代码分析
其他代码部分可以参考上一篇《Pyqt5系列(二 )-第一个PyQt程序》中的说明。

L21~22：
```python
self.closeButton.setText("Close")          #text
self.closeButton.setIcon(QIcon("close.png")) #icon
```
setText()方法，设定button的文本 setIcon()方法，设定button的图标 关于button 文本和图标的显示，也可以通过QPushButton的构造函数，在创建对象实例的时候通过参数直接设定。 | QPushButton(str, QWidget parent=None) | QPushButton(QIcon, str, QWidget parent=None)

L23：
```python
self.closeButton.setShortcut('Ctrl+D')  
```
给closeButton设定快捷键方式，即通过Ctrl+D实现与点击closeButton一样的功能。

L24:
```python
self.closeButton.clicked.connect(self.close)
```
closeButton点击事件处理的逻辑：在点击closeButton之后调用QWidget的close()方法。通过connect()方法将点击事件和处理逻辑关联起来 。

L25：
```python
self.closeButton.setToolTip("Close the widget")
```
setToolTip()设定提示信息，当鼠标移动到button上时显示”Close the widget”提示信息。

---
### QToolButton：

```python
class QToolButton(QAbstractButton)
 |  QToolButton(QWidget parent=None)
```
同理QToolButton继承自QAbstractButton。QToolButton就是工具操作相关的按钮,通常和QToolBar搭配使用。QToolButton通常不显示文本，而显示图标QIcon。一般QToolButton会在QToolBar：：addAction时创建，或者已经存在的action添加到QToolBar时创建。

通过一个示例对QToolButton来进行说明：
``` python
'''
ToolButton
'''
__author__ = 'Tony Zhu'

from PyQt5.QtWidgets import QApplication, QWidget, QToolButton, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import sys

class ToolButton(QMainWindow):
    def __init__(self):
        super(ToolButton,self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("ToolButton")
        self.setGeometry(400,400,300,260)

        self.toolbar = self.addToolBar("toolBar")
        self.statusBar()

        self._detailsbutton = QToolButton()                                     
        self._detailsbutton.setCheckable(True)                                  
        self._detailsbutton.setChecked(False)                                   
        self._detailsbutton.setArrowType(Qt.RightArrow)
        self._detailsbutton.setAutoRaise(True)

        self._detailsbutton.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self._detailsbutton.clicked.connect(self.showDetail)
        self.toolbar.addWidget(self._detailsbutton)

    def showDetail(self):
        if self._detailsbutton.isChecked():
            self.statusBar().showMessage("Show Detail....")
        else:
            self.statusBar().showMessage("Close Detail....")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ToolButton()
    ex.show()
    sys.exit(app.exec_())
```
##### 控件说明：
| 控件类型    | 控件名称       | 文本 | 图标       |
| ----------- | -------------- | ---- | ---------- |
| QToolButton | _detailsbutton |      | 右箭头图标 |
##### 示例说明
图标为“右箭头图标”的 Buttton，此按钮有开关之分。当Button打开之后在消息栏显示“Show Detail….”,反之显示“Close Detail”。
##### 代码分析
其他代码部分可以参考上一篇《Pyqt5系列(二 )-第一个PyQt程序》中的说明。
L24~25:
```python
self._detailsbutton.setCheckable(True)                                         self._detailsbutton.setChecked(False)
```
setCheckable()方法，“True”设置该button为可选属性，及存在“开”和“关”两种状态。 setChecked()方法，设置button的状态为为选中的状态。

L26:
```python
self._detailsbutton.setArrowType(Qt.RightArrow)
```
setArrowType()方法，设定button上显示的箭头类型 arrowType，箭头属性，按钮是否显示一个arrow代替正常的icon
> Qt.NoArrow 0
Qt.UpArrow 1
Qt.DownArrow 2
Qt.LeftArrow 3
Qt.RightArrow 4

L29:
```python
self._detailsbutton.setToolButtonStyle(Qt.ToolButtonIconOnly)
```
setToolButtonStyle()，设定button文本和图标显示的样式。程序中的参数为只显示icon不显示文本（Qt.ToolButtonIconOnly） 参数类型如下：
> Qt.ToolButtonIconOnly 0 Only display the icon.
Qt.ToolButtonTextOnly 1 Only display the text.
Qt.ToolButtonTextBesideIcon 2 The text appears beside the icon.
Qt.ToolButtonTextUnderIcon 3 The text appears under the icon.
Qt.ToolButtonFollowStyle 4

如果在实际的使用过程中，需要同时显示自定义的icon和文本的时候，可以按照如下参数设置：
```python
self._detailsbutton.setIcon(QIcon("test.jpg"))
self._detailsbutton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
```
对于QPushButton和QToolButton，如上的例子中只是涉及到部分常用的方法，所以对于详细的说明可以通过如下两个途径：

PyQt5 Class Reference 网站： http://pyqt.sourceforge.net/Docs/PyQt5/class_reference.html

在命令行中通过help()方法： 如 help(QPushButton)
