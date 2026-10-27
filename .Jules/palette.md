## 2024-10-27 - Non-interactive span used as buttons
**Learning:** Found a widespread pattern where non-interactive `<span class="btn">` tags were used as primary call-to-actions, missing out on keyboard accessibility and screen reader focusability.
**Action:** Always replace `<span class="btn">` tags with semantic `<button type="button" class="btn">` for keyboard access and ensure `cursor:pointer`, `font:inherit`, and `:focus-visible` styles are correctly applied.
