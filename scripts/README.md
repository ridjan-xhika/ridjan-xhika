# Profile artwork

Run `python3 scripts/build_assets.py` from the repository root to rebuild the original SVG header, project cards, toolkit, Spotify card, and footer. Commit the generated files in `assets/` with any source changes.

The artwork uses standard SVG and CSS animation, embeds no scripts or external fonts, and respects `prefers-reduced-motion`. The toolkit has a separate mobile layout. Project images wrap onto separate rows on narrow screens.

The Spotify card is decorative artwork linked to a public Spotify playlist, not a live listening-status widget. Update its title in `build_assets.py` and the destination link in `README.md` together when changing playlists. Playback happens in Spotify.

The contribution snake is generated separately by `.github/workflows/snake.yml` each day, using the same teal palette in light and dark variants.
