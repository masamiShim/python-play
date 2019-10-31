import string


class TextContent:
    def __init__(self, text=''):
        self.text = text
        self.template = """
        <p>
            $text
        </p>
        """

    def render(self):
        tmpl = string.Template(self.template)
        return tmpl.substitute({'text': self.text})
