#!/bin/bash

# generate otf from fontforge sfd
fontforge build_font.py OpenTTD-Small.sfd

# generate previews
python3 font_preview.py
