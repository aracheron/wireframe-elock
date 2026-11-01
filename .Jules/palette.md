## 2024-05-24 - Semantic Button Elements
**Learning:** The app design heavily relies on `<span>` tags styled as buttons (e.g., `<span class="btn">`). This is a recurring accessibility anti-pattern in this specific codebase, breaking keyboard navigation (tabbing), screen reader support, and lacking default interaction styles like `cursor: pointer`.
**Action:** Always prefer native `<button>` elements over styled spans to ensure semantic meaning and native focus behavior, and explicitly style `.btn:focus-visible` to ensure keyboard focus states are clear and visible.
