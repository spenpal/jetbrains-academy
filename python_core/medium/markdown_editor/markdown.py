# CLASS #
class MarkdownEditor:
    formatters = 'plain bold italic header link inline-code ordered-list unordered-list new-line'.split()
    special_cmds = '!help !done'.split()

    def __init__(self):
        self.output = ''

    def _plain(self):
        text = input('Text: ')
        md_text = text
        self.output += md_text

    def _bold(self):
        text = input('Text: ')
        md_text = f'**{text}**'
        self.output += md_text

    def _italic(self):
        text = input('Text: ')
        md_text = f'*{text}*'
        self.output += md_text

    def _header(self):
        while not 1 <= (level := int(input('Level: '))) <= 6:
            print('The level should be within the range of 1 to 6')

        text = input('Text: ')
        md_text = f'\n{"#" * level} {text}\n'
        self.output += md_text

    def _link(self):
        label = input('Label: ')
        url = input('URL: ')
        md_text = f'[{label}]({url})'
        self.output += md_text

    def _inline_code(self):
        text = input('Text: ')
        md_text = f'`{text}`'
        self.output += md_text

    def _list(self, ordered):
        while (rows := int(input('Number of rows: '))) < 1:
            print('The number of rows should be greater than zero')

        for num in range(1, rows + 1):
            row_text = input(f'Row #{num}: ')
            prefix = f'{num}.' if ordered else '*'
            md_text = f'{prefix} {row_text}\n'
            self.output += md_text

    def _new_line(self):
        md_text = '\n'
        self.output += md_text

    def _formatting(self, formatter):
        md_format = {
            'plain': self._plain,
            'bold': self._bold,
            'italic': self._italic,
            'header': self._header,
            'link': self._link,
            'inline-code': self._inline_code,
            'ordered-list': lambda: self._list(ordered=True),
            'unordered-list': lambda: self._list(ordered=False),
            'new-line': self._new_line
        }

        md_format[formatter]()

    def _print_help(self):
        print(f'Available formatters: {" ".join(self.formatters)}')
        print(f'Special commands: {" ".join(self.special_cmds)}')

    def save(self):
        with open('output.md', 'w') as f:
            f.write(self.output.lstrip())

    def start(self):
        while (formatter := input('Choose a formatter: ')) != '!done':
            if formatter == '!help':
                self._print_help()
            elif formatter not in self.formatters:
                print('Unknown formatting type or command')
            else:
                self._formatting(formatter)
                print(self.output.lstrip())

        self.save()


# MAIN #
md = MarkdownEditor()
md.start()