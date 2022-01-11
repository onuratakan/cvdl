

import toml


from CVContent import *
from CVStyle import *

class CVMaker:
    def __init__(self, content_path, schema_path, style_path, output_file_name):
        self.content_path = content_path
        self.style_path = style_path
        self.schema_path = schema_path
        self.output_file_name = output_file_name
        self.content = None
        self.style = None
        self.schema = None
        self.cv = None

    def process_content(self):
        raw_content = self.read_content()
        parsed_content = self.parse_content(raw_content)
        self.content = self.generate_structured_content(parsed_content)

    def read_content(self):
        f = open(self.content_path, 'r')
        return f.read()

    def parse_content(self, raw_content):
        parsed_content = toml.loads(raw_content)
        print(parsed_content)

    def generate_structured_content(self, parsed_content):
        pass

    def process_style(self):
        pass

    def generate_cv(self):
        pass

    def render_cv(self):
        pass
