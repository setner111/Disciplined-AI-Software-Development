# MIT LICENSE - Copyright 2025 Jay Baleine (https://github.com/Varietyz https://banes-lab.com)
import os
from ..config.config import OUTPUT_DIR, SEPARATE_FILES

def create_combined_content(tree_lines, files_content, title="The Project"):
    tree_section = f'''## 📂 {title} - Current Tree Structure
```
{chr(10).join(tree_lines)}
```

## 📄 Project File Contents

'''
    return f'''<img src="https://banes-lab.com/assets/images/banes_lab/700px_Main_Animated.gif" width="70" />

{tree_section}
{files_content}'''

def create_repo_content_collapsible(root_files, directory_sections):
    header = '''# <img src="https://banes-lab.com/assets/images/banes_lab/700px_Main_Animated.gif" width="70" /> Repository Navigation

---
'''
    
    collapsible_sections = []
    
    for section_lines in directory_sections:
        if section_lines:
            section_title = section_lines[0]
            section_content = chr(10).join(section_lines[1:])
            collapsible_sections.append(f'''<details>
<summary>{section_title}</summary>
<pre>
{section_content}
</pre>
</details>''')
    
    final_content = header + chr(10).join(collapsible_sections)
    
    if root_files:
        converted_root_files = []
        for line in root_files:
            if '[' in line and '](' in line and '<a href=' not in line:
                import re
                line = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', line)
            converted_root_files.append(f'- {line}')
        final_content += chr(10) + chr(10) + (chr(10) + chr(10)).join(converted_root_files)
    
    return final_content

def create_repo_content(tree_lines):
    tree_section = chr(10).join(tree_lines)
    return f'''# <img src="https://banes-lab.com/assets/images/banes_lab/700px_Main_Animated.gif" width="70" /> Repository Navigation

---

{tree_section}

---
'''

def save_file(content, filename):
    if SEPARATE_FILES:
        analysis_dir = os.path.join(OUTPUT_DIR)
        os.makedirs(analysis_dir, exist_ok=True)
        output_path = os.path.join(analysis_dir, filename)
    else:
        output_path = filename

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Extraction saved to {output_path}')