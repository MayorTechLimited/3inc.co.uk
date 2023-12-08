#! venv/bin/python
import os
from pathlib import Path

import markdown
from bs4 import BeautifulSoup
from staticjinja import Site


markdowner = markdown.Markdown(output_format="html5")


def context_blog_index(template):
    posts = []
    root = Path("./src/blog")
    for p in root.glob("**/*.md"):
        html = markdowner.convert(p.read_text())
        soup = BeautifulSoup(html, "html.parser")
        posts.append(
            {
                "title": soup.h1.get_text(),
                "url": str(p).replace("src", "").replace(".md", ""),
                "excerpt": soup.p.get_text(),
                "date": str(p).split("/")[2],
            }
        )
    return {"blog_posts": sorted(posts, key=lambda bp: bp["date"], reverse=True)}


def context_md(template):
    markdown_content = Path(template.filename).read_text()
    html = markdowner.convert(markdown_content)
    soup = BeautifulSoup(html, "html.parser")
    return {
        "post_content_html": html,
        "title": soup.h1.get_text(),
        "excerpt": soup.p.get_text(),
        "date": template.name.split("/")[1],
    }


def render_md(site, template, **kwargs):
    out = Path(site.outpath) / template.name.replace(".md", "") / "index.html"
    os.makedirs(out.parent, exist_ok=True)
    site.get_template("blog/_post.html").stream(**kwargs).dump(
        str(out), encoding="utf-8"
    )


if __name__ == "__main__":
    site = Site.make_site(
        searchpath=f"{os.environ['VG_APP_DIR']}/src",
        outpath="dist",
        contexts=[
            ("blog/index.html", context_blog_index),
            (r".*\.md", context_md),
        ],
        rules=[
            (r".*\.md", render_md),
        ],
    )
    site.render(use_reloader=True)
