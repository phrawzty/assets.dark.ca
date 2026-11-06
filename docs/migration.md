# Noti.st migration material

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

The local preservation folder is currently retained. Moving it to cold storage requires a chosen destination and checksum verification before deleting the source. Its Release backup remains in place.
