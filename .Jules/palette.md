## 2024-05-24 - Scrollable Region Accessibility
**Learning:** Scrollable containers in wireframes (like `.scroll` and `.inner`) aren't inherently keyboard-accessible. This prevents keyboard-only users and screen readers from reading obscured content. Adding `tabindex="0"`, `role="region"`, and an `aria-label` makes them discoverable and navigable.
**Action:** Always verify scrollable text areas and tables have explicit tabindex and ARIA region definitions in wireframes and final implementations.
