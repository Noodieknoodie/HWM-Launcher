import importlib
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QMessageBox, 
                           QFrame, QScrollArea)
from PyQt5.QtCore import Qt, pyqtSignal
from utils.theme import Theme

class ScriptLoader(QWidget):
    script_executed = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("script_loader")
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # Title section
        title_label = QLabel("Script Loader")
        title_label.setObjectName("script_loader_title")
        title_label.setFont(Theme.get_title_font())
        layout.addWidget(title_label)
        
        # Content frame
        self.content_frame = QFrame()
        self.content_frame.setObjectName("script_loader_content")
        self.content_frame.setFrameShape(QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Raised)
        content_layout = QVBoxLayout(self.content_frame)
        content_layout.addStretch()
        layout.addWidget(self.content_frame)
        
        # Apply theme
        self.setStyleSheet(Theme.SCRIPT_LOADER_STYLE.format(**Theme.get_style_params()))

    def load_script(self, script_name):
        # Clear previous content
        self.clear_content()
        
        try:
            # Load the script module
            script_module = __import__(f"scripts.{script_name}", fromlist=['load_ui'])
            
            # Call the load_ui function from the script module
            script_ui = script_module.load_ui(self.content_frame)
            
            # Add the script UI to the content frame
            self.content_frame.layout().insertWidget(0, script_ui)
        except Exception as e:
            self.show_error(f"Error loading script: {e}")

    def clear_content(self):
        """Remove all widgets from the content frame."""
        layout = self.content_frame.layout()
        while layout.count() > 1:  # Keep the stretcher
            widget = layout.takeAt(0).widget()
            if widget:
                widget.deleteLater()

    def show_error(self, message):
        """Display error message in the content area."""
        error_label = QLabel(message)
        error_label.setStyleSheet(f"color: {Theme.ERROR};")
        error_label.setWordWrap(True)
        self.content_frame.layout().insertWidget(0, error_label)
        
    def execute_script(self, script_name):
        """Emit the script_executed signal with the script name."""
        self.script_executed.emit(script_name)
