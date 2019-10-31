from src.template.common.CommonTmpl import BaseTmpl


class InnerTmpl(BaseTmpl):
    pass

class ContentTmpl(InnerTmpl):
    def __init__(self, item: list = []):
        self.layout = 2
        self.tempate
