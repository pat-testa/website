# tools/

One-shot scripts kept for provenance. **You do not need to run these to edit
the site** — `research/index.qmd` is a normal hand-editable file now.

- `genresearch.py` — generated the first version of `research/index.qmd`,
  including the Abstract/BibTeX toggles. Re-running it would overwrite any
  hand edits made to that page since, so don't, unless you mean to.
- `abstracts.json` — abstracts extracted from the PDFs in `files/`, keyed by
  paper slug. Kept so the text can be checked against the source.

Abstracts were pulled from the draft PDFs, de-hyphenated, and had ligatures
(`ﬁ` → `fi`) normalised. BibTeX DOIs were verified against Crossref.

## Adding a paper by hand

Copy an existing `::: {.entry}` block in `research/index.qmd` and edit it.
The toggle markup is plain HTML: a `.pill` button whose `aria-controls`
matches the `id` of a `.panel` div. Keep those ids unique across the page.
