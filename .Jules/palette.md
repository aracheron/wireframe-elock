
## 2024-05-24 - Enhance Theme Toggle Button UX & Accessibility
**Learning:** Stateful toggle buttons should clearly communicate the *resulting* state (e.g., "Switch to light mode" / "Switch to dark mode") and use dynamic ARIA labels rather than a generic action like "Toggle". This significantly improves clarity for both sighted users and screen reader users.
**Action:** When implementing toggles, always bind the text and `aria-label` to the inverse of the current active state to provide an actionable description of what clicking the button will do.
