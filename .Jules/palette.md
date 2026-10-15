## 2026-10-15 - Tab component accessibility
**Learning:** Native tab interfaces typically require custom javascript to replicate proper WAI-ARIA behavior, including dynamic `tabindex` switching (`0` on active, `-1` on inactive) and keyboard arrow navigation (`ArrowRight` and `ArrowLeft`).
**Action:** When auditing custom tablists, specifically look for missing `tabindex` toggling and arrow key navigation listeners. Do not assume standard click handlers are sufficient for screen readers and keyboard users.
