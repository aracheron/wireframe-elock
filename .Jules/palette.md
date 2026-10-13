## 2024-05-13 - Add Roving Tabindex to Tabs
**Learning:** Native `<button role="tab">` elements without `tabindex` or keyboard event listeners force screen reader / keyboard users to tab sequentially through every tab to reach content. Standard ARIA patterns dictate that the active tab gets `tabindex="0"`, inactive ones `-1`, and arrow keys should navigate between tabs to swap focus.
**Action:** Always implement roving `tabindex` and Left/Right arrow key navigation (with `.focus()`) when building custom tab components to ensure WCAG/ARIA compliance.
