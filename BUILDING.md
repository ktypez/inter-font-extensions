# Project Building

This project relies on the Makefile and GitHub Actions to build, test, and release the font files. It uses the [googlefonts-project-template](https://github.com/googlefonts/googlefonts-project-template), which implements industry best practices through fonttools, fontmake, and other essential packages for binary font production.

## Building

Fonts are built automatically by GitHub Actions - take a look in the "Actions" tab for the latest build.

If you want to build fonts manually on your own computer:

* `make build` will produce all font files.
* `make build-only-var` will produce only variable font files.
* `make test` will run [FontBakery](https://github.com/googlefonts/fontbakery)'s quality assurance tests.
* `make proof` will generate HTML proof files.

## Directories

### `features/`

Contains Inter's feature files required for building. Note that when UFO files are merged, the `include` statements are relative to the outer directory.

### `recipeproviders/`

Houses a custom recipe configuration for building all font sources with `gftools builder`.

### `glyphsets/`

Contains a modified `GF_Latin_Core` set with additional glyphs for building:

- `tcedilla`
- `drthook`
- `uni021A`
- `commabelowcmb`
- `acutedblcomb`
- `uni012F.ccmp`

### `scripts/`

Collection of Python utilities to assist the building process:

* `bumpfontversion.py` – A small derived version of Simon's [bumpfontversion](https://github.com/simoncozens/bumpfontversion) for .glyphspackage.
* `config-for-vf.py` – Temporarily create yaml configs for `build-only-var` build target.
* `fix_encoding.py` – Remap the encoding for some glyphs to match the latest Inter's sources.
* `process-merge.py` – Process the merging each script and Inter's Latin sources.