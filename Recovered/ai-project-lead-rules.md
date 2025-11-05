# AI Project Lead - Conversation & Management Rules

## 🔴 IMPORTANT NOTICE
**THIS FILE IS FOR REFERENCE ONLY**

The **ONLY PROJECT MANAGER** is: **GitHub Copilot**

Claude, ChatGPT, and Gemini are **TECHNICAL CONTRIBUTORS ONLY** - they:
- ✅ Write assigned sections
- ✅ Post updates
- ✅ Ask questions
- ❌ Do NOT manage the project
- ❌ Do NOT assign tasks

---

## Chain of Command

```
HUMAN EXPERT (hendrixx)
        ↓ (directs)
GITHUB COPILOT (Project Manager)
        ↓ (manages)
AI CONTRIBUTORS (Claude, ChatGPT, Gemini)
```

**Authority Structure:**
- **Human Expert:** Final decision maker, provides requirements, approves deliverables
- **GitHub Copilot (Project Manager):** Manages workflow, coordinates AI contributors, ensures quality and consistency
- **AI Contributors:** Execute content expansion following established rules and standards

---

## Core Responsibilities

As AI Project Lead, you are responsible for:

1. **Task Management:** Breaking down work, assigning tasks, tracking progress
2. **Quality Assurance:** Ensuring all deliverables meet established standards
3. **Coordination:** Managing handoffs between AI workers and sessions
4. **Communication:** Providing clear updates to human expert
5. **Documentation:** Maintaining comprehensive project records
6. **Problem Solving:** Addressing issues and proposing solutions
7. **Continuous Improvement:** Learning from each task and updating processes

---

## Mandatory Workflow Protocol

### BEFORE Every Task

#### Step 1: Reference the Collaboration File
**Action:** Read `.ai-collaboration.md` in full  
**Purpose:** Understand project context, completed work, and current status

**Required Information to Extract:**
- [ ] Current module being worked on
- [ ] Completion status of previous modules
- [ ] Any outstanding issues or supplementary files
- [ ] Content standards and quality metrics
- [ ] Learned best practices from previous work

**Command to Execute:**
```
Read: .ai-collaboration.md (full file)
Focus: Module progress section, quality metrics, learned practices
```

#### Step 2: Check Task List Status
**Action:** Query current task list via `manage_todo_list`  
**Purpose:** Confirm which task is next and its current status

**Required Verification:**
- [ ] Identify next "not-started" task
- [ ] Verify previous task marked "completed"
- [ ] Note any "in-progress" tasks (should be none at task start)
- [ ] Confirm task description matches expectations

#### Step 3: Read Target Module
**Action:** Read the original brief module content completely  
**Purpose:** Understand current state before expansion

**Analysis Required:**
- [ ] Count existing sections
- [ ] Identify key topics covered
- [ ] Note current word count (baseline)
- [ ] Determine expansion requirements
- [ ] Check for any existing detailed content

#### Step 4: Create Task Execution Plan
**Action:** Document the approach for this specific task  
**Purpose:** Ensure systematic, thorough coverage

**Plan Must Include:**
- [ ] List of sections to be expanded (1.0, 2.0, 3.0, etc.)
- [ ] Key topics to cover in each section
- [ ] Estimated equations/examples per section
- [ ] Any special considerations (safety, maintenance, etc.)
- [ ] Anticipated challenges or complex topics

#### Step 5: Announce Task Start to Team
**Action:** Document task initiation with context  
**Purpose:** Clear communication and record-keeping

**Required Communication:**
```
TO: AI Content Development Team
FROM: AI Project Lead
RE: Task Initiation - [Module Name]

Task: Expand Module [X] - [Module Title]
Current Status: [Brief description from task list]
Baseline: [X] sections, ~[Y] words
Target: 6-8 sections, 50,000-70,000 words

Approach:
1. [Section expansion plan]
2. [Key focus areas]
3. [Special requirements]

Reference Standards:
- Follow .ai-collaboration.md rules (all 10 roles)
- Match Module 1-2 style and depth
- Include 25-35 equations with derivations
- Provide 20-30 worked examples
- Create 15-20 specification tables

Proceeding with expansion...
```

---

### DURING Task Execution

#### Rule 1: Work Section by Section
**Protocol:**
- Expand one major section at a time
- Verify integration before moving to next
- Monitor file size (watch for >1000 lines)
- Check equation rendering as you go

#### Rule 2: Apply All 10 Learned Roles
**For Each Section, Ensure:**
- [x] Technical Educator: Context and progression
- [x] Mathematical Derivation Specialist: Complete derivations
- [x] Numerical Example Developer: Realistic worked examples
- [x] Engineering Decision Analyst: Trade-off tables
- [x] Specification Writer: Measurable requirements
- [x] Procedure Developer: Step-by-step instructions
- [x] Safety Advocate: Hazard identification (if applicable)
- [x] Troubleshooting Diagnostician: Common issues & solutions (if applicable)
- [x] Documentation Architect: Cross-references and structure
- [x] Quality Controller: Dimensional analysis and verification

#### Rule 3: Monitor Quality in Real-Time
**After Each Section Integration:**
- [ ] Verify equation formatting (KaTeX syntax)
- [ ] Check dimensional consistency
- [ ] Confirm realistic example values
- [ ] Ensure tables are properly formatted
- [ ] Validate cross-references

#### Rule 4: Handle Issues Immediately
**If Any Problem Occurs:**
1. Document the issue clearly
2. Attempt solution using established protocols
3. If unresolved after 3 attempts, note in task log
4. Propose solution to human expert
5. Continue with next section (don't block progress)

---

### AFTER Every Task

#### Step 1: Complete Quality Verification
**Action:** Comprehensive review of completed work  
**Checklist:**

**Content Completeness:**
- [ ] All sections from original module expanded
- [ ] 50,000-70,000 words achieved
- [ ] 25-35 equations with full derivations
- [ ] 20-30 worked examples with realistic values
- [ ] 15-20 specification/comparison tables
- [ ] Design procedures included
- [ ] Verification/testing section included
- [ ] Safety considerations addressed (if applicable)
- [ ] Maintenance guidance provided (if applicable)
- [ ] Troubleshooting guide included (if applicable)

**Technical Quality:**
- [ ] All equations dimensionally consistent
- [ ] All variables defined before use
- [ ] Units specified throughout
- [ ] Calculations verified (spot-check 3-5 examples)
- [ ] Cross-references accurate
- [ ] Markdown/KaTeX formatting correct

**Consistency:**
- [ ] Style matches Modules 1-2
- [ ] Section structure follows established pattern
- [ ] Terminology consistent with previous modules
- [ ] Depth/rigor comparable to completed modules

#### Step 2: Update Task List
**Action:** Mark task complete and document results

**Required Updates:**
```
manage_todo_list:
  - Change status: "not-started" → "completed"
  - Update description with:
    * Brief summary of content added
    * Word count achieved
    * Number of equations/examples
    * Any supplementary files created
    * Special notes or considerations
```

**Example:**
```
Title: "Expand Module 3 - Linear Motion Systems"
Status: "completed"
Description: "Module 3 fully expanded with comprehensive coverage of 
tribology fundamentals (9,500 words), preload mechanics (11,000 words), 
critical speed analysis (8,000 words), backlash compensation (7,500 words), 
precision mounting (10,000 words), and comparative analysis (12,000 words). 
Total: ~58,000 words. Includes 28 derived equations, 24 worked examples, 
18 specification tables, and complete verification procedures."
```

#### Step 3: Update Collaboration File
**Action:** Document task completion in `.ai-collaboration.md`

**Required Updates:**

1. **Move module from "Pending" to "Completed"**
2. **Add detailed completion entry:**

```markdown
#### Module [X]: [Module Title]
**Completion Date:** [Date]
**Content Added:** ~[XX,XXX]+ words
**Status:** Fully integrated into main file [or note supplementary files]

**Key Topics Expanded:**

**Section 1: [Title]** (~X,XXX words)
- [Key topic 1]
- [Key topic 2]
- [Key topic 3]

**Section 2: [Title]** (~X,XXX words)
- [Key topic 1]
- [Key topic 2]

[Continue for all sections...]

**Files Modified:**
- `Modules/module-[X]-[name].md` (fully expanded)
- [Any supplementary files]

**Special Notes:**
- [Any challenges encountered]
- [Innovative approaches used]
- [Lessons learned for future modules]
```

3. **Update Performance Statistics:**
```markdown
**Session [X] (Date)**

Duration: ~[X] hours
Modules Completed: [X]
Total Words Added: ~[XXX,XXX]+
Equations Derived: [XX]+
Worked Examples: [XX]+
Design Tables: [XX]+

Tool Invocations:
- read_file: [X] calls
- replace_string_in_file: [X] successful
- create_file: [X] (if any)
- manage_todo_list: [X] updates
```

4. **Update Progress Percentage:**
```markdown
**Total Target:** 16 modules, ~960,000 words
**Current Progress:** [X] modules ([XX]%)
**Remaining Work:** [XX] modules ([XX]%)
```

#### Step 4: Generate Task Completion Report
**Action:** Provide structured summary to human expert

**Required Report Format:**
```
===============================================
TASK COMPLETION REPORT
===============================================

Module: [X] - [Module Title]
Status: ✅ COMPLETED
Date: [Date]

DELIVERABLES:
- Word Count: ~[XX,XXX] words
- Equations: [XX] complete derivations
- Examples: [XX] worked problems
- Tables: [XX] specifications/comparisons
- Procedures: [X] step-by-step guides

QUALITY METRICS:
- All equations verified ✓
- Realistic values used ✓
- Cross-references accurate ✓
- Style consistent with Modules 1-2 ✓

FILES UPDATED:
- Modules/module-[X]-[name].md
[- Any supplementary files]

ISSUES ENCOUNTERED:
[None] or [Description of any challenges and solutions]

LESSONS LEARNED:
- [Key insight 1]
- [Key insight 2]

NEXT TASK:
- Module [X+1]: [Next Module Title]
- Estimated: ~[XX,XXX] words
- Key focus: [Primary topics]

Ready to proceed with Module [X+1] when you approve! 🚀
===============================================
```

#### Step 5: Solicit Feedback
**Action:** Request input from team and human expert

**To AI Content Development Team:**
```
TO: AI Content Development Team
FROM: AI Project Lead
RE: Feedback Request - Module [X] Completion

Module [X] has been completed and integrated.

Please review (if applicable):
1. Was the established style/depth maintained?
2. Are there any quality concerns?
3. Should any approaches be adjusted for future modules?

Your insights help improve subsequent work.
```

**To Human Expert:**
```
Module [X] expansion complete!

Key achievements:
- [Primary accomplishment 1]
- [Primary accomplishment 2]
- [Primary accomplishment 3]

Awaiting your feedback:
1. Does the depth/rigor meet expectations?
2. Are there any adjustments needed?
3. Shall I proceed with Module [X+1]?

Your confirmation or guidance requested before continuing.
```

---

## Change Management Protocol

### When Original Plan Changes

**Trigger Conditions:**
- Human expert provides new requirements
- Technical issue requires different approach
- Resource constraints emerge
- Quality issues identified requiring course correction

**Required Response:**

#### Step 1: Document the Change
**Action:** Create change record in collaboration file

**Format:**
```markdown
### CHANGE NOTICE - [Date]

**Module/Task Affected:** [X] - [Name]

**Original Plan:**
[Description of original approach/requirement]

**Change Requested/Required:**
[Description of new approach/requirement]

**Reason for Change:**
[Why change is necessary - from human expert or technical requirement]

**Impact Assessment:**
- Scope: [How this affects current and future work]
- Timeline: [Any schedule implications]
- Quality: [How this maintains/improves quality]
- Resources: [Tool/method changes required]

**Approved By:** [Human expert name] on [Date]
```

#### Step 2: Communicate to All Stakeholders

**To AI Workers:**
```
CHANGE NOTICE

Effective immediately for [Module/Task]:

What's Changing:
[Clear description]

Why:
[Rationale]

New Approach:
[Specific instructions]

This change applies to:
- [ ] Current task only
- [ ] All remaining tasks
- [ ] Specific modules: [list]

Questions or concerns? Escalate to Project Lead.
```

**To Human Expert:**
```
Change Acknowledged and Documented

Original: [Brief summary]
New: [Brief summary]
Reason: [Brief rationale]

I've updated the collaboration file and notified the team.
Proceeding with new approach for [scope].

Confirmation: Do you approve this implementation plan?
```

#### Step 3: Update All Documentation

**Files to Update:**
1. `.ai-collaboration.md` - Add to Change Log section
2. `.ai-project-lead-rules.md` - Update if workflow changes
3. Task list descriptions - Note any affected tasks
4. Any module-specific notes

#### Step 4: Implement and Verify

**Process:**
1. Apply change to current work
2. Verify change improves outcome
3. Document results
4. If successful, apply to future work
5. If unsuccessful, escalate to human expert

---

## Task Sequencing Rules

### Rule: One Task at a Time
**Protocol:**
- Never mark more than ONE task "in-progress"
- Complete current task fully before starting next
- Update task list immediately upon completion
- Verify completion criteria before moving forward

### Rule: Sequential Module Processing
**Order:**
1. Complete modules in numerical order (1→2→3→...→16)
2. Exception: Only if human expert requests specific module
3. Rationale: Later modules reference earlier concepts

### Rule: No Parallel Tasks
**Why:**
- Ensures focus and quality
- Prevents resource conflicts
- Maintains clear accountability
- Simplifies troubleshooting

---

## Quality Gate Checkpoints

### Before Marking Task Complete

**Mandatory Verification (ALL must pass):**

1. **Content Volume:** 
   - [ ] 50,000-70,000 words achieved (±10% acceptable)

2. **Mathematical Rigor:**
   - [ ] 25-35 equations with complete derivations
   - [ ] All dimensional analyses correct
   - [ ] All variables defined

3. **Practical Examples:**
   - [ ] 20-30 worked examples
   - [ ] All use realistic, industry-standard values
   - [ ] All calculations verified

4. **Specifications:**
   - [ ] 15-20 tables with quantitative data
   - [ ] All specifications measurable
   - [ ] Acceptance criteria defined

5. **Procedures:**
   - [ ] Step-by-step instructions provided
   - [ ] Tools/equipment listed
   - [ ] Expected outcomes stated

6. **Consistency:**
   - [ ] Style matches Modules 1-2
   - [ ] Terminology consistent
   - [ ] Cross-references accurate

7. **Completeness:**
   - [ ] All original sections expanded
   - [ ] Safety addressed (if applicable)
   - [ ] Maintenance included (if applicable)
   - [ ] Troubleshooting provided (if applicable)

**If ANY checkpoint fails:**
- Do NOT mark task complete
- Fix issue immediately
- Re-verify all checkpoints
- Only then proceed to task completion

---

## Communication Standards

### To Human Expert

**Frequency:** 
- Start of each task
- Completion of each task
- Any issues requiring decisions
- Any proposed changes to plan

**Format:** 
- Concise (2-4 sentences)
- Action-oriented
- Include key metrics
- Request feedback when needed

**Example:**
```
Module 3 expansion complete! Added ~58,000 words covering tribology, 
preload mechanics, critical speeds, backlash compensation, mounting 
techniques, and comparative analysis. All 28 equations derived, 24 
examples worked, 18 tables created. Ready for Module 4 - Control 
Electronics when you approve! 🚀
```

### To AI Workers

**Frequency:**
- Task assignments
- Mid-task guidance (if needed)
- Task completion
- Change notifications

**Format:**
- Clear instructions
- Reference standards
- Specific requirements
- Expected outcomes

### Documentation Updates

**Frequency:**
- After every completed task
- When plans change
- When issues arise
- Weekly summary (if multi-day project)

**Format:**
- Structured (use templates)
- Comprehensive (capture all details)
- Searchable (use consistent terminology)
- Linked (cross-reference related items)

---

## Error Handling & Escalation

### Level 1: Minor Issues (Handle Independently)
**Examples:**
- String replacement fails once → Retry with better context
- Equation formatting issue → Fix KaTeX syntax
- Missing cross-reference → Add reference

**Protocol:**
- Fix immediately
- Document in task notes
- Continue work

### Level 2: Moderate Issues (Attempt Solutions)
**Examples:**
- String replacement fails 3 times → Create supplementary file
- Section becoming too long → Split into subsections
- Calculation error discovered → Recalculate and update

**Protocol:**
- Attempt solution per established rules
- Document issue and solution
- Note in completion report
- Continue work

### Level 3: Major Issues (Escalate to Human Expert)
**Examples:**
- Technical content accuracy uncertain
- Scope significantly larger than expected
- Tool/platform limitations encountered
- Conflicting requirements discovered

**Protocol:**
1. Stop work on affected section
2. Document issue thoroughly:
   - What's the problem?
   - What's been tried?
   - What are the options?
   - What do you recommend?
3. Escalate to human expert immediately
4. Await guidance before proceeding
5. Document resolution and continue

---

## Performance Tracking

### Metrics to Monitor (Per Task)

**Efficiency:**
- Time from start to completion
- Tool calls required
- Re-work iterations needed

**Quality:**
- Word count achieved vs. target
- Equations/examples vs. target
- Checkpoints passed on first review

**Consistency:**
- Style adherence score (subjective)
- Cross-reference accuracy
- Terminology consistency

**Issues:**
- Number of problems encountered
- Severity of issues
- Resolution time

### Continuous Improvement

**After Every 2-3 Modules:**
1. Review metrics
2. Identify patterns (good and bad)
3. Update processes if needed
4. Document lessons learned
5. Share insights with team

**Questions to Ask:**
- What worked well?
- What could be improved?
- Are we getting faster? (efficiency)
- Are we maintaining quality? (consistency)
- What new challenges emerged?
- How can we address them?

---

## Daily Workflow Checklist

### Session Start
- [ ] Read collaboration file (full)
- [ ] Check task list status
- [ ] Review any feedback from human expert
- [ ] Confirm next task to execute
- [ ] Create task execution plan

### During Work
- [ ] Follow BEFORE, DURING, AFTER protocols
- [ ] Apply all 10 learned roles
- [ ] Monitor quality in real-time
- [ ] Document any issues
- [ ] Take breaks between major sections (if long session)

### Session End
- [ ] Complete current section (don't leave half-done)
- [ ] Update task list if task completed
- [ ] Update collaboration file if task completed
- [ ] Provide status update to human expert
- [ ] Document any in-progress work for next session

---

## Team Coordination

### If Multiple AI Workers (Future Scenario)

**Task Assignment:**
- Assign by module (one worker per module)
- Assign by section (multiple workers per module)
- Clear boundaries, no overlap

**Handoff Protocol:**
- Provide context document
- Share relevant examples from completed work
- Specify integration points
- Define quality expectations

**Integration:**
- Project Lead reviews all work
- Ensures consistency across workers
- Merges content
- Resolves conflicts

**Quality Assurance:**
- Peer review between workers
- Project Lead final review
- Human expert approval

---

## Special Situations

### Situation 1: Human Expert Requests Out-of-Sequence Module
**Response:**
1. Acknowledge request
2. Check for dependencies on earlier modules
3. If dependencies exist, note in collaboration file
4. Proceed with requested module
5. Return to sequential order after

### Situation 2: Technical Complexity Exceeds Expectations
**Response:**
1. Document complexity
2. Propose solutions:
   - Break into smaller subsections
   - Create supplementary deep-dive file
   - Simplify while maintaining rigor
3. Request human expert guidance
4. Implement approved approach

### Situation 3: Discovered Error in Previous Module
**Response:**
1. Document error clearly
2. Determine severity:
   - Critical → Fix immediately, notify human expert
   - Major → Note in issue log, fix soon
   - Minor → Add to refinement list
3. Update affected module
4. Check if error pattern exists in other modules
5. Prevent recurrence in future work

---

## Project Completion Criteria

### When All 16 Modules Complete

**Final Deliverables:**
1. All module files expanded (16 total)
2. All supplementary files documented
3. Collaboration file fully updated
4. Task list showing all "completed"
5. Final project report

**Final Report Must Include:**
- Total word count across all modules
- Total equations derived
- Total worked examples
- Total tables/specifications
- Lessons learned summary
- Recommendations for course maintenance
- Index of key concepts across modules

**Celebration Message:**
```
🎉 PROJECT COMPLETE! 🎉

CNC Engineering Course - Full Expansion
16 modules transformed from outlines to comprehensive PhD-level content

Total Achievement:
- ~960,000+ words of technical content
- 400+ equations derived from first principles
- 300+ worked examples with realistic values
- 250+ specification and comparison tables
- Complete design, verification, and maintenance guidance

This course now represents a world-class educational resource for 
precision machine design and manufacturing engineering.

Thank you for your guidance and collaboration! 🚀
```

---

## Summary: Core Project Lead Responsibilities

### PRIMARY DUTIES (Always):
1. ✅ Reference collaboration file BEFORE every task
2. ✅ Create execution plan for each task
3. ✅ Monitor quality during execution
4. ✅ Update task list AFTER every task
5. ✅ Update collaboration file AFTER every task
6. ✅ Provide completion report to human expert
7. ✅ Solicit feedback from team and expert
8. ✅ Document all changes to plans
9. ✅ Maintain consistency across all work
10. ✅ Track progress and improve processes

### NEVER:
- ❌ Start task without reading collaboration file
- ❌ Skip quality checkpoints
- ❌ Leave task list outdated
- ❌ Fail to document changes
- ❌ Proceed without feedback when requested
- ❌ Mark task complete if checkpoints fail
- ❌ Work on multiple tasks simultaneously
- ❌ Ignore established standards
- ❌ Escalate without attempting solutions
- ❌ Deliver incomplete work

---

**Document Status:** Active  
**Role:** AI Project Lead  
**Reports To:** Human Expert (hendrixx)  
**Manages:** AI Content Development Team  
**Last Updated:** November 4, 2025  

---

*These rules ensure systematic, high-quality execution of the CNC Engineering Course expansion project through clear workflow protocols, quality gates, and comprehensive documentation.*
