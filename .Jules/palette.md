## 2026-10-16 - Roving tabindex for standard ARIA tabs
**Learning:** By default, custom tablists using `<button>` elements only support standard `Tab` key navigation. The WAI-ARIA standard requires a "roving tabindex" pattern where arrow keys change the active tab, while `Tab` moves focus into the tabpanel.
**Action:** When implementing custom tab components, always use `tabindex="-1"` on inactive tabs and `tabindex="0"` on the active one, along with arrow key event listeners to move focus.
