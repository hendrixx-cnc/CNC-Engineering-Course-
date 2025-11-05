# CNC Engineering Course - Project Structure

## Repository Organization

```
CNC-Engineering-Course-/
│
├── Communication/                          # Project management & collaboration
│   ├── ai-collaboration.md                # AI collaboration documentation
│   ├── ai-project-lead-rules.md          # Project lead workflow & rules
│   ├── project-structure.md              # This file - overall organization
│   ├── progress-tracker.md               # Detailed progress tracking
│   └── team-communication-log.md         # Communication history
│
├── Modules/                               # Course content (16 modules)
│   ├── Module-01/module-1-mechanical-frame.md      # ✅ COMPLETED
│   ├── module-1-sections-9-15-EXPANDED.md # Supplementary content
│   ├── Module-02/module-2-vertical-axis.md         # ✅ COMPLETED
│   ├── Module-03/module-03-linear-motion.md        # ⏳ PENDING
│   ├── module-04-control-electronics.md  # ⏳ PENDING
│   ├── module-05-plasma.md               # ⏳ PENDING
│   ├── module-06-spindle.md              # ⏳ PENDING
│   ├── module-07-fiber-laser.md          # ⏳ PENDING
│   ├── module-08-waterjet.md             # ⏳ PENDING
│   ├── module-09-pick-place-robot.md     # ⏳ PENDING
│   ├── module-10-robotic-arm.md          # ⏳ PENDING
│   ├── module-11-large-fdm.md            # ⏳ PENDING
│   ├── module-12-hybrid-waterjet-laser.md # ⏳ PENDING
│   ├── module-13-emi-emc.md              # ⏳ PENDING
│   ├── module-14-linuxcnc-hal.md         # ⏳ PENDING
│   ├── module-15-gcode.md                # ⏳ PENDING
│   ├── module-16-cad-dfm.md              # ⏳ PENDING
│   ├── course-acknowledgments.md         # Course metadata
│   ├── course-appendix.md                # Additional resources
│   ├── course-changelog.md               # Version history
│   ├── course-foreword.md                # Introduction
│   └── course-license.md                 # Licensing info
│
├── Visual prompts/                        # Visualization documentation
│   ├── visuals-acknowledgments.md
│   ├── visuals-appendix.md
│   ├── visuals-changelog.md
│   ├── visuals-foreword.md
│   ├── visuals-license.md
│   └── visuals-module-[01-16].md         # Visual guides per module
│
├── .venv/                                 # Python virtual environment
│
└── README.md                              # Repository introduction

```

---

## File Categories

### 1. Communication & Collaboration Files
**Location:** `/Communication/`  
**Purpose:** Project management, AI coordination, progress tracking

| File | Purpose | Updated |
|------|---------|---------|
| `ai-collaboration.md` | Complete project documentation, rules, progress | After each module |
| `ai-project-lead-rules.md` | Workflow protocols for AI Project Lead | As needed |
| `project-structure.md` | Repository organization (this file) | As structure changes |
| `progress-tracker.md` | Detailed task-by-task progress | After each task |
| `team-communication-log.md` | Record of all communications | Every interaction |

---

### 2. Course Module Files
**Location:** `/Modules/`  
**Purpose:** Core educational content (PhD-level technical material)

#### Core Modules (Technical Content)
- `Module-01/module-1-mechanical-frame.md` - Foundation structures
- `Module-02/module-2-vertical-axis.md` - Z-axis design
- `module-03-linear-motion.md` - Motion systems
- `module-04-control-electronics.md` - Electronics & control
- `module-05-plasma.md` - Plasma cutting systems
- `module-06-spindle.md` - Spindle systems
- `module-07-fiber-laser.md` - Laser cutting
- `module-08-waterjet.md` - Waterjet cutting
- `module-09-pick-place-robot.md` - Pick & place automation
- `module-10-robotic-arm.md` - Articulated robots
- `module-11-large-fdm.md` - Large-format 3D printing
- `module-12-hybrid-waterjet-laser.md` - Hybrid systems
- `module-13-emi-emc.md` - EMI/EMC compliance
- `module-14-linuxcnc-hal.md` - LinuxCNC software
- `module-15-gcode.md` - CNC programming
- `module-16-cad-dfm.md` - Design & manufacturing

#### Course Metadata
- `course-acknowledgments.md` - Credits and thanks
- `course-appendix.md` - Supplementary information
- `course-changelog.md` - Version history
- `course-foreword.md` - Course introduction
- `course-license.md` - Usage rights

#### Supplementary Files
- `module-1-sections-9-15-EXPANDED.md` - Overflow content from Module 1

---

### 3. Visual Documentation
**Location:** `/Visual prompts/`  
**Purpose:** Visualization guides and image generation prompts

- Visual guides for each module (01-16)
- Metadata files (acknowledgments, appendix, changelog, foreword, license)

---

### 4. Development Environment
**Location:** `/.venv/`  
**Purpose:** Python virtual environment for development tools

- Python 3.13.7
- Development dependencies
- Scripts and utilities

---

## Workflow Integration

### For AI Project Lead

**Before Starting Any Task:**
1. Read `/Communication/ai-collaboration.md` (full context)
2. Read `/Communication/ai-project-lead-rules.md` (workflow protocols)
3. Check `/Communication/progress-tracker.md` (current status)
4. Review `/Communication/team-communication-log.md` (recent updates)

**After Completing Any Task:**
1. Update `/Communication/ai-collaboration.md` (module completion details)
2. Update `/Communication/progress-tracker.md` (task status)
3. Log in `/Communication/team-communication-log.md` (what was done)
4. Update relevant module file in `/Modules/`

### For Content Development

**Target Files:**
- Work primarily in `/Modules/module-[XX]-[name].md`
- Create supplementary files in `/Modules/` if needed
- Never modify `/Communication/` files during content work
- Update `/Communication/` files only during task start/completion

### For Human Expert Review

**Review Locations:**
- **Progress:** `/Communication/progress-tracker.md`
- **Completed Work:** `/Modules/module-[XX]-[name].md`
- **Project Status:** `/Communication/ai-collaboration.md`
- **Communications:** `/Communication/team-communication-log.md`

---

## File Naming Conventions

### Module Files
- Format: `module-[XX]-[descriptive-name].md`
- Numbers: Use leading zeros (01-16)
- Names: Lowercase, hyphen-separated
- Example: `module-03-linear-motion.md`

### Communication Files
- Format: `[purpose]-[description].md`
- No prefixes with dots (`.`)
- Lowercase, hyphen-separated
- Example: `ai-collaboration.md`

### Supplementary Files
- Format: `module-[XX]-[section-description]-EXPANDED.md`
- Use UPPERCASE for distinguishing keywords
- Example: `module-1-sections-9-15-EXPANDED.md`

---

## Access Patterns

### Daily Work Session
```
1. Start → Read Communication/ files (context)
2. Work → Edit Modules/ files (content)
3. End → Update Communication/ files (progress)
```

### New Module Start
```
1. Read: /Communication/ai-collaboration.md
2. Read: /Modules/module-[XX]-[name].md (original)
3. Plan: Document in communication log
4. Execute: Expand module content
5. Complete: Update all communication files
```

### Quality Review
```
1. Check: /Communication/progress-tracker.md (completion status)
2. Review: /Modules/module-[XX]-[name].md (technical content)
3. Verify: Against /Communication/ai-collaboration.md (standards)
4. Feedback: Log in /Communication/team-communication-log.md
```

---

## Maintenance Schedule

### After Each Module Completion
- [x] Update `ai-collaboration.md` (completion details)
- [x] Update `progress-tracker.md` (task status)
- [x] Update `team-communication-log.md` (completion notice)

### After Every 2-3 Modules
- [ ] Review `project-structure.md` (ensure accurate)
- [ ] Archive old communication logs (if needed)
- [ ] Update progress statistics

### At Project Completion
- [ ] Final update to all Communication/ files
- [ ] Generate project completion report
- [ ] Archive working documents
- [ ] Create final README.md with course overview

---

## Document Relationships

```
ai-collaboration.md (master reference)
        ↓ references
ai-project-lead-rules.md (workflow protocols)
        ↓ drives
progress-tracker.md (task status)
        ↓ records
team-communication-log.md (interaction history)
        ↓ produces
module-[XX]-[name].md (deliverables)
```

---

## Backup & Version Control

### Git Repository
- **Repository:** hendrixx-cnc/CNC-Engineering-Course-
- **Branch:** main
- **Commits:** After each module completion

### Critical Files to Track
- All `/Modules/*.md` files
- All `/Communication/*.md` files
- README.md
- `.venv/` requirements (if applicable)

### Not Tracked
- `.venv/` contents (Python packages)
- Temporary working files
- IDE configurations

---

## Future Expansions

### Planned Additions
- `/Examples/` - Standalone calculation examples
- `/Templates/` - Design calculation templates
- `/References/` - External resource links
- `/Assessments/` - Knowledge check questions

### Potential Structure Changes
- Split large modules into sub-modules if needed
- Add `/Archive/` for superseded versions
- Create `/Index/` for cross-module topics
- Develop `/Glossary/` for terminology

---

**Document Status:** Active  
**Maintained By:** AI Project Lead  
**Last Updated:** November 4, 2025  
**Next Review:** After Module 5 completion  

---

*This structure ensures clear organization, efficient workflow, and easy navigation for all project stakeholders.*
