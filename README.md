# portfolio.dark.ca assets

Public presentation assets for [Daniel Maher's speaking portfolio](https://github.com/phrawzty/portfolio.dark.ca).

Git tracks `catalog.json`, preservation checksums, and this documentation. Large binaries are attached to GitHub Releases, never committed to Git and never stored in Git LFS.

## Local layout

Clone alongside `portfolio.dark.ca` under the same parent directory (normally `~/repos`).

- `files/`: original-quality PDFs, slide images and headshots used by the authoring tools. Ignored by Git; restored from Releases.
- `preservation/`: public Noti.st downloads, raw audit evidence and reconstructed PDFs. Ignored by Git; backed up separately in the migration Release.
- `releases/`: disposable locally prepared release archives.
- `catalog.json`: mirror of the portfolio's committed `data/asset-releases.json`. The portfolio's copy controls its reproducible builds.
- `preservation-manifest.json`: every preserved file's size and SHA-256, plus the backup archive's download URL, size and SHA-256.

## Everyday publishing

From the portfolio checkout, run `uv run portfolio`, choose **Upload public slides to GitHub**, then commit the updated content and `data/asset-releases.json` and push. Publishing requires GitHub CLI (`gh`) authenticated as an account with write access here. Draft slides are excluded unless explicitly requested with `--include-drafts`.

`uv run portfolio assets fetch --pdfs` restores the authoring cache. Cloudflare fetches only published slide images and headshots; PDF links go directly to Releases. Downloads are checksum-verified. Releases use immutable content-addressed filenames, and the uploader never replaces an existing attachment.

After publishing, commit the updated `catalog.json` here as a convenient inventory. Builds use the manifest in the portfolio repository, so their behavior is independent of when this mirror is committed.

## Migration backup

The `notist-migration-2026-11-05` Release contains a snapshot of public migration evidence, all original downloads, reconstruction outputs and review images. This is separate from the processed assets needed to serve the site. Third-party recording bodies were not mirrored.

To restore it on a new machine:

```sh
python3 scripts/preservation.py restore
python3 scripts/preservation.py verify
```

The restore script verifies the archive before extraction and every file afterwards. It refuses to overwrite an existing `preservation/` directory. Keep the local copy as well as the GitHub copy; a Release is recoverable storage, not a guarantee against account deletion or loss of GitHub access.

No `assets.dark.ca` DNS record or website is required. The name identifies the GitHub repository; public downloads use GitHub Release URLs.
