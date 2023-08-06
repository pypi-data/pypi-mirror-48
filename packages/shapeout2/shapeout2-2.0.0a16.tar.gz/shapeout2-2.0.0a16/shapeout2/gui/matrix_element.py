import pkg_resources

from PyQt5 import uic, QtWidgets, QtCore


class MatrixElement(QtWidgets.QWidget):
    _quick_view_instance = None
    quickview_selected = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        path_ui = pkg_resources.resource_filename(
            "shapeout2.gui", "matrix_element.ui")
        uic.loadUi(path_ui, self)

        self.active = False
        self.enabled = True

        self.update_content()

    def __getstate__(self):
        state = {"active": self.active,
                 "enabled": self.enabled}
        return state

    def __setstate__(self, state):
        self.active = state["active"]
        self.enabled = state["enabled"]
        self.update_content()

    def mousePressEvent(self, event):
        # toggle selection
        if event.modifiers() == QtCore.Qt.ShiftModifier:
            quickview = True
        else:
            self.active = not self.active
            quickview = False
        self.update_content(quickview)
        event.accept()

    def update_content(self, quickview=False):
        if self.active and self.enabled:
            color = "#86E789"  # green
            label = "active"
            tooltip = "Click to deactivate"
        elif self.active and not self.enabled:
            color = "#A4D5A7"  # gray-green
            label = "active\n(disabled)"
            tooltip = "Click to deactivate"
        elif not self.active and self.enabled:
            color = "#EFEFEF"  # light gray
            label = "inactive"
            tooltip = "Click to activate"
        else:
            color = "#C0C1C0"  # gray
            label = "inactive"
            tooltip = "Click to activate"

        curinst = MatrixElement._quick_view_instance
        if curinst is self:
            do_quickview = True
        elif quickview:
            # reset color of old quick view instance
            if curinst is not None and self is not curinst:
                MatrixElement._quick_view_instance = None
                curinst.update_content()
            MatrixElement._quick_view_instance = self
            do_quickview = True
        else:
            do_quickview = False
        if do_quickview:
            color = "#F0A1D6"
            label += "\n(QV)"
            self.quickview_selected.emit()
        else:
            tooltip += "\nShift+Click for Quick View"

        self.setStyleSheet("background-color:{}".format(color))
        self.label.setStyleSheet("background-color:{}".format(color))
        self.label.setText(label)
        self.setToolTip(tooltip)
        self.label.setToolTip(tooltip)
