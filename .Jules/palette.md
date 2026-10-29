## 2026-10-29 - [Custom Tabs Keyboard Navigation]
**Learning:** Custom tab implementations without standard keyboard accessibility (arrow navigation and roving tabindex) can create significant usability hurdles for keyboard and screen reader users. Standard WAI-ARIA tabbed UI patterns ensure inclusive UX without affecting visual layout.
**Action:** When inspecting custom Javascript components that map to standard native ARIA roles (like tab/tablist), proactively verify WAI-ARIA keyboard navigation specifications and apply them.
