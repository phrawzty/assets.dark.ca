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

Publish from the portfolio checkout:

```sh
uv run portfolio publish
```

The portfolio detects whether referenced assets changed. When necessary it commits and pushes those files here, updates `data/assets-lock.json`, verifies the production build and then pushes the portfolio. No routine Git work is needed in this repository.

Keep assets commits referenced by the portfolio available.
