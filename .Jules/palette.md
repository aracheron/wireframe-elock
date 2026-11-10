## 2024-11-10 - Roving Tabindex for Tablists prevents Tab Fatigue
**Learning:** When multiple `<button role="tab">` elements are grouped in a tablist, keeping all of them in the normal document tab flow causes severe "tab fatigue" for keyboard users, who are forced to tab through every inactive tab to reach the main content.
**Action:** Always implement a roving `tabindex` (where the active tab has `tabindex="0"` and inactive tabs have `tabindex="-1"`) combined with standard arrow key (`ArrowLeft`, `ArrowRight`, `Home`, `End`) navigation within the tablist.
