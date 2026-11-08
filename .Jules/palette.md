## 2026-11-08 - Added WAI-ARIA tab navigation for tabs
**Learning:** Adding `tabindex="0"` to the selected tab and `-1` to others (roving tabindex), along with mapping the Arrow keys to shift focus, is essential to make standard `[role="tab"]` elements fully accessible for keyboard and screen-reader users, preventing users from tabbing through all hidden tabs.
**Action:** Next time I encounter `role="tab"` or `role="tablist"` elements, I will proactively check and implement Arrow key navigation and roving tabindex for proper keyboard accessibility.
