#!/usr/bin/env python3
"""Builds privacy.html and support.html for the iOS app Nocte.

Same layout as ~/Developer/tinta-legal, single language (English) for 1.0.
The privacy text mirrors ~/Developer/breathe/docs/PRIVACY.md; keep them in sync.
Publish with GitHub Pages from main, then put the privacy address into
PRIVACY_URL (breathe/src/services/links.ts) and store/metadata/*/description.txt.
"""
import html
import os

EMAIL = "vladislava.bogaturova@gmail.com"
DEV = "Vladyslava Ostapchuk"
UPDATED = "2026-10-29"
APP = "Nocte"

# Colours from the app (breathe/src/theme.ts): warm paper by day, warm night by night.
CSS = """
:root{--bg:#F5F2EC;--surface:#EDE8E0;--fg:#1E1B18;--muted:#6E655B;--accent:#95571B;--rule:#E2DCD2}
@media (prefers-color-scheme:dark){:root{--bg:#12100E;--surface:#1C1916;--fg:#EEE7DD;--muted:#A89D90;--accent:#E7AE72;--rule:#2A2622}}
*{box-sizing:border-box}
body{margin:0;font:17px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;background:var(--bg);color:var(--fg);overflow-wrap:break-word}
header{border-bottom:1px solid var(--rule);padding:22px 16px}
header .in,main{max-width:760px;margin:0 auto}
header h1{margin:0;font-size:28px;letter-spacing:-.4px}
header p{margin:4px 0 0;color:var(--muted)}
main{padding:8px 16px 48px}
h2{margin:28px 0 6px;font-size:19px}
main h1{font-size:24px;margin:20px 0 4px}
em{color:var(--muted)}
a{color:var(--accent)}
ul{padding-left:22px}
footer{max-width:760px;margin:0 auto;padding:0 16px 32px;font-size:14px;color:var(--muted)}
"""

PRIVACY = [
    ("The short version", [
        "Nocte does not collect any data. We have no servers, no accounts and no analytics.",
        "Everything you do in the app (your sessions, saved mixes, settings and reminder times) stays on your iPhone.",
        "Purchases are handled by Apple. We never see your payment details or your Apple ID.",
    ]),
    ("What stays on your iPhone", [
        "The breathing sessions you finish: date and time, practice, length, and your answer to “How do you feel?”; when your sleep timer turned the sound off; your saved sound mixes, the goals you picked on the first screens, your reminder times and app settings.",
        "This information is stored only in the app's storage on your device. It is not uploaded, synced or backed up by us. Your device's own backup (for example iCloud Backup) may include it, according to your device settings; that is controlled by you and Apple. If you delete the app, this information is deleted with it.",
    ]),
    ("Purchases", [
        "Nocte Pro is sold through the App Store. Apple processes the payment and tells the app, on your device, whether you have an active subscription or a lifetime purchase. We do not receive your name, email, payment details or Apple ID. Apple's privacy policy applies to purchases: https://www.apple.com/legal/privacy/",
    ]),
    ("Notifications", [
        "Reminders and notices (for example that a free trial is about to end) are scheduled locally on your iPhone. They are not sent from a server. You can turn them off in the app or in iPhone Settings.",
    ]),
    ("Contacting us", [
        "If you choose “Send feedback”, the app opens a draft email in your mail app with the app version, iOS version and language filled in. You see the text and decide whether to send it. If you send it, we receive your email address and what you wrote, and use them only to reply. We don't add you to any list, and we delete your messages on request.",
    ]),
    ("Children", [
        "Nocte is not directed at children under 13 and does not knowingly collect information from anyone.",
    ]),
    ("Your rights", [
        "Because we don't collect data, there is nothing for us to access, correct or delete, apart from emails you send us. For those, write to the address below. If you are in the EU or UK, you also have the right to complain to your data protection authority.",
    ]),
    ("Changes", [
        "If this policy changes, we will update this page and the date above. If the app ever starts collecting data, we will say so here and in the App Store before it does.",
    ]),
]

SUPPORT = [
    ("Restore a purchase", [
        "Open Nocte, go to Settings and tap Restore purchases, signed in with the Apple ID you used to buy. Nocte Pro comes back on every iPhone with that Apple ID.",
    ]),
    ("Cancel a subscription", [
        "In Nocte: Settings → Manage subscription. Or in iPhone Settings → your name → Subscriptions → Nocte. Cancel at least 24 hours before the end of the period. A free trial can be cancelled the same way; Nocte reminds you two days before it ends if notifications are allowed.",
    ]),
    ("Refunds", [
        "Refunds are handled by Apple, not by us: https://reportaproblem.apple.com",
    ]),
    ("Where your history is kept", [
        "Only on your iPhone. There is no account and no cloud copy kept by us, so we can't restore a deleted history. Your iPhone backup (iCloud or computer) includes it.",
    ]),
    ("Sound or vibration doesn't work", [
        "Vibration during breathing works while the screen is on; check Settings → Sounds & Haptics → System Haptics. If sound doesn't play, check that the side switch and volume are on and that “Breathe over my music” is set the way you want. If something still seems wrong, write to us from Nocte: Settings → Send feedback adds the app version for you.",
    ]),
]


def e(s):
    return html.escape(s, quote=False)


def link(s):
    """Escapes text and turns bare https:// addresses into links."""
    out = []
    for word in e(s).split(" "):
        if word.startswith("https://"):
            url = word.rstrip(".,;")
            out.append(f'<a href="{url}">{url}</a>{word[len(url):]}')
        else:
            out.append(word)
    return " ".join(out)


def page(kind):
    title = "Privacy Policy" if kind == "privacy" else "Support"
    parts = [f"<h1>{title}</h1>"]
    if kind == "privacy":
        parts.append(f"<p><em>Last updated: {UPDATED}. App: Nocte: Breathing &amp; Sleep (iOS). Developer: {e(DEV)}.</em></p>")
        for h, paras in PRIVACY:
            parts.append(f"<h2>{e(h)}</h2>")
            if h == "The short version":
                parts.append("<ul>" + "".join(f"<li>{link(p)}</li>" for p in paras) + "</ul>")
            else:
                parts.extend(f"<p>{link(p)}</p>" for p in paras)
    else:
        parts.append(f'<p>Questions, problems or ideas: <a href="mailto:{EMAIL}">{EMAIL}</a>. We read every message.</p>')
        for h, paras in SUPPORT:
            parts.append(f"<h2>{e(h)}</h2>")
            parts.extend(f"<p>{link(p)}</p>" for p in paras)
    parts.append(f'<h2>Contact</h2><p><a href="mailto:{EMAIL}">{EMAIL}</a></p>')
    html_page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{APP}: {title}</title><meta name="robots" content="index,follow"><style>{CSS}</style></head><body>
<header><div class="in"><h1>{APP}</h1><p>Breathing &amp; sleep sounds · {e(DEV)}</p></div></header>
<main>{''.join(parts)}</main>
<footer><a href="privacy.html">Privacy</a> · <a href="support.html">Support</a><br>© 2026 {e(DEV)}</footer></body></html>"""
    name = f"{kind}.html"
    with open(os.path.join(os.path.dirname(__file__) or ".", name), "w", encoding="utf-8") as f:
        f.write(html_page)
    print("built", name)


if __name__ == "__main__":
    page("privacy")
    page("support")
