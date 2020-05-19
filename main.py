
from PyQt5 import QtCore, QtGui, QtWidgets

try:
    import os
    import time
    from gtts import gTTS
    import wolframalpha
    import playsound
    import speech_recognition as sr

except:
    os.system("sudo pip3 install SpeechRecognition")
    os.system("sudo pip3 install gtts")
    os.system("sudo pip3 install PlaySound")
    os.system("sudo pip3 install wolframalpha")

num = 0

class Ui_MainWindow(object):
 
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(746, 725)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.UploadBtn = QtWidgets.QPushButton(self.centralwidget)
        self.UploadBtn.setGeometry(QtCore.QRect(20, 30, 691, 51))
        self.UploadBtn.setAutoFillBackground(False)
        self.UploadBtn.setStyleSheet("QPushButton{\n"
"    font-weight:bold;\n"
"    outline:none;\n"
"    color:#fff;\n"
"    font-style:italic;\n"
"    transition: all 0.5s ease;\n"
"background-color:#dd1200;\n"
"}\n"
"QPushButton:hover{\n"
"    color:#000;\n"
"    pointer:cursor;\n"
"}")
        self.UploadBtn.setObjectName("UploadBtn")
        self.UploadBtn.clicked.connect(self.pushButton_Handler)
        self.fileBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.fileBrowser.setGeometry(QtCore.QRect(20, 100, 691, 581))
        self.fileBrowser.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fileBrowser.setReadOnly(False)
        self.fileBrowser.setObjectName("fileBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 746, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "File Reader"))
        self.UploadBtn.setText(_translate("MainWindow", "Upload File"))

    def pushButton_Handler(self):
        print("Button Pressed")
        self.open_dialog_box()
    
    def open_dialog_box(self):
        filename = QtWidgets.QFileDialog.getOpenFileName()
        if filename[0]:
            f = open(filename[0],'r')
            with f:
                data = f.read()
                self.fileBrowser.setText(data)
                self.assisant(data)
    
    
    def assisant(self,document):
        global num
        num += 1
        print(document)
        toSpeak = gTTS(text=document,lang="tr",slow=False)
        sound_file = str(num)+".mp3"
        toSpeak.save(sound_file)

        playsound.playsound(sound_file,True)
        os.remove(sound_file)

    def read(self):
        rObject = sr.Recognizer()
        audio = ''
        with sr.Microphone() as source:
            self.assisant("Lütfen Bekleyiniz")
            audio = rObject.listen(source,phrase_time_limit=5)
            print("Hazirlaniyor")
        try:
            txt = rObject.recognize_google(audio,language="tr_TR")
            print(txt)
            return txt
        except:
            self.assisant("dosya yok")

        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

