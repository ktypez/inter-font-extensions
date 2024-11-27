#!/usr/bin/env python3

from ufomerge import merge_ufos
import ufoLib2
import sys, os
import logging
import fix_encoding

INTER_MASTER="inter/build/ufo-editable/Inter-Display"
glyphset = list(open("glyphsets/GF_Latin_Core.txt").read().splitlines())

logging.getLogger("ufomerge").setLevel(logging.DEBUG)

def main():
    if len(sys.argv) != 2:
        print("Please provide an input UFO.")
        sys.exit(1)
    
    ufo = sys.argv[1]
    
    if (not os.path.exists(ufo)):
        print("The provided UFO does not exist.")
        sys.exit(1)
    
    style = os.path.basename(ufo).split("-")[1].split(".")[0]
    style = "" if style == "Regular" else style
    
    inter_ufo = INTER_MASTER + style + ".ufo"
    
    if (not os.path.exists(inter_ufo)):
        print("The Inter master ufo does not exist: {}".format(inter_ufo))
        sys.exit(1)
        
    ufo_font = ufoLib2.Font.open(ufo)
    inter_ufo_font = ufoLib2.Font.open(inter_ufo)
    
    merge_ufos(
        ufo1=ufo_font,
        ufo2=inter_ufo_font,
        glyphs=glyphset,
        existing_handling="replace",
        layout_handling="subset"
    )
    
    fix_encoding.fix(ufo_font)
    
    ufo_font.save(ufo, overwrite=True)
    
if __name__ == "__main__":
    main()