# assets.dark.ca

Git storage for the PDFs, slide images and headshots used by [portfolio.dark.ca](https://github.com/phrawzty/portfolio.dark.ca).

Clone alongside the portfolio repository:

```sh
git clone https://github.com/phrawzty/assets.dark.ca.git
```

Decks live under `files/decks/<date-title-event>/`, with each PDF and its `slides/` images together. Headshots live under `files/speaker/`.

Add and replace slides from the portfolio checkout:

```sh
uv run portfolio
```

After marking an appearance ready, commit and push its assets:

```sh
uv run portfolio assets publish
```

This commits only files referenced by published content, pushes this repository and updates the portfolio’s `data/assets-lock.json`. Commit that lock file with the portfolio changes.

Keep assets commits referenced by the portfolio available.
