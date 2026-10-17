## 2023-10-24 - Exposing Keyboard Shortcuts Visually
**Learning:** Adding global keyboard shortcuts to tools (like a theme toggler) significantly enhances the experience for power users, but they go unused if they are hidden. Adding visual affordances such as a `<kbd>` tag and configuring `aria-keyshortcuts` helps screen reader users and sighted users discover these conveniences effortlessly.
**Action:** When adding functional keyboard shortcuts to a generic UI, make sure to add both a `<kbd>` tag to visually hint the key, and use `aria-keyshortcuts` to expose it to assistive tech.
