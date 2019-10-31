import string

from src.template.common.CommonTmpl import HeadTmpl, ScriptTmpl, NavTmpl


class LayoutTemplate:
    def __init__(self, content=""):
        self.content = {
            'head': HeadTmpl().render(),
            'nav': NavTmpl().render(),
            'body': content,
            'script': ScriptTmpl().render()
        }

        self.template = """
        <!DOCTYPE html>
        <html lang="ja">
          <head>
            $head
          </head>
          <body>
          　$nav

            <div class="template-container">
            $body
            </div>

            $script
          <body>
        </html>
        """

    def render(self):
        tmpl = string.Template(self.template)
        return tmpl.substitute(self.content)

