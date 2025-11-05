#!/usr/bin/env python3
"""
Generate PDFs for CNC Engineering Course
Creates individual PDFs for each module and a comprehensive table of contents
"""

import os
import subprocess
from pathlib import Path
from typing import Optional, List, Tuple

# Base directory
BASE_DIR = Path(__file__).parent
MODULES_DIR = BASE_DIR / "Modules"
APPENDICES_DIR = MODULES_DIR / "Appendices"
PRINT_DIR = BASE_DIR / "Print"
PDF_DIR = BASE_DIR / "PDFs"
TEMP_DIR = BASE_DIR / "tmp_pdf"

# Ensure PDF directory exists
PDF_DIR.mkdir(exist_ok=True)
TEMP_DIR.mkdir(exist_ok=True)

# Map problematic Unicode characters to ASCII-safe equivalents for LaTeX
REPLACEMENTS = {
    "\u2260": "!=",
    "\u2264": "<=",
    "\u2265": ">=",
    "\u2070": "^0",
    "\xb9": "^1",
    "\u00b2": "^2",
    "\u00b3": "^3",
    "\u2074": "^4",
    "\u2075": "^5",
    "\u2076": "^6",
    "\u2077": "^7",
    "\u2078": "^8",
    "\u2079": "^9",
    "\u207b": "^-",
    "\u2080": "_0",
    "\u2081": "_1",
    "\u2082": "_2",
    "\u2083": "_3",
    "\u2084": "_4",
    "\u2085": "_5",
    "\u2086": "_6",
    "\u2087": "_7",
    "\u2088": "_8",
    "\u2089": "_9",
    "\u03bc": "mu",
    "\u03b8": "theta",
    "\u03b7": "eta",
    "\u03c1": "rho",
    "\u03a9": "Ohms",
    "\u2713": "[check]",
    "\u2610": "[ ]",
    "\u25a1": "[ ]",
    "\u2500": "-",
    "\u2502": "|",
    "\u250c": "+",
    "\u2510": "+",
    "\u2514": "+",
    "\u2518": "+",
    "\u252c": "+",
    "\u2534": "+",
    "\u251c": "|",
    "\u2524": "|",
    "\u253c": "+",
    "\u2014": "--",
    "\u2013": "-",
    "\u2192": "->",
    "\u2190": "<-",
    "\u00d7": "x",
    "\u00f7": "/",
    "\u00b7": "*",
    "\u00b1": "+/-",
    "\u2212": "-",
    "\u2122": "TM",
    "\u2120": "SM",
    "\xae": "(R)",
    "\uff0c": ",",
    "\uff1a": ":",
    "$": "\\$"
}

def sanitize_text(text: str) -> str:
    """Replace problematic characters with LaTeX-safe alternatives"""
    for old, new in REPLACEMENTS.items():
        text = text.replace(old, new)
    return text

def sanitize_title(title: str) -> str:
    """Sanitize title strings for LaTeX metadata"""
    return title.replace("&", "and").strip()

def prepare_temp_file(source_path: Path, temp_name: Optional[str] = None) -> Path:
    """Create a sanitized copy of the markdown file for PDF conversion"""
    target_name = temp_name or source_path.name
    temp_path = TEMP_DIR / target_name
    with open(source_path, 'r', encoding='utf-8') as src:
        sanitized = sanitize_text(src.read())
    with open(temp_path, 'w', encoding='utf-8') as dst:
        dst.write(sanitized)
    return temp_path

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

def convert_to_pdf(markdown_file, output_pdf, title: str = "", include_toc: bool = True):
    """Convert markdown file to PDF using pandoc with a Unicode-capable engine"""
    try:
        clean_title = sanitize_title(title) if title else ""
        cmd = [
            'pandoc',
            str(markdown_file),
            '-o', str(output_pdf),
            '--pdf-engine=tectonic',
            '-V', 'geometry:margin=1in',
            '-V', 'fontsize=11pt',
            '-V', 'mainfont=Helvetica Neue',
            '-V', 'monofont=Menlo',
            '--standalone'
        ]

        if include_toc:
            cmd.append('--toc')

        if clean_title:
            cmd.extend(['--metadata', f'title={clean_title}'])
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"✓ Created: {output_pdf.name}")
            return True
        else:
            print(f"✗ Failed: {output_pdf.name}")
            print(f"  Error: {result.stderr[:200]}")
            return False
    except Exception as e:
        print(f"✗ Error creating {output_pdf.name}: {e}")
        return False

def merge_module_files(module_dir, output_file):
    """Merge all section files in a module into one file for PDF generation"""
    sections = []
    
    for file in sorted(module_dir.glob("*.md")):
        if file.name.startswith("module-") or file.name == output_file.name:
            continue
        
        with open(file, 'r', encoding='utf-8') as f:
            content = sanitize_text(f.read())
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

    sanitized_toc = prepare_temp_file(toc_file, "table-of-contents-sanitized.md")

    # Convert TOC to PDF
    toc_pdf = PDF_DIR / "00-Table-of-Contents.pdf"
    convert_to_pdf(sanitized_toc, toc_pdf, "CNC Engineering Course - Table of Contents")
    
    return sanitized_toc

def main():
    print("=" * 60)
    print("CNC Engineering Course - PDF Generation")
    print("=" * 60)
    
    # Generate Table of Contents
    print("\n📄 Generating Table of Contents...")
    generate_toc()
    
    # Generate Front Matter PDFs
    print("\n📄 Generating Front Matter PDFs...")
    
    front_matter = [
        (PRINT_DIR / "course-foreword.md", "01-Foreword.pdf", "Foreword"),
        (PRINT_DIR / "course-acknowledgments.md", "02-Acknowledgments.pdf", "Acknowledgments"),
        (PRINT_DIR / "thank-you-to-ai.md", "03-Thank-You-to-AI.pdf", "Thank You to AI"),
        (PRINT_DIR / "course-license.md", "04-License.pdf", "License")
    ]
    
    for source, pdf_name, title in front_matter:
        if source.exists():
            output_pdf = PDF_DIR / pdf_name
            temp_md = prepare_temp_file(source, f"{source.stem}-sanitized.md")
            convert_to_pdf(temp_md, output_pdf, title)
        else:
            print(f"⚠ Warning: {source} not found")
    
    # Generate Module PDFs
    print("\n📄 Generating Module PDFs...")
    
    for module_num in list(range(1, 11)) + list(range(21, 27)):
        module_dir = MODULES_DIR / f"Module-{module_num:02d}"
        
        if not module_dir.exists():
            print(f"⚠ Warning: {module_dir} not found")
            continue
        
        module_name = get_module_name(module_num)
        
        # Create merged module file
        merged_file = module_dir / f"module-{module_num:02d}-complete.md"
        merge_module_files(module_dir, merged_file)
        
        # Convert to PDF
        output_pdf = PDF_DIR / f"Module-{module_num:02d}-{module_name.replace(' ', '-').replace('&', 'and')}.pdf"
        convert_to_pdf(merged_file, output_pdf, f"Module {module_num}: {module_name}")
        
        # Clean up merged file
        merged_file.unlink()
    
    # Generate Appendix PDFs
    print("\n📄 Generating Appendix PDFs...")
    
    for appendix_file in sorted(APPENDICES_DIR.glob("appendix-*.md")):
        letter = appendix_file.stem.split('-')[1].upper()
        name = ' '.join(appendix_file.stem.split('-')[2:]).title()
        
        temp_md = prepare_temp_file(appendix_file, f"{appendix_file.stem}-sanitized.md")
        output_pdf = PDF_DIR / f"Appendix-{letter}-{appendix_file.stem.split('-', 2)[2]}.pdf"
        convert_to_pdf(temp_md, output_pdf, f"Appendix {letter}: {name}")
    
    print("\n" + "=" * 60)
    print("✅ PDF Generation Complete!")
    print(f"📁 PDFs saved to: {PDF_DIR}")
    # Clean up temporary markdown files
    for temp_file in TEMP_DIR.iterdir():
        temp_file.unlink()
    print("=" * 60)

if __name__ == "__main__":
    main()
