class Tags:
    def __init__(self, text='text', subtag=None):
        self.text = text
        self.subtag = subtag

    def __str__(self):
        line = ''
        line += f"<{self.__class__.__name__.lower()}>\n"
        if self.text:
            line += f"{self.text}\n"
        if self.subtag:
            line += str(self.subtag)
        line += f"<{self.__class__.__name__.lower()}>\n"
        return line


class Html(Tags):
    def __init__(self, text='text', subtag=None):
        super().__init__(text, subtag)

    def __str__(self):
        return super().__str__()


class Body(Tags):
    def __init__(self, text='text', subtag=None):
        super().__init__(text, subtag)

    def __str__(self):
        return super().__str__()


class P(Tags):
    def __init__(self, text='text', subtag=None):
        super().__init__(text, subtag)

    def __str__(self):
        return super().__str__()


# q = Tags()
# p = P(text="Some text paragraph", subtag=q)
p = P(text="Some text paragraph")
body = Body("Some text body", subtag=p)
html = Html("Some HTML text", subtag=body)

print(html.__str__())
