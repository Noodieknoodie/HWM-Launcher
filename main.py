import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QSplitter, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from ui.sidebar import Sidebar
from ui.script_loader import ScriptLoader
from utils.theme import Theme

class ElkRunApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set window title and size
        self.setWindowTitle("ElkRun Platform")
        self.setGeometry(100, 100, 1200, 800)
        
        # Apply theme
        self.setStyleSheet(Theme.MAIN_WINDOW_STYLE.format(**Theme.get_style_params()))

        # Load and set icon
        try:
            icon_path = os.path.join(os.path.dirname(__file__), "assets", "icons", "agenda_icon.ico")
            if os.path.exists(icon_path):
                self.setWindowIcon(QIcon(icon_path))
            else:
                QMessageBox.warning(self, "Missing Icon", "The application icon (agenda_icon.ico) is missing.")
        except Exception as e:
            QMessageBox.critical(self, "Icon Error", f"An error occurred while loading the icon:\n{e}")

        # Central widget and layout
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # Create splitter for sidebar and main content
        splitter = QSplitter(Qt.Horizontal)
        splitter.setHandleWidth(1)
        splitter.setStyleSheet("""
            QSplitter::handle {
                background-color: #e0e0e0;
            }
        """)
        
        # Add sidebar and script loader
        self.sidebar = Sidebar(self)
        self.script_loader = ScriptLoader(self)
        
        splitter.addWidget(self.sidebar)
        splitter.addWidget(self.script_loader)
        
        # Set initial sizes (30% sidebar, 70% main content)
        splitter.setSizes([int(self.width() * 0.3), int(self.width() * 0.7)])
        
        layout.addWidget(splitter)
        self.setCentralWidget(central_widget)

        # Connect sidebar selection to script loader
        self.sidebar.script_selected.connect(self.script_loader.load_script)
        
        # Connect script execution signal to run_script method
        self.script_loader.script_executed.connect(self.run_script)

    def run_script(self, script_name):
        processing_dialog = QMessageBox(self)
        processing_dialog.setWindowTitle("Processing")
        processing_dialog.setText("Processing files...")
        processing_dialog.setStandardButtons(QMessageBox.Cancel)
        processing_dialog.setModal(True)
        processing_dialog.show()
        QApplication.processEvents()

        try:
            # Import and execute the script
            script_module = __import__(f"scripts.{script_name}", fromlist=['run'])
            if hasattr(script_module, 'run'):
                script_module.run()
            processing_dialog.close()
        except Exception as e:
            processing_dialog.setText(f"An error occurred: {e}")
            processing_dialog.setIcon(QMessageBox.Critical)
            processing_dialog.setStandardButtons(QMessageBox.Ok)
            processing_dialog.exec_()

def main():
    app = QApplication(sys.argv)
    
    # Set application-wide stylesheet
    app.setStyle("Fusion")  # Use Fusion style for consistent cross-platform look
    
    elk_run_app = ElkRunApp()
    elk_run_app.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
