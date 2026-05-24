import os
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

SOURCE_FILE = "brain_dump.md"
OUTPUT_FILE = "auto_presentation.html"
LIB_PATH = "lib/reveal.js"

HTML_TEMPLATE = """<!doctype html>
<html lang="ja">
<head>
    <meta charset="utf-8">
    <title>Auto Generated Presentation</title>
    <style>
        {css_content}
        :root {{
            --r-main-color: #fff;
            --r-heading-color: #4facfe;
            --r-link-color: #00f2fe;
        }}
        .reveal {{ background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%); }}
        .reveal h1 {{ text-shadow: 0 0 20px rgba(79, 172, 254, 0.8); }}
    </style>
</head>
<body>
    <div class="reveal">
        <div class="slides">
            {slides_content}
        </div>
    </div>
    <script>{js_reveal}</script>
    <script>{js_notes}</script>
    <script>{js_markdown}</script>
    <script>{js_highlight}</script>
    <script>
        Reveal.initialize({{
            hash: true,
            center: true,
            transition: 'zoom',
            plugins: [ RevealMarkdown, RevealHighlight, RevealNotes ]
        }});
    </script>
</body>
</html>
"""

def get_file_content(path):
    with open(path, 'r') as f:
        return f.read()

def build_presentation():
    print(f"[*] Building {OUTPUT_FILE} from {SOURCE_FILE}...")
    
    if not os.path.exists(SOURCE_FILE):
        with open(SOURCE_FILE, 'w') as f:
            f.write("# Start Typing Here\n\n- Bullet points become fragments\n- Use `---` for new slides")

    # Read assets
    css = "\\n".join([
        get_file_content(os.path.join(LIB_PATH, "reset.css")),
        get_file_content(os.path.join(LIB_PATH, "reveal.css")),
        get_file_content(os.path.join(LIB_PATH, "theme/black.css")),
        get_file_content(os.path.join(LIB_PATH, "plugin/highlight/monokai.css"))
    ])
    
    js_reveal = get_file_content(os.path.join(LIB_PATH, "reveal.js"))
    js_notes = get_file_content(os.path.join(LIB_PATH, "plugin/notes.js"))
    js_markdown = get_file_content(os.path.join(LIB_PATH, "plugin/markdown.js"))
    js_highlight = get_file_content(os.path.join(LIB_PATH, "plugin/highlight.js"))

    # Process Slides
    md_content = get_file_content(SOURCE_FILE)
    sections = md_content.split("\\n---\\n")
    slides_html = ""
    for section in sections:
        slides_html += f'<section data-markdown><script type="text/template">\\n{section}\\n</script></section>'

    final_html = HTML_TEMPLATE.format(
        css_content=css,
        slides_content=slides_html,
        js_reveal=js_reveal,
        js_notes=js_notes,
        js_markdown=js_markdown,
        js_highlight=js_highlight
    )

    with open(OUTPUT_FILE, 'w') as f:
        f.write(final_html)
    
    print(f"[+] Done. {os.path.getsize(OUTPUT_FILE)} bytes written.")

class Watcher(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(SOURCE_FILE):
            build_presentation()

if __name__ == "__main__":
    build_presentation()
    print(f"[*] Monitoring {SOURCE_FILE} for changes... (Ctrl+C to stop)")
    observer = Observer()
    observer.schedule(Watcher(), ".", recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
