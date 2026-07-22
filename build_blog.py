import glob
import os
import re

import markdown

BLOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "blog")
PORTFOLIO = "https://sasireddy001.github.io/Portfolio/"

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <style>
    :root {{ --bg:#0f172a; --card:#111827; --text:#e2e8f0; --muted:#94a3b8; --accent:#38bdf8; --code:#1e293b; --border:#334155; }}
    * {{ box-sizing: border-box; }}
    body {{ font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: var(--bg); color: var(--text); margin:0; line-height:1.75; }}
    header {{ background: var(--card); padding:1rem 1.5rem; border-bottom:1px solid var(--border); }}
    header a {{ color: var(--accent); text-decoration:none; font-weight:600; }}
    main {{ max-width:760px; margin:0 auto; padding:3rem 1.5rem 4rem; }}
    h1 {{ font-size:2.2rem; line-height:1.2; margin-bottom:1rem; }}
    h2 {{ color: var(--accent); border-bottom:1px solid var(--border); padding-bottom:.4rem; margin-top:2.5rem; font-size:1.5rem; }}
    h3 {{ margin-top:2rem; }}
    p, li {{ color: var(--text); }}
    a {{ color: var(--accent); }}
    code {{ background: var(--code); padding:.15rem .35rem; border-radius:.25rem; font-size:.9rem; }}
    pre {{ background: var(--code); padding:1rem; border-radius:.5rem; overflow-x:auto; }}
    pre code {{ background: transparent; padding:0; }}
    blockquote {{ border-left: 3px solid var(--accent); margin:0; padding-left:1rem; color: var(--muted); }}
    table {{ width:100%; border-collapse: collapse; margin:1.5rem 0; }}
    th, td {{ border:1px solid var(--border); padding:.5rem .75rem; text-align:left; }}
    th {{ background: var(--code); }}
    .mermaid {{ background: transparent; padding:0; text-align:center; }}
    .mermaid:not([data-processed="true"]) {{ visibility: hidden; }}
    footer {{ text-align:center; padding:2rem; color: var(--muted); border-top:1px solid var(--border); }}
  </style>
</head>
<body>
  <header><a href="{portfolio}">← Back to Portfolio</a></header>
  <main>
    {content}
  </main>
  <footer>© Sasidhar Mopuru · Data & AI Platform Engineer</footer>
  <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
  <script>mermaid.initialize({{startOnLoad:true, theme:'dark'}});</script>
</body>
</html>
"""


def main():
    for path in glob.glob(os.path.join(BLOG_DIR, "*.md")):
        if os.path.basename(path).lower() in ("readme.md",):
            continue
        with open(path, "r", encoding="utf-8") as f:
            md = f.read()

        first_line = md.split("\n")[0].lstrip("#").strip()
        title = first_line or os.path.basename(path).replace("-", " ").replace(".md", "").title()

        mermaids = []

        def store_mermaid(m: re.Match) -> str:
            mermaids.append(m.group(1))
            return f"\n\nMERMAID_{len(mermaids) - 1}\n\n"

        md_work = re.sub(r"```mermaid\s*\n(.*?)\n```", store_mermaid, md, flags=re.DOTALL)

        body = markdown.markdown(md_work, extensions=["fenced_code", "tables"])

        def restore_mermaid(m: re.Match) -> str:
            idx = int(m.group(1))
            return f'<pre class="mermaid">{mermaids[idx]}</pre>'

        body = re.sub(r"(?:<p>)?MERMAID_(\d+)(?:</p>)?", restore_mermaid, body)

        out_path = path.replace(".md", ".html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(TEMPLATE.format(title=title, portfolio=PORTFOLIO, content=body))
        print("Generated", out_path)


if __name__ == "__main__":
    main()
