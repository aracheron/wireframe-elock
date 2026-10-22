## 2026-10-22 - Roving Tabindex for Custom Tabs
**Learning:** Custom tab implementations often miss WAI-ARIA standards for keyboard navigation. Native buttons are focusable by default, meaning users must tab through every single tab. A roving `tabindex` pattern is needed where only the active tab has `tabindex="0"`, inactive tabs have `tabindex="-1"`, and arrow keys (`ArrowLeft`/`ArrowRight`) are used to switch between tabs.
**Action:** Always check custom tab components for roving `tabindex` and arrow key navigation to ensure standard accessibility compliance.
