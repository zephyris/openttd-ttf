#!/usr/bin/python3

# Checks characters used in OpenTTD strings against characters present in these fonts

# Usage:
# python3 checkTranslationChars.py path/to/openttd/src/lang
# python3 path/to/checkTranslationChars.py [run in openttd/src/lang]

import glob, os, sys
from fontTools.ttLib import TTFont

if len(sys.argv) > 1:
  langpath = sys.argv[1]
else:
  langpath = "."

# maximum number of missing characters to list in full
maxlist = 100

# find all ttfs by suffix in directory
suffix = ".ttf"
scriptpath = os.path.dirname(os.path.realpath(__file__))
files = [
  os.path.join(scriptpath, "openttd-sans", "OpenTTD-Sans.ttf"),
  os.path.join(scriptpath, "openttd-serif", "OpenTTD-Serif.ttf"),
  os.path.join(scriptpath, "openttd-mono", "OpenTTD-Mono.ttf"),
  os.path.join(scriptpath, "openttd-small", "OpenTTD-Small.ttf"),
  os.path.join(scriptpath, "openttd-small", "OpenTTD-SmallCaps.ttf")
]
fonts = []
for file in files:
  # for each font, record name and list of character codes available
  font = TTFont(file)
  fonts.append({
    "name": os.path.basename(file[:-len(suffix)]),
    "codes": list(font.getBestCmap().keys())
  })

# find all lang files by suffix in directory
suffix = ".txt"
files = glob.glob(os.path.join(langpath, "*" + suffix))
print(os.path.join(langpath, "*" + suffix))
for file in files:
  # for each language
  lang = os.path.basename(file[:-len(suffix)])
  with open(file, "r") as handle:
    # read lines and remove empty lines
    strings = [x for x in handle.read().splitlines() if x]
    # extract translated strings
    strings = [x[x.find(":") + 1:] for x in strings if x[0] != "#"]
    # list all character codes and characters across strings
    codes = sorted(list(set([ord(x) for x in "".join(strings)])))
    chars = [chr(x) for x in codes]
    # check if fully supported by each font
    print(lang)
    completecount = 0
    for font in fonts:
      missing = [x for x in codes if x not in font["codes"]]
      if len(missing) == 0:
        completecount += 1
      else:
        if len(missing) <= maxlist:
          print("", font["name"], "missing "+str(len(missing))+":", "("+"".join([chr(x) for x in missing])+")")
        else:
          print("", font["name"], "missing "+str(len(missing))+":", "[too many to list]")
    if completecount == len(fonts):
      print("", "[complete]")