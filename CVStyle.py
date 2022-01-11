

class CVStyle:
    """
    CVStyle is a set of dictionaries providing specification for style of
    different parts of the CV.
    """
    def __init__(self):
        self.metadata = None
        """
        Metadata Includes but not limited to
        - Margins
        - Font Choices
        - Line Heights
        - Space Between Entries
        - Page Layout
        - Default Entry Layouts
            + Content/Date/Place/Link
        - Colors
            + Background Color
            + Section Header Color
            + 
        - Borders
            + Existence
            + Width
            + Style(Color/Type etc.)
        - Footer
            + Page Number
            + Other Information
        - Date Style
        - Recurring Content Display Choices
            + Use of Hyphen/Emdash/Endash/Bullet
            + Icon Family
        """
        self.sections = None
        """
        Design document defines a custom layout for each schema type.
        These layouts can override the default settings provided 
        in the document as design metadata. 
        """



