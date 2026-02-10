# 📝 Markdown to HTML Converter

A **Python-based tool** to **convert Markdown-formatted text into HTML**.
This project helps users **quickly transform Markdown documents into HTML** for websites, blogs, or documentation.

---

## 🎯 Aim of the Project

To develop a **Python program** that can read Markdown text and convert it into **proper HTML**, supporting **headings, lists, links, bold/italic text, and inline code**, while allowing **file-based input and output**.

---

## 📝 Objectives

* Read Markdown content from an **input file**.
* Parse and convert Markdown elements to **corresponding HTML tags**.
* Support **headings (# to ######)**, **bold/italic**, **lists**, **inline code**, and **links**.
* Save the converted HTML into an **output file** for use in browsers or web pages.
* Ensure the program is **file-driven**, so changes in input automatically reflect in output.

---

## ✨ Features

* Convert Markdown headings (H1-H6) to `<h1>` - `<h6>`.
* Convert **bold** (`**text**`) and *italic* (`*text*`) text.
* Convert **unordered lists** (`- item`) to `<ul><li>...</li></ul>`.
* Convert **inline code** using backticks (```).
* Convert **links** `[text](url)` to `<a href="url">text</a>`.
* Automatic file-based **input and output** for easy editing.
* Fully Python-based — no additional libraries required.

---

## ⚙️ Requirements

* Python 3.8+
* Libraries:

  * `re` (built-in)
  * `os` (built-in)

No additional installations are required.

---

## 📂 Project Structure

```
MarkdownConverter/
│── markdown_to_html.py    # Main Python program
│── input.md               # Markdown input file
│── output.html            # Generated HTML output
│── README.md              # Project documentation
```

---

## 🚀 How to Run

1. Make sure Python is installed.
2. Place your Markdown content in `input.md`.
3. Run the program:

```bash
python markdown_to_html.py
```

4. Check the generated `output.html` file in the same folder.
5. Edit `input.md` and rerun to automatically update `output.html`.

---

## 🧩 Code Overview

* **read_markdown()** → Reads Markdown text from the input file.
* **write_html(content)** → Writes the converted HTML to the output file.
* **parse_headings(text)** → Converts `#` to `<h1>` ... `<h6>`.
* **parse_bold_italic(text)** → Converts `**bold**` and `*italic*`.
* **parse_inline_code(text)** → Converts `` `code` `` to `<code>`.
* **parse_links(text)** → Converts `[text](url)` to `<a href="url">text</a>`.
* **parse_lists(text)** → Converts `- item` to `<ul><li>item</li></ul>`.
* **parse_paragraphs(text)** → Wraps remaining lines in `<p>`.
* **convert()** → Calls all parsing functions in order and writes output.

---

## 🗃️ Sample `input.md`

```markdown
# My Markdown Project

This is **bold text** and this is *italic text*.

- First item
- Second item

Use `print("Hello World")` to display output.

Visit [Python](https://python.org)
```

---

## 🖥️ Sample `output.html`

```html
<h1>My Markdown Project</h1>

<p>This is <strong>bold text</strong> and this is <em>italic text</em>.</p>

<ul>
<li>First item</li>
<li>Second item</li>
</ul>

<p>Use <code>print("Hello World")</code>.</p>
<p>Visit <a href="https://python.org">Python</a></p>
```

---

## 🔮 Future Enhancements

* Add **support for ordered lists** (`1. item`) and nested lists.
* Handle **blockquotes (`> quote`)** and code blocks (` ``` `).
* Add **GUI interface** for easier file selection and conversion.
* Add **live preview in browser**.
* Export to **HTML templates** for blogs or websites.

---

## 👤 Developer

**Name:** Jiban Maji
**GitHub:** [https://github.com/Jiban0507](https://github.com/Jiban0507)