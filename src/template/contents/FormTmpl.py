import string

from src.template.common.CommonTmpl import BaseTmpl


class FormTmpl(BaseTmpl):
    def __init__(self, form_items=[]):
        self.form_items = form_items
        self.template = """
        <form>
            $items
        </form>
        """

    def render(self):
        tmpl = string.Template(self.template)
        items = '\n'.join([item.render() for item in self.form_items])

        return tmpl.substitute({'items': items})


class InputTmpl(BaseTmpl):
    def __init__(self, id='', label='', type='input', placeholder='', hint=''):
        inputTmpl = string.Template("""
            <input $type class="form-control" $id $aria_describedby $placeholder />
        """)

        self.id = '' if not id else 'id="' + id + '"'
        self.label = '<label' + ('>' if not id else f' for="{id}">') + label + '</label>'
        self.type = f'type={type}'
        self.placeholder = '' if not placeholder else f' placeholder = "{placeholder}"'
        self.aria_describedby = '' if not hint else f'aria-describedby="{id}Help"'

        self.input = inputTmpl.substitute(
            {'type': self.type, 'id': self.id, 'aria_describedby': self.aria_describedby, 'placeholder': self.placeholder})

        self.small = '<small' + ('' if not id else f' id="{id}Help"') + f' class="form-text text-muted">{hint}</small>'

        self.template = """
            <div class="col">
                $label
                $input
                $small
            </div>
        """

    def render(self):
        tmpl = string.Template(self.template)
        return tmpl.substitute({'label': self.label, 'input': self.input, 'small': self.small})
