import sys

files_to_check = ["index.html.html", "Elock website wireframes.html"]

for filepath in files_to_check:
    with open(filepath, 'r') as f:
        content = f.read()

    if 'role="group" aria-label="Legend"' not in content:
        print(f"Error: role='group' not found in {filepath}")
        sys.exit(1)

    if 'aria-pressed="false"' not in content and 'aria-pressed="true"' not in content:
        print(f"Error: aria-pressed not found in {filepath}")
        sys.exit(1)

    if "btn.setAttribute('aria-pressed'" not in content:
        print(f"Error: aria-pressed toggle not found in JS of {filepath}")
        sys.exit(1)

print("All static checks passed successfully!")
