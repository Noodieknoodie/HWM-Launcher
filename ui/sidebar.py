import os
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QListWidget, QLabel, 
                           QFrame, QScrollArea)
from PyQt5.QtCore import pyqtSignal, Qt
from utils.theme import Theme

class Sidebar(QWidget):
    script_selected = pyqtSignal(str)

    def __init__(self, parent=None, scripts_dir="scripts"):
        super().__init__(parent)
        self.scripts_dir = scripts_dir
        self.setObjectName("sidebar")  # For styling
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # Title section
        title_label = QLabel("Available Scripts")
        title_label.setObjectName("sidebar_title")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setFont(Theme.get_title_font())
        layout.addWidget(title_label)

        # Scrollable script list
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFrameShape(QFrame.NoFrame)
        
        # Script list container
        list_container = QWidget()
        list_layout = QVBoxLayout(list_container)
        list_layout.setContentsMargins(0, 0, 0, 0)
        
        self.script_list = QListWidget()
        self.script_list.setFont(Theme.get_body_font())
        self.script_list.setFrameShape(QFrame.NoFrame)
        self.script_list.setSpacing(2)
        
        list_layout.addWidget(self.script_list)
        scroll_area.setWidget(list_container)
        layout.addWidget(scroll_area)
        
        # Load scripts and apply styling
        self.load_scripts()
        self.script_list.itemClicked.connect(self.on_script_selected)
        
        # Apply theme
        self.setStyleSheet(Theme.SIDEBAR_STYLE.format(**Theme.get_style_params()))

    def load_scripts(self):
        """Load available scripts from the scripts directory."""
        try:
            script_files = [
                f[:-3] for f in os.listdir(self.scripts_dir)
                if f.endswith('.py') and f != '__init__.py'
            ]
            
            # Sort scripts alphabetically
            script_files.sort()
            
            # Add each script as a list item with proper formatting
            for script_name in script_files:
                # Convert snake_case to Title Case for display
                display_name = " ".join(word.capitalize() for word in script_name.split('_'))
                self.script_list.addItem(display_name)
                
        except OSError as e:
            print(f"Error loading scripts: {e}")

    def on_script_selected(self, item):
        """Emit signal when a script is selected."""
        # Convert display name back to script name
        script_name = "_".join(item.text().lower().split())
        self.script_selected.emit(script_name)
