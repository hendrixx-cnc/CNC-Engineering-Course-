#!/usr/bin/env python3
"""
Generate PDFs for CNC Engineering Course using HTML intermediate
Creates individual PDFs for each module and a comprehensive table of contents
"""

import os
import subprocess
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).parent
MODULES_DIR = BASE_DIR / "Modules"
APPENDICES_DIR = MODULES_DIR / "Appendices"
PRINT_DIR = BASE_DIR / "Print"
PDF_DIR = BASE_DIR / "PDFs"
HTML_DIR = BASE_DIR / "HTML"

# Ensure directories exist
PDF_DIR.mkdir(exist_ok=True)
HTML_DIR.mkdir(exist_ok=True)

def get_module_name(module_num):
    """Get module name from module master outline file"""
    module_names = {
        1: "Mechanical Frame & Structure",
        2: "Vertical Axis & Z-Stage",
        3: "Linear Motion",
        4: "Control Electronics",
        5: "Plasma Cutting",
        6: "Spindle & Rotary Tools",
        7: "Fiber Laser",
        8: "Waterjet Cutting",
        9: "Pick & Place Robot",
        10: "Robotic Arm",
        21: "Metrology and Precision Measurement",
        22: "Quality Management Systems (QMS)",
        23: "Shop Organization and Management",
        24: "L.E.A.N. Strategies for CNC Manufacturing",
        25: "Work-Life Balance in CNC Manufacturing",
        26: "CNC Business Ownership and Management"
    }
    return module_names.get(module_num, f"Module {module_num}")

def convert_to_html(markdown_file, output_html, title=""):
    """Convert markdown file to HTML using pandoc"""
    try:
        cmd = [
            'pandoc',
            str(markdown_file),
            '-o', str(output_html),
            '--standalone',
            '--toc',
            '--css=style.css',
            '-V', 'geometry:margin=1in',
            '--metadata', f'title={title}' if title else 'title=CNC Engineering Course'
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"✓ Created HTML: {output_html.name}")
            return True
        else:
            print(f"✗ Failed: {output_html.name}")
            print(f"  Error: {result.stderr[:200]}")
            return False
    except Exception as e:
        print(f"✗ Error creating {output_html.name}: {e}")
        return False

def create_css():
    """Create a nice CSS file for the HTML output"""
    css_content = """
body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    line-height: 1.6;
    max-width: 900px;
    margin: 0 auto;
    padding: 20px;
    color: #333;
}

h1 {
    color: #2c3e50;
    border-bottom: 3px solid #3498db;
    padding-bottom: 10px;
}

h2 {
    color: #34495e;
    margin-top: 30px;
    border-bottom: 2px solid #ecf0f1;
    padding-bottom: 8px;
}

h3 {
    color: #7f8c8d;
    margin-top: 20px;
}

code {
    background-color: #f4f4f4;
    padding: 2px 6px;
    border-radius: 3px;
    font-family: 'Monaco', 'Menlo', 'Courier New', monospace;
}

pre {
    background-color: #f4f4f4;
    padding: 15px;
    border-radius: 5px;
    overflow-x: auto;
}

table {
    border-collapse: collapse;
    width: 100%;
    margin: 20px 0;
}

th, td {
    border: 1px solid #ddd;
    padding: 12px;
    text-align: left;
}

th {
    background-color: #3498db;
    color: white;
}

tr:nth-child(even) {
    background-color: #f9f9f9;
}

blockquote {
    border-left: 4px solid #3498db;
    padding-left: 20px;
    margin-left: 0;
    color: #555;
    font-style: italic;
}

a {
    color: #3498db;
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}

#TOC {
    background-color: #f8f9fa;
    padding: 20px;
    border-radius: 5px;
    margin-bottom: 30px;
}

#TOC ul {
    list-style-type: none;
}

@media print {
    body {
        max-width: 100%;
    }
    
    @page {
        margin: 1in;
    }
}
"""
    
    css_file = HTML_DIR / "style.css"
    with open(css_file, 'w', encoding='utf-8') as f:
        f.write(css_content)
    
    print("✓ Created style.css")

def merge_module_files(module_dir, output_file):
    """Merge all section files in a module into one file for PDF generation"""
    sections = []
    
    for file in sorted(module_dir.glob("*.md")):
        if file.name.startswith("module-") or file.name == output_file.name:
            continue
        
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            sections.append(content)
            sections.append("\n\n---\n\n")  # Page break
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("\n".join(sections))

def generate_toc():
    """Generate comprehensive table of contents"""
    toc_content = """# CNC Engineering Course
## Table of Contents

**Author**: Todd  
**Company**: Hendrixx Design  
**Contact**: todd@hendrixxdesign.com

---

## Front Matter

1. **Foreword** - A Word from the Author
2. **Acknowledgments** - Recognition of Contributors
3. **Thank You to AI** - Collaboration with AI Tools
4. **License** - Course Terms and Conditions

---

## Course Modules

### Foundation Modules (1-4)

"""
    
    # Add modules 1-10
    for i in range(1, 11):
        module_name = get_module_name(i)
        toc_content += f"**Module {i:02d}**: {module_name}\n\n"
    
    toc_content += "\n### Professional Development Modules (21-26)\n\n"
    
    # Add modules 21-26
    for i in range(21, 27):
        module_name = get_module_name(i)
        toc_content += f"**Module {i}**: {module_name}\n\n"
    
    toc_content += "\n---\n\n## Appendices\n\n"
    
    # Add appendices
    appendix_names = {
        'A': 'Material Properties',
        'B': 'Hardware Specifications',
        'C': 'Motor Drive Sizing',
        'D': 'Linear Motion',
        'E': 'Electrical Standards',
        'F': 'G-code Reference',
        'G': 'Safety Standards',
        'H': 'Lubrication',
        'I': 'Conversions',
        'J': 'Troubleshooting',
        'K': 'Vendors',
        'L': 'Resources',
        'M': 'Glossary',
        'N': 'Contact',
        'O': 'Updates',
        'P': 'Mathematics',
        'Q': 'QMS Templates',
        'R': 'Organization Templates',
        'S': 'LEAN Manufacturing Templates (2,910 lines)',
        'T': 'Business Ownership Templates (6,612 lines)'
    }
    
    for letter, name in appendix_names.items():
        toc_content += f"**Appendix {letter}**: {name}\n\n"
    
    toc_content += "\n---\n\n## Course Information\n\n"
    toc_content += "**Total Modules**: 26 comprehensive modules\n\n"
    toc_content += "**Total Appendices**: 20 reference appendices (including 9,500+ lines of templates)\n\n"
    toc_content += "**Course Scope**: Foundation through advanced topics and business ownership\n\n"
    toc_content += "**Target Audience**: Entry-level through experienced professionals and entrepreneurs\n\n"
    toc_content += "\n---\n\n"
    toc_content += "*Course Version 1.0 | Last Updated: November 2025*\n"
    
    # Write TOC
    toc_file = BASE_DIR / "table-of-contents.md"
    with open(toc_file, 'w', encoding='utf-8') as f:
        f.write(toc_content)
    
    print(f"\n✓ Created: table-of-contents.md")
    
    # Convert TOC to HTML
    toc_html = HTML_DIR / "00-Table-of-Contents.html"
    convert_to_html(toc_file, toc_html, "CNC Engineering Course - Table of Contents")
    
    return toc_file

def create_print_instructions():
    """Create instructions for printing to PDF"""
    instructions = """# How to Create PDFs from HTML Files

The HTML files have been generated in the `HTML/` directory.

## Method 1: Using Chrome/Edge Browser (Recommended)

1. Open each HTML file in Chrome or Microsoft Edge
2. Press `Cmd+P` (Mac) or `Ctrl+P` (Windows) to open Print dialog
3. Select "Save as PDF" as the destination
4. Click "Save" and choose the `PDFs/` directory
5. The PDF will preserve all formatting, Unicode characters, and tables

## Method 2: Using Safari (Mac)

1. Open each HTML file in Safari
2. Click File → Export as PDF
3. Save to the `PDFs/` directory

## Method 3: Bulk Conversion (Advanced)

If you want to convert all HTML files to PDF at once, you can install wkhtmltopdf:

```bash
brew install wkhtmltopdf  # On Mac
```

Then run:

```bash
cd HTML
for file in *.html; do
    wkhtmltopdf "$file" "../PDFs/${file%.html}.pdf"
done
```

## Files Generated

The following HTML files are ready for conversion:

- 00-Table-of-Contents.html
- 01-Foreword.html
- 02-Acknowledgments.html
- 03-Thank-You-to-AI.html
- 04-License.html
- Module-01 through Module-10 (Foundation modules)
- Module-21 through Module-26 (Professional modules)
- Appendix-A through Appendix-T (All appendices)

## Note

HTML files can be viewed directly in any web browser and printed to PDF individually
or in batches. The CSS styling ensures professional appearance in print.
"""
    
    instructions_file = HTML_DIR / "README-PRINTING.md"
    with open(instructions_file, 'w', encoding='utf-8') as f:
        f.write(instructions)
    
    print("\n✓ Created printing instructions: HTML/README-PRINTING.md")

def main():
    print("=" * 60)
    print("CNC Engineering Course - HTML/PDF Generation")
    print("=" * 60)
    
    # Create CSS
    print("\n📄 Creating stylesheet...")
    create_css()
    
    # Generate Table of Contents
    print("\n📄 Generating Table of Contents...")
    generate_toc()
    
    # Generate Front Matter HTMLs
    print("\n📄 Generating Front Matter HTMLs...")
    
    front_matter = [
        (PRINT_DIR / "course-foreword.md", "01-Foreword.html", "Foreword"),
        (PRINT_DIR / "course-acknowledgments.md", "02-Acknowledgments.html", "Acknowledgments"),
        (PRINT_DIR / "thank-you-to-ai.md", "03-Thank-You-to-AI.html", "Thank You to AI"),
        (PRINT_DIR / "course-license.md", "04-License.html", "License")
    ]
    
    for source, html_name, title in front_matter:
        if source.exists():
            output_html = HTML_DIR / html_name
            convert_to_html(source, output_html, title)
        else:
            print(f"⚠ Warning: {source} not found")
    
    # Generate Module HTMLs
    print("\n📄 Generating Module HTMLs...")
    
    for module_num in list(range(1, 11)) + list(range(21, 27)):
        module_dir = MODULES_DIR / f"Module-{module_num:02d}"
        
        if not module_dir.exists():
            print(f"⚠ Warning: {module_dir} not found")
            continue
        
        module_name = get_module_name(module_num)
        
        # Create merged module file
        merged_file = module_dir / f"module-{module_num:02d}-complete.md"
        merge_module_files(module_dir, merged_file)
        
        # Convert to HTML
        output_html = HTML_DIR / f"Module-{module_num:02d}-{module_name.replace(' ', '-').replace('&', 'and')}.html"
        convert_to_html(merged_file, output_html, f"Module {module_num}: {module_name}")
        
        # Clean up merged file
        merged_file.unlink()
    
    # Generate Appendix HTMLs
    print("\n📄 Generating Appendix HTMLs...")
    
    for appendix_file in sorted(APPENDICES_DIR.glob("appendix-*.md")):
        letter = appendix_file.stem.split('-')[1].upper()
        name = ' '.join(appendix_file.stem.split('-')[2:]).title()
        
        output_html = HTML_DIR / f"Appendix-{letter}-{appendix_file.stem.split('-', 2)[2]}.html"
        convert_to_html(appendix_file, output_html, f"Appendix {letter}: {name}")
    
    # Create printing instructions
    create_print_instructions()
    
    print("\n" + "=" * 60)
    print("✅ HTML Generation Complete!")
    print(f"📁 HTML files saved to: {HTML_DIR}")
    print(f"📁 PDFs will be saved to: {PDF_DIR}")
    print("\nTo convert to PDF:")
    print("  1. Open HTML files in Chrome/Edge")
    print("  2. Press Cmd+P and select 'Save as PDF'")
    print("  3. Or see HTML/README-PRINTING.md for details")
    print("=" * 60)

if __name__ == "__main__":
    main()
