# patrickatesta.com

Source for my academic website. Built with [Quarto](https://quarto.org).

## Editing

Each page is a Markdown file:

| Page | File | URL |
|---|---|---|
| Home | `index.qmd` | `/` |
| About Me | `about-me/index.qmd` | `/about-me/` |
| Research | `research/index.qmd` | `/research/` |
| Resources | `data/index.qmd` | `/data/` |
| Teaching | `teaching/index.qmd` | `/teaching/` |
| Contact | `contact/index.qmd` | `/contact/` |

Site-wide settings (nav bar, footer, title) live in `_quarto.yml`.
Styling lives in `styles.scss`.

PDFs go in `files/`, images in `images/`. Link to them from a page with a
relative path, e.g. from `research/index.qmd`:

```markdown
[Draft](../files/my-new-paper.pdf)
```

## Previewing locally

```bash
quarto preview
```

Opens a live-reloading browser tab. Edits show up on save.

## Building

```bash
quarto render
```

Writes the finished static site to `_site/`. That directory is generated —
it is not checked into git.

## Adding a new paper

Drop the PDF in `files/`, then add an entry to `research/index.qmd`
following the pattern of the existing ones:

```markdown
::: {.entry}
"[Title](https://journal-url)," *Journal Name*, 2026, 1, 1–20
(with [Coauthor](https://coauthor-site)).

[Download: [Draft](../files/paper.pdf).]{.links}

[Summary: One sentence.]{.summary}
:::
```
