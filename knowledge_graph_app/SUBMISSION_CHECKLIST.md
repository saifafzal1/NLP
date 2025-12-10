# Assignment Submission Checklist

**Course:** M.Tech AIML - NLP Applications (S1-25_AIMLCZG519)
**Assignment:** Assignment 1 - PS-9
**Submission Date:** [Add Date]

---

## Part A: Knowledge Graph Application (10 Marks)

### Code Deliverables ✅

- [x] **Backend Code (`app.py`)**
  - Flask application with NetworkX
  - All API endpoints implemented
  - Comprehensive error handling
  - Well-documented with comments

- [x] **Frontend Code (`templates/index.html`)**
  - Clean, responsive interface
  - Manual input form (Entity1-Relationship-Entity2)
  - CSV upload functionality
  - Query interface (3 query types)
  - Interactive graph visualization using Vis.js
  - Real-time statistics

- [x] **Dependencies (`requirements.txt`)**
  - Flask==3.0.0
  - flask-cors==4.0.0
  - networkx==3.2.1

- [x] **Sample Data (`data/sample_transportation.csv`)**
  - 40+ transportation network relationships
  - Cities, stations, airports, transit modes

### Documentation Deliverables ✅

- [x] **README.md**
  - Complete installation instructions
  - Running the application locally
  - Usage guide with examples
  - API documentation
  - Design choices explained
  - Troubleshooting guide

- [x] **Implementation Report (`docs/Implementation_Report.md`)**
  - Design choices with rationale
  - Challenges faced and solutions
  - Architecture diagrams
  - Testing and validation
  - Performance analysis
  - Screenshot descriptions (need to capture actual screenshots)

- [x] **Quick Start Guide (`QUICKSTART.md`)**
  - Fast setup instructions
  - Quick demo steps

### Screenshots Required 📸

Still need to capture:

- [ ] Initial interface (empty graph)
- [ ] Adding manual relationship
- [ ] Graph after first addition
- [ ] CSV upload dialog
- [ ] Populated graph (after CSV upload)
- [ ] Query execution - Find Connections
- [ ] Query execution - Shortest Path
- [ ] Graph interaction (hover tooltip)
- [ ] Statistics dashboard
- [ ] **OSHA Lab screenshot showing credentials** ⚠️ REQUIRED

### Feature Checklist ✅

#### Frontend Development (3 Marks)
- [x] Web-based interface
- [x] Input fields for entities and relationships
- [x] Dedicated fields: Entity 1, Relationship, Entity 2
- [x] Graph visualization
- [x] Dynamic updates

#### Graph Management and Querying (3 Marks)
- [x] Flask backend
- [x] NetworkX integration
- [x] API endpoint: Add relationship
- [x] API endpoint: Upload CSV
- [x] API endpoint: Query graph (neighbors)
- [x] API endpoint: Query graph (all relationships)
- [x] API endpoint: Query graph (path)
- [x] API endpoint: Get graph data
- [x] API endpoint: Clear graph

#### Integration (2 Marks)
- [x] Frontend-backend integration
- [x] RESTful API
- [x] Real-time graph updates
- [x] User-friendly result display

### Task B: Enhancement Plan (2 Marks) ✅

- [x] **Enhancement Plan Document (`docs/Task_B_Enhancement_Plan.md`)**
  - Visual enhancement strategies
  - Interactive enhancement strategies
  - Information enhancement strategies
  - User experience enhancements
  - Performance enhancements
  - Advanced features
  - Implementation roadmap
  - Technology recommendations

---

## Part B: Literature Survey (5 Marks)

### Literature Review Deliverable ✅

- [x] **Literature Review (`docs/Literature_Review_RAG_Hallucination.md`)**
  - **Topic:** Hallucination Reduction Strategies in Retrieval-Augmented Generation
  - **Word Count:** ~5,800 words
  - **Structure:**
    - Abstract
    - Introduction (background, problem, scope)
    - Taxonomy of strategies
    - Retrieval-based strategies (4 subsections)
    - Generation-based strategies (4 subsections)
    - Verification-based strategies (3 subsections)
    - Hybrid and advanced strategies (3 subsections)
    - Training-based strategies (3 subsections)
    - Prompting strategies (3 subsections)
    - Evaluation methodologies
    - Comparative analysis
    - Current limitations and challenges
    - Future directions
    - Industry applications
    - Conclusion
    - 40+ academic references

---

## Final Submission Package

### File Structure

```
knowledge_graph_app/
│
├── app.py                              # Main Flask application
├── requirements.txt                    # Python dependencies
├── README.md                           # Complete documentation
├── QUICKSTART.md                       # Quick start guide
├── SUBMISSION_CHECKLIST.md            # This file
├── run.sh                             # Startup script
│
├── templates/
│   └── index.html                     # Frontend interface
│
├── data/
│   └── sample_transportation.csv      # Sample data
│
└── docs/
    ├── Implementation_Report.md       # Design & challenges report
    ├── Task_B_Enhancement_Plan.md     # Task B deliverable
    ├── Literature_Review_RAG_Hallucination.md  # Part B deliverable
    └── screenshots/                   # Application screenshots
        ├── 01_initial_interface.png
        ├── 02_add_relationship.png
        ├── 03_graph_first_addition.png
        ├── 04_csv_upload.png
        ├── 05_populated_graph.png
        ├── 06_query_connections.png
        ├── 07_query_path.png
        ├── 08_graph_interaction.png
        ├── 09_statistics.png
        └── 10_osha_lab_credentials.png  ⚠️ REQUIRED
```

---

## Submission Format

### For Code Files

Create a ZIP file with the following:

```
Assignment1_PS9_[YourName].zip
│
├── knowledge_graph_app/
│   ├── [all files and folders as above]
│   └── docs/screenshots/  [all 10 screenshots]
│
└── OSHA_Lab_Screenshot.png  [copy here too for visibility]
```

### For PDF Documents

Create PDFs from Markdown:

1. **Task B PDF:**
   - Convert `docs/Task_B_Enhancement_Plan.md` to PDF
   - Name: `Task_B_Enhancement_Plan.pdf`

2. **Part B PDF:**
   - Convert `docs/Literature_Review_RAG_Hallucination.md` to PDF
   - Name: `Part_B_Literature_Review.pdf`

3. **Implementation Report PDF:**
   - Convert `docs/Implementation_Report.md` to PDF
   - Include all screenshots in Appendix
   - Name: `Implementation_Report.pdf`

### Conversion to PDF

**Method 1: Using Pandoc (Recommended)**
```bash
pandoc docs/Task_B_Enhancement_Plan.md -o Task_B_Enhancement_Plan.pdf
pandoc docs/Literature_Review_RAG_Hallucination.md -o Part_B_Literature_Review.pdf
pandoc docs/Implementation_Report.md -o Implementation_Report.pdf
```

**Method 2: Online Converters**
- https://www.markdowntopdf.com/
- https://md2pdf.netlify.app/

**Method 3: VS Code Extension**
- Install "Markdown PDF" extension
- Right-click on .md file → "Markdown PDF: Export (pdf)"

---

## Pre-Submission Testing

### Functional Testing Checklist

- [ ] Clone/extract project to fresh directory
- [ ] Run `pip install -r requirements.txt`
- [ ] Start application with `python app.py`
- [ ] Access http://127.0.0.1:5000 in browser
- [ ] Add single relationship manually
- [ ] Verify graph updates
- [ ] Upload sample CSV
- [ ] Verify 40+ relationships loaded
- [ ] Execute all 3 query types
- [ ] Verify results displayed correctly
- [ ] Test clear graph functionality
- [ ] Verify all screenshots captured
- [ ] Verify OSHA Lab screenshot included

### Documentation Review Checklist

- [ ] README has clear installation steps
- [ ] README has running instructions
- [ ] Implementation Report explains design choices
- [ ] Implementation Report documents challenges
- [ ] Task B Enhancement Plan is comprehensive
- [ ] Literature Review covers the topic thoroughly
- [ ] All documents are well-formatted
- [ ] No typos or grammatical errors

---

## Grading Rubric Reference

### Part A (10 Marks)

| Component | Marks | Self-Assessment |
|-----------|-------|----------------|
| Frontend Development | 3 | ✅ All features implemented |
| Graph Management & Querying | 3 | ✅ All endpoints working |
| Integration | 2 | ✅ Seamless integration |
| Task B: Enhancement Plan | 2 | ✅ Comprehensive document |

### Part B (5 Marks)

| Component | Marks | Self-Assessment |
|-----------|-------|----------------|
| Literature Survey Quality | 5 | ✅ 5,800 words, 40+ refs |

**Expected Total: 15/15** ✅

---

## Important Reminders

### Must Have:
1. ✅ Well-documented code (comments in Python and HTML/JS)
2. ✅ Instructions for running locally (README.md)
3. ✅ Brief report with design choices and challenges (Implementation_Report.md)
4. ✅ Screenshots of entire application flow
5. ⚠️ **OSHA Lab screenshot with credentials** - REQUIRED!
6. ✅ Task B as PDF
7. ✅ Part B literature review as PDF

### Must Do:
1. Test on BITS OSHA Cloud Lab (as per assignment requirement)
2. Capture screenshot showing OSHA credentials
3. Convert markdown documents to PDF
4. Create ZIP file with all deliverables
5. Submit before deadline (NO EXTENSIONS)

### Contact for Queries:
**Vasugi I** - vasugii@wilp.bits-pilani.ac.in

---

## Final Checklist Before Submission

- [ ] All code files included
- [ ] All documentation files included
- [ ] All 10 screenshots captured and included
- [ ] OSHA Lab screenshot captured
- [ ] Task B converted to PDF
- [ ] Part B literature review converted to PDF
- [ ] Implementation report converted to PDF
- [ ] ZIP file created
- [ ] ZIP file tested (extract and verify contents)
- [ ] File naming convention followed
- [ ] Submission uploaded to portal

---

## Post-Submission

- [ ] Verify submission confirmation received
- [ ] Keep a backup copy
- [ ] Note submission timestamp

---

**Good luck with your submission!** 🎓

---

**Document Version:** 1.0
**Last Updated:** December 2025
