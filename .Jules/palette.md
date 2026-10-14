## $(date +%Y-%m-%d) - [Accessible buttons in wireframes]
**Learning:** Wireframes often use non-semantic elements like `<span>` with classes for buttons to save layout quirks, which breaks tab navigation completely during early reviews and keyboard testing.
**Action:** Replace `<span>` elements masquerading as buttons with actual `<button>` elements, add `:focus-visible` states, and reset `cursor` and `font-family` to maintain the design while preserving accessibility right from the wireframing stage.
