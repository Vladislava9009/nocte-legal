# Nocte: privacy and support pages

Privacy Policy and Support pages for the iOS app **Nocte: Breathing & Sleep** (`com.vladislava.nocte`), English.

**Status:** built locally, **not published** (2026-10-29). Publish the same way as tinta-legal: create a public GitHub repository `nocte-legal`, push `main`, turn on GitHub Pages from `main`. Then:

- Privacy URL: `https://vladislava9009.github.io/nocte-legal/privacy.html` → `PRIVACY_URL` in `~/Developer/breathe/src/services/links.ts` and `[PRIVACY_URL]` in `breathe/store/metadata/*/description.txt`;
- Support URL: `https://vladislava9009.github.io/nocte-legal/support.html` → App Store Connect, App Information.

Source: `build.py` (texts inside) → `privacy.html`, `support.html`.

```bash
python3 build.py
```
