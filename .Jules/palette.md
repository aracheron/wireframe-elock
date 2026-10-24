## 2024-10-24 - ARIA roles on generic elements and theme toggle state
**Learning:** Screen readers ignore aria-label on generic <div> elements unless they have semantic roles (like group or region). Also, theme toggles should use aria-pressed to communicate their state.
**Action:** Always assign role="group" or role="region" to <div>s that use aria-label, and use aria-pressed for toggle buttons.
