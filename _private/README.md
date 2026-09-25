# _private/

Working copies of documents you maintain outside the public site (resume, CV, etc.).

This folder is never built or served by Jekyll: any directory prefixed with `_` that
is not one of Jekyll's special directories (`_layouts`, `_includes`, `_data`, `_sass`,
`_plugins`) and not registered under `collections:` in `_config.yml` is skipped by
default. `_experiment/` in this repo works the same way. So files here are versioned
in git and visible in the repo, but will never appear on fuchsfranklin.github.io.

- `resume/resume.md` — one-page resume, plain-text working copy. Source-of-record
  formatting still lives in the actual .docx; sync edits back manually.
- `cv/cv.md` — placeholder for the long-form CV Word doc content, once it's pasted
  in as text (a .docx pasted directly into chat comes through corrupted — paste the
  extracted text instead, or point Kiro at the file's path on disk).
