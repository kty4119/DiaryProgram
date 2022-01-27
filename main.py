import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication
#from PyQt5 import uic
class DiaryProgram(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.statusBar()
        self.statusBar().showMessage("상태표시줄")
        
        menu = self.menuBar()  #메뉴바 생성
        menu_file = menu.addMenu("FILE")   #그룹 생성
        menu_edit= menu.addMenu("EDIT")   #그룹 생성
        
        file_exit = QAction('EXIT',self)    #메뉴 객체 생성
        file_exit.setShortcut("Ctrl+Q")
        file_exit.setStatusTip("상태표시")
        new_txt = QAction("txt 파일", self)
        new_py= QAction("py 파일", self)
        
        file_exit.triggered.connect(QCoreApplication.instance().quit)
        
        file_new = QMenu('new',self) # 서브그룹 생성
        
        file_new.addAction(new_txt) # 서브 메뉴 추가
        file_new.addAction(new_py)# 서브 메뉴 추가
        
        menu_file.addMenu(file_new)     #주 메뉴 추가
        menu_file.addAction(file_exit)#주 메뉴 추가
        
        btn = QPushButton("일기 쓰기", self)
        btn.resize(btn.sizeHint())
        btn.move(500,600)
        # 버튼에 메서드 연결(이벤트처리)
        btn.clicked.connect(QCoreApplication.instance().quit)
        
        btn.setToolTip("일기장 생성 및 저장")
        
        self.setGeometry(300,300,700,700)
        self.setWindowTitle("일기장")
        self.show()
    def closeEvent(self, QCloseEvent):
        ans = QMessageBox.question(self,"종료 확인", "종료하시겠습니까?",QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if ans == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()
        
app = QApplication(sys.argv)
w = DiaryProgram()
sys.exit(app.exec_())

#form_class = uic.loadUiType("MainWindow.ui")[0]
#print(form_class)

#window = QWidget()
#window.show()

#app.exec_()
'''
class WindowClass(QMainWindow, form_class):
    def __init(self):
        super.setupUi(self)
        self.pushButton.clicked.connect(self.functionStart)
    
    def functionStart(self):
        f = open('일기장이름.txt','w')
        f.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QWidget()
    Window = WindowClass()
    Window.show()
    app.exec_()
'''