# Safety + quality checklist

Before you ship a QR:
- Verify the destination loads fast on mobile.
- Make sure the QR encodes the *final* URL (with UTM if used).
- Test scanning in:
  - bright light
  - dim light
  - from the expected distance
- If it’s a payment/login link, consider using a landing page instead.

Avoid:
- Shorteners you don’t control (harder to trust)
- URLs with spaces or weird characters (always URL-encode)
