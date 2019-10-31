from src.template.LayoutTemplate import LayoutTemplate
from src.template.contents.FormTmpl import FormTmpl, InputTmpl

path = "./outputTest.html"

form = FormTmpl([
    InputTmpl(
        id='email',
        type='email',
        label='Email',
        placeholder='hogehoge@example.com'),
    InputTmpl(
        id='text1',
        label='Text1',
        placeholder='Text1'),
    InputTmpl(
        id='text2',
        label='Text2',
        placeholder='Text2'),
    InputTmpl(
        id='text3',
        label='Text3',
        placeholder='Text3'),
    ]
)

layout = LayoutTemplate(form.render())
with open(path, encoding='UTF-8', mode='w') as f:
    f.writelines(layout.render())
