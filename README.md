# portfolio.dark.ca assets

PDFs, slide images and headshots for [Daniel Maher's speaking portfolio](https://github.com/phrawzty/portfolio.dark.ca), tracked as **ordinary Git files**. No Git LFS and no Release downloads are required for the website assets. Clone or mirror this repository to any Git host.

## Contents

- `files/pdfs/`: full-quality PDFs with readable date/title/event filenames. Identical PDFs are shared; revised PDFs receive readable version suffixes.
- `files/decks/`: individual slide images, grouped by immutable deck version. The directory hashes identify content versions; they are not the public PDF names.
- `files/speaker/`: publication headshots.
- `preservation-manifest.json` and `scripts/preservation.py`: the manifest and restore/verify tool for the separate migration backup.
- `preservation/`: ignored local migration material. **It is not committed.**
- `releases/`: ignored scratch directory for backup packaging.

## Use with the portfolio

Clone this repository alongside `portfolio.dark.ca` under the same parent directory (normally `~/repos`). The PDFs and images are immediately present in the clone.

From the portfolio checkout, run `uv run portfolio` to author talks. Adding a PDF processes it locally into images, keeps the original bytes here with a readable filename, and registers checksums/transcripts in the portfolio metadata. The menu's **Commit and push public assets** action uses normal Git to commit and push only the files referenced by public appearances, then records the resulting commit in the portfolio's `data/assets-lock.json`. Commit that lock with the portfolio content. You can also make an assets commit manually before running that action.

Builds use the pinned assets commit. Cloudflare serves images; PDF downloads use a configurable HTTP base URL (initially GitHub raw-file URLs pinned to the same commit). To use another host, serve `files/` from a clone and change `assets.public_base_url` in the portfolio. Nothing about the assets repository requires GitHub.

## Migration backup — separate from website assets

The `notist-migration-2026-11-05` GitHub Release still contains the public Noti.st recovery snapshot: original downloads, audit evidence, reconstruction outputs and review images. Its local copy remains under ignored `preservation/`. This material has not been added to Git; its retention/cold-storage destination is undecided.

To restore or verify that separate snapshot:

```sh
python3 scripts/preservation.py restore
python3 scripts/preservation.py verify
```

Restore verifies the archive checksum and every extracted file; it refuses to overwrite an existing `preservation/` directory. Third-party recording bodies were not mirrored.

The older `portfolio-assets-v1` Release is retained as historical storage. Its `images-*.tar` attachments were slide-image/headshot bundles used by the previous distribution workflow. The current website does not fetch those bundles or its PDF attachments.

No `assets.dark.ca` DNS record or separately deployed website is required by this repository name.
