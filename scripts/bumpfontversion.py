# A small derived version of Simon's bumpfontversion for .glyphspackage
# https://github.com/simoncozens/bumpfontversion

import re
import logging
import sys
from glyphsLib import GSFont
from bumpversion.cli import _parse_new_version
from bumpversion.version_part import VersionPart, VersionConfig
from argparse import ArgumentParser

logger = logging.getLogger("bump2fontversion")
parser = r"(?P<major>\d+)\.(?P<minor>\d+)"
serializer = "{major}.{minor}"
vc = VersionConfig(parser, [serializer], None, None)


def main():
    parser = ArgumentParser(
        description="Bump font version in glyphs/glyphspackage format"
    )
    parser.add_argument(
        "--verbose",
        "-V",
        action="store_true",
        default=False,
        help="Print verbose logging to stderr.",
    )

    gp = parser.add_mutually_exclusive_group(required=True)
    gp.add_argument(
        "--new-version",
        metavar="VERSION",
        help="New version that should be in the files",
    )
    gp.add_argument(
        "--part", help="Part of the version to be bumped.", choices=["major", "minor"]
    )

    parser.add_argument(
        "files",
        metavar="file",
        nargs="*",
        help="Files to change",
    )

    args = parser.parse_args()

    if not args.files:
        print("No files to change; nothing to do")
        sys.exit(0)

    if args.verbose:
        logger.setLevel("INFO")

    versions = {}
    new_version = None
    if args.new_version:
        new_version = _parse_new_version(args, None, vc)
        if new_version is None:
            logger.error(f"Bad version {args.new_version}; should be format X.Y")
            sys.exit(1)

    if new_version:
        for path in args.files:
            font = GSFont(path)
            currentMajor = VersionPart(str(font.versionMajor or 0));
            currentMinor = VersionPart(str(font.versionMinor or 0));
            newMajor = int(new_version["major"].value)
            newMinor = int(new_version["minor"].value)
            
            replaced = None

            # We will just replace the text string instead of using a parser's load and dump.
            infopath = f"{path}/fontinfo.plist"
            with open(infopath, "r") as file:
                logger.info(f"Updating font version: {path}")
                txt = file.read()
                
                search = f"versionMajor\\s\\=\\s{currentMajor};"
                replace = f"versionMajor = {newMajor};"
                txt = re.sub(search, replace, txt)
                
                search = f"versionMinor\\s\\=\\s{currentMinor};"
                replace = f"versionMinor = {newMinor};"
                txt = re.sub(search, replace, txt)
                
                replaced = txt
                
            with open(infopath, "w") as file:
                file.write(replaced)
                

if __name__ == "__main__":
    main()
