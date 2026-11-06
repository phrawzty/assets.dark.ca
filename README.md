# assets.dark.ca

PDFs, slide images and headshots for [portfolio.dark.ca](https://github.com/phrawzty/portfolio.dark.ca). All assets are checked into Git.

Clone alongside the portfolio repository:

```sh
git clone https://github.com/phrawzty/assets.dark.ca.git
```

Each deck lives under `files/decks/<date-title-event>/`, with its PDF and `slides/` images together. Headshots live under `files/speaker/`.

Manage slides from the portfolio checkout:

```sh
uv run portfolio
```

To commit and push updated assets:

```sh
uv run portfolio assets publish
```

This updates the portfolio’s `data/assets-lock.json`; commit that change with the portfolio.

Keep assets commits referenced by the portfolio available.
