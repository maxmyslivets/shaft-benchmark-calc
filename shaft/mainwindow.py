from string import digits

from PySide6.QtWidgets import QMainWindow

from ui.shaft_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self) -> None:
        super(MainWindow, self).__init__()

        self.setupUi(self)

        self._init_triggers()

        self.old_shaft_line = ''

    def _init_triggers(self) -> None:
        self.shaft_H_line_edit.textChanged.connect(self.float_validation)
        # self.shaft_calc_button.clicked.connect(self.shaft_calc)

    def float_validation(self) -> None:
        line = self.shaft_H_line_edit.text()
        fix_line = ''
        try:
            for idx, ch in enumerate(line):
                ch = ch.replace(',', '.')
                if line.count('.') > 1:
                    raise ValueError
                if ch not in digits + '+-.,':
                    raise ValueError
                if ch in '+-' and idx != 0:
                    raise ValueError
                fix_line += ch
            self.shaft_H_line_edit.setText(fix_line)
            self.old_shaft_line = fix_line
        except ValueError:
            self.shaft_H_line_edit.setText(self.old_shaft_line)

    # def shaft_calc(self) -> None:
    #
    #     benchmark = float(self.shaft_H_line_edit.text())



