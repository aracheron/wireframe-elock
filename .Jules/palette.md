## 2024-10-24 - Scrollable Regions Keyboard Accessibility
**Learning:** In vanilla HTML implementations without frontend frameworks, `overflow-x: auto` elements (like tables in mobile views) are inaccessible to keyboard-only users who can't scroll them horizontally to read their content. They must be made focusable to allow arrow key scrolling.
**Action:** Always add `tabindex="0"`, `role="region"`, and a descriptive `aria-label` to any scrollable container (e.g., `.scroll` wraps) so users can focus it and navigate its overflow via keyboard.
