# Speaking portfolio assets

PDFs, slide images and headshots for [portfolio.dark.ca](https://github.com/phrawzty/portfolio.dark.ca). They are **ordinary Git files**: a clone contains the real bytes, and the repository can be mirrored to any Git host.

## Layout

```text
files/
  decks/
    2018-06-01-serverless-revealed-dotscale-2018/
      2018-06-01-serverless-revealed-dotscale-2018.pdf
      slides/
        001.jpg
        002.jpg
  speaker/
    daniel-maher-headshot-1.jpg
```

Each deck version keeps its PDF and slide images together. Unchanged repeats share the folder. Revisions get new readable names or a `-v2` suffix; later title edits do not rename existing assets. Image-only entries have no PDF. Identical file contents share one Git blob even when used at multiple paths. Integrity checksums, editable transcripts and appearance-specific text live in the portfolio repo.

## Use

Clone alongside `portfolio.dark.ca`, normally under `~/repos`. Then author talks from the portfolio checkout:

```sh
cd ~/repos/portfolio.dark.ca
uv run portfolio
```

Adding slides processes the PDF locally and writes its bundle here. **Commit and push public assets** uses regular Git to commit the files referenced by published appearances, pushes this checkout's configured remote, and records the commit in the portfolio's `data/assets-lock.json`. Commit that lock with the portfolio content.

You can also commit assets manually, then run `uv run portfolio assets publish` from the portfolio checkout to record/push that commit. Unrelated staged changes must be committed or unstaged first. Draft-only files are not automatically included.

Cloudflare builds check out the recorded commit. It serves slide images; PDF downloads use `assets.public_base_url` in the portfolio's `portfolio.toml`, initially GitHub raw-file URLs at that commit. To use another HTTP host, serve `files/` from a clone and change that URL. No `assets.dark.ca` DNS record or separate website is required.

## Migration material and disk usage

`preservation/` is an ignored local Noti.st recovery archive, separate from the website assets. Its existing Release backup and restore/verify instructions are in [migration notes](docs/migration.md). Retention/cold storage is still undecided; it is not committed to Git.

`releases/` is ignored scratch space. The website does not use the historical Release image bundles or PDF attachments.

A Git checkout holds both working binaries and Git's compressed objects. Portfolio preview/build hard links refer to the same working files, so independently reported directory sizes overlap. Renaming unchanged assets reuses their binary objects.

Launch progress and dashboard steps are tracked in the [portfolio launch checklist](https://github.com/phrawzty/portfolio.dark.ca/blob/main/deploy/launch-checklist.md).
