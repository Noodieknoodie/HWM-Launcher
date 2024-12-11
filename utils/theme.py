from PyQt5.QtGui import QColor, QFont, QPalette
from PyQt5.QtCore import Qt

class Theme:
    # Modern Color Palette
    PRIMARY = "#2B3A67"        # Deep Navy
    SECONDARY = "#496A81"      # Steel Blue
    ACCENT = "#66999B"         # Sage
    BACKGROUND = "#F8F9FA"     # Light Gray
    SURFACE = "#FFFFFF"        # White
    SURFACE_ALT = "#E9ECEF"    # Light Gray Alt
    ERROR = "#DC3545"          # Red
    SUCCESS = "#28A745"        # Green
    WARNING = "#FFC107"        # Amber
    INFO = "#17A2B8"          # Cyan
    TEXT_PRIMARY = "#212529"   # Dark Gray
    TEXT_SECONDARY = "#6C757D" # Medium Gray
    TEXT_DISABLED = "#ADB5BD"  # Light Gray
    BORDER = "#DEE2E6"        # Border Gray
    
    # Fonts
    FONT_FAMILY = "Segoe UI"
    FONT_SIZES = {
        'h1': 28,
        'h2': 24,
        'h3': 20,
        'h4': 16,
        'body': 14,
        'small': 12
    }
    
    # Spacing and Sizing
    PADDING = {
        'xs': 4,
        'small': 8,
        'medium': 16,
        'large': 24,
        'xl': 32
    }
    BORDER_RADIUS = {
        'small': 4,
        'medium': 8,
        'large': 12
    }
    
    # Component Styles
    BUTTON_STYLE = """
        QPushButton {{
            background-color: {primary};
            color: white;
            border: none;
            border-radius: {border_radius}px;
            padding: 10px 20px;
            font-family: "{font_family}";
            font-size: 14px;
            font-weight: 500;
            min-width: 100px;
        }}
        QPushButton:hover {{
            background-color: {secondary};
        }}
        QPushButton:pressed {{
            background-color: {accent};
        }}
        QPushButton:disabled {{
            background-color: {disabled};
            color: {text_disabled};
        }}
    """
    
    SIDEBAR_STYLE = """
        QWidget#sidebar {{
            background-color: {surface};
            border-right: 1px solid {border};
        }}
        QLabel#sidebar_title {{
            color: {primary};
            font-size: 18px;
            font-weight: bold;
            padding: 20px 0;
            background-color: {surface};
            border-bottom: 1px solid {border};
        }}
        QListWidget {{
            background-color: {surface};
            border: none;
            outline: none;
            padding: 8px;
        }}
        QListWidget::item {{
            color: {text_primary};
            padding: 12px 16px;
            border-radius: {border_radius}px;
            margin: 2px 8px;
            font-size: 14px;
        }}
        QListWidget::item:selected {{
            background-color: {primary};
            color: white;
        }}
        QListWidget::item:hover:!selected {{
            background-color: {surface_alt};
        }}
    """
    
    MAIN_WINDOW_STYLE = """
        QMainWindow {{
            background-color: {background};
        }}
        QWidget {{
            font-family: "{font_family}";
        }}
        QLabel {{
            color: {text_primary};
        }}
        QFrame#content_frame {{
            background-color: {surface};
            border-radius: {border_radius}px;
            padding: 24px;
        }}
        QSplitter::handle {{
            background-color: {border};
            width: 1px;
        }}
    """

    FILE_SECTION_STYLE = """
        QFrame#file_section {{
            background-color: {surface};
            border: 1px solid {border};
            border-radius: {border_radius}px;
            padding: 16px;
        }}
        QLabel#section_title {{
            color: {primary};
            font-weight: bold;
            font-size: 16px;
            margin-bottom: 8px;
        }}
        QLabel#status_label {{
            color: {text_secondary};
            font-size: 13px;
            margin: 4px 0;
        }}
    """

    SCRIPT_LOADER_STYLE = """
        QWidget#content_frame {{
            background-color: {surface};
            border-radius: {border_radius}px;
            padding: 24px;
        }}
        QLabel#title {{
            color: {primary};
            font-size: 20px;
            font-weight: bold;
            margin-bottom: 16px;
        }}
        QLabel#description {{
            color: {text_secondary};
            font-size: 14px;
            margin-bottom: 24px;
        }}
        QLabel#error {{
            color: {error};
            font-size: 14px;
            padding: 8px;
            background-color: {surface_alt};
            border-radius: {border_radius}px;
        }}
    """

    @classmethod
    def get_style_params(cls):
        """Return a dictionary with all style parameters"""
        return {
            'primary': cls.PRIMARY,
            'secondary': cls.SECONDARY,
            'accent': cls.ACCENT,
            'background': cls.BACKGROUND,
            'surface': cls.SURFACE,
            'surface_alt': cls.SURFACE_ALT,
            'border': cls.BORDER,
            'text_primary': cls.TEXT_PRIMARY,
            'text_secondary': cls.TEXT_SECONDARY,
            'text_disabled': cls.TEXT_DISABLED,
            'disabled': cls.TEXT_DISABLED,
            'font_family': cls.FONT_FAMILY,
            'border_radius': cls.BORDER_RADIUS['medium'],
            'error': cls.ERROR
        }
    
    @classmethod
    def get_title_font(cls):
        font = QFont(cls.FONT_FAMILY, cls.FONT_SIZES['h2'])
        font.setWeight(QFont.Bold)
        return font
    
    @classmethod
    def get_body_font(cls):
        return QFont(cls.FONT_FAMILY, cls.FONT_SIZES['body'])
    
    @classmethod
    def apply_theme(cls, app):
        """Apply theme palette to entire application"""
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(cls.BACKGROUND))
        palette.setColor(QPalette.WindowText, QColor(cls.TEXT_PRIMARY))
        palette.setColor(QPalette.Base, QColor(cls.SURFACE))
        palette.setColor(QPalette.AlternateBase, QColor(cls.SURFACE_ALT))
        palette.setColor(QPalette.ToolTipBase, QColor(cls.SURFACE))
        palette.setColor(QPalette.ToolTipText, QColor(cls.TEXT_PRIMARY))
        palette.setColor(QPalette.Text, QColor(cls.TEXT_PRIMARY))
        palette.setColor(QPalette.Button, QColor(cls.PRIMARY))
        palette.setColor(QPalette.ButtonText, QColor("white"))
        palette.setColor(QPalette.Highlight, QColor(cls.ACCENT))
        palette.setColor(QPalette.HighlightedText, QColor("white"))
        palette.setColor(QPalette.Disabled, QPalette.Text, QColor(cls.TEXT_DISABLED))
        palette.setColor(QPalette.Disabled, QPalette.ButtonText, QColor(cls.TEXT_DISABLED))
        app.setPalette(palette)