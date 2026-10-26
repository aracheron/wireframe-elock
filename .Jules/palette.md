## 2024-05-18 - Roving tabindex pattern
**Learning:** Tab lists must support arrow key navigation per WAI-ARIA standards. Standard `tabindex="0"` on all tabs creates unnecessary tab stops. The roving tabindex pattern (where only the active tab has `tabindex="0"` and others have `tabindex="-1"`) provides a much cleaner navigation experience, allowing users to tab into the active panel and use arrow keys for selection.
**Action:** Always implement roving tabindex + arrow key navigation for tab components, rather than making all tabs focusable via standard tabbing.
