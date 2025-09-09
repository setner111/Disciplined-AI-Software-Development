# MIT LICENSE - Copyright 2025 Jay Baleine (https://github.com/Varietyz https://banes-lab.com)
"""
Output content formatting and generation
"""
import os
from .config import OUTPUT_DIR, SEPARATE_FILES

def create_combined_content(tree_lines, files_content, title="The Project"):
    tree_section = f'''## 📂 {title} - Current Tree Structure
```
{chr(10).join(tree_lines)}
```

## 📄 Project File Contents

'''
    return f'''<img src="https://banes-lab.com/assets/images/banes_lab/700px_Main_Animated.gif" width="70" />

{tree_section}{files_content}'''

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