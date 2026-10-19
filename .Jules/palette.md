## 2026-10-19 - Accessible Buttons in Wireframes
**Learning:** Using `<span>` elements for buttons in wireframes removes them from the tab order, completely breaking keyboard navigation and making them inaccessible to screen readers.
**Action:** Always add `role="button"` and `tabindex="0"` to interactive `<span>` or `<div>` elements acting as buttons, and ensure they have proper `:focus-visible` styles to show a clear outline when focused.
