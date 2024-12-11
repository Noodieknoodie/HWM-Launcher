from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from utils.theme import Theme

def load_ui(parent=None):
    widget = QWidget(parent)
    layout = QVBoxLayout(widget)
    
    label = QLabel("Test Script")
    label.setFont(Theme.get_title_font())
    layout.addWidget(label)
    
    button = QPushButton("Test Button")
    button.setStyleSheet(Theme.BUTTON_STYLE.format(
        primary=Theme.PRIMARY,
        secondary=Theme.SECONDARY,
        accent=Theme.ACCENT,
        disabled=Theme.TEXT_DISABLED,
        text_disabled=Theme.TEXT_DISABLED,
        font_family=Theme.FONT_FAMILY,
        border_radius=Theme.BORDER_RADIUS['small']
    ))
    layout.addWidget(button)
    
    return widget 