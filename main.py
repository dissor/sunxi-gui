import sys
import os

from modules import *

# 兼容显示
os.environ['QT_FONT_DPI'] = '96'

# 全局控件
widgets = None

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()

        # 设置为全局控件
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # 设置默认界面


        # 按键点击
        widgets.btn_ver.clicked.connect(self.buttonClick)
        widgets.btn_list.clicked.connect(self.buttonClick)
        widgets.btn_spl.clicked.connect(self.buttonClick)
        widgets.btn_write.clicked.connect(self.buttonClick)
        widgets.btn_exec.clicked.connect(self.buttonClick)
        widgets.btn_spiflash_info.clicked.connect(self.buttonClick)
        widgets.btn_spiflash_read.clicked.connect(self.buttonClick)
        widgets.btn_spiflash_write.clicked.connect(self.buttonClick)

        widgets.pushButton.clicked.connect(self.buttonClick)
        widgets.pushButton_2.clicked.connect(self.buttonClick)
        widgets.pushButton_3.clicked.connect(self.buttonClick)
        widgets.pushButton_4.clicked.connect(self.buttonClick)


        # 显示应用
        self.show()

    # 按键点击
    def buttonClick(self):
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == "btn_ver":
            os.system("sunxi_tools\sunxi-fel.exe ver")


        print(f'Button "{btnName}" pressed!')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWidget()
    sys.exit(app.exec())