#!/usr/bin/fontforge

import sys

font = fontforge.open(sys.argv[1])
font.ascent = 600
font.descent = 000
font.generate(sys.argv[1][:-3] + "ttf")
#font.generate(sys.argv[1][:-3] + "otf")
#font.save("tmp.sfd")
