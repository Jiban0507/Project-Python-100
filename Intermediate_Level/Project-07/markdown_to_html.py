import re
import os


class MarkdownToHTML:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def read_markdown(self):
        with open(self.input_file, "r", encoding="utf-8") as file:
            return file.read()

    def write_html(self, content):
        with open(self.output_file, "w", encoding="utf-8") as file:
            file.write(content)

    def parse_headings(self, text):
        for level in range(6, 0, -1):
            text = re.sub(
                f'^{"#" * level} (.*)$',
                f'<h{level}>\\1</h{level}>',
                text,
                flags=re.MULTILINE
            )
        return text

    def parse_bold_italic(self, text):
        text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
        text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
        return text

    def parse_inline_code(self, text):
        return re.sub(r'`(.*?)`', r'<code>\1</code>', text)

    def parse_links(self, text):
        return re.sub(
            r'\[(.*?)\]\((.*?)\)',
            r'<a href="\2">\1</a>',
            text
        )

    def parse_lists(self, text):
        lines = text.split("\n")
        result = []
        in_list = False

        for line in lines:
            if line.startswith("- "):
                if not in_list:
                    result.append("<ul>")
                    in_list = True
                result.append(f"<li>{line[2:]}</li>")
            else:
                if in_list:
                    result.append("</ul>")
                    in_list = False
                result.append(line)

        if in_list:
            result.append("</ul>")

        return "\n".join(result)

    def parse_paragraphs(self, text):
        lines = text.split("\n")
        result = []

        for line in lines:
            if not line.strip():
                continue
            if line.startswith("<"):
                result.append(line)
            else:
                result.append(f"<p>{line}</p>")

        return "\n".join(result)

    def convert(self):
        markdown = self.read_markdown()

        html = markdown
        html = self.parse_headings(html)
        html = self.parse_bold_italic(html)
        html = self.parse_inline_code(html)
        html = self.parse_links(html)
        html = self.parse_lists(html)
        html = self.parse_paragraphs(html)

        self.write_html(html)
        print("Markdown successfully converted to HTML.")


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))

    input_path = os.path.join(base_dir, "input.md")
    output_path = os.path.join(base_dir, "output.html")

    converter = MarkdownToHTML(input_path, output_path)
    converter.convert()
