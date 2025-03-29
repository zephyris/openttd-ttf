# Default target
.PHONY: all
all: openttd-sans openttd-serif openttd-small openttd-mono

# Fonts
.PHONY: openttd-sans
openttd-sans: openttd-sans/OpenTTD-Sans.ttf
.PHONY: openttd-serif
openttd-serif: openttd-serif/OpenTTD-Serif.ttf
.PHONY: openttd-small
openttd-small: openttd-small/OpenTTD-Small.ttf openttd-small/OpenTTD-SmallCaps.ttf
.PHONY: openttd-mono
openttd-mono: openttd-mono/OpenTTD-Mono.ttf

# TTF files
openttd-sans/OpenTTD-Sans.ttf: openttd-sans/OpenTTD-Sans.sfd
	cd openttd-sans && fontforge build_font.py OpenTTD-Sans.sfd && python3 font_preview.py
openttd-serif/OpenTTD-Serif.ttf: openttd-serif/OpenTTD-Serif.sfd
	cd openttd-serif && fontforge build_font.py OpenTTD-Serif.sfd && python3 font_preview.py
openttd-small/OpenTTD-Small.ttf: openttd-small/OpenTTD-Small.sfd
	cd openttd-small && fontforge build_font.py OpenTTD-Small.sfd && python3 font_preview.py OpenTTD-Small
openttd-small/OpenTTD-SmallCaps.ttf: openttd-small/OpenTTD-SmallCaps.sfd
	cd openttd-small && fontforge build_font.py OpenTTD-SmallCaps.sfd && python3 font_preview.py OpenTTD-SmallCaps
openttd-mono/OpenTTD-Mono.ttf: openttd-mono/OpenTTD-Mono.sfd
	cd openttd-mono && fontforge build_font.py OpenTTD-Mono.sfd && python3 font_preview.py
