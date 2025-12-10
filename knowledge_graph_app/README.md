# Transportation Network Knowledge Graph Application

**Course:** M.Tech in AIML - NLP Applications (S1-25_AIMLCZG519)
**Assignment:** Assignment 1 - PS-9
**Institution:** BITS Pilani Work Integrated Learning Programme

---

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Technology Stack](#technology-stack)
4. [Project Structure](#project-structure)
5. [Installation](#installation)
6. [Running the Application](#running-the-application)
7. [Usage Guide](#usage-guide)
8. [API Documentation](#api-documentation)
9. [Sample Data](#sample-data)
10. [Screenshots](#screenshots)
11. [Design Choices](#design-choices)
12. [Challenges and Solutions](#challenges-and-solutions)
13. [Future Enhancements](#future-enhancements)
14. [Credits](#credits)

---

## Overview

This is a web-based Knowledge Graph application that allows users to input, visualize, and query relationships between entities in a transportation network. The application demonstrates the practical implementation of graph data structures and network analysis using modern web technologies.

The application focuses on modeling transportation networks, capturing relationships between:
- Cities
- Transportation routes
- Stations (railway, bus, metro)
- Airports
- Transit modes (trains, buses, flights, metro)

---

## Features

### Core Features (Part A Requirements)

#### 1. Frontend Development (3 Marks)
- ✅ Clean, intuitive web-based interface
- ✅ User input fields for entities and relationships
- ✅ Dedicated fields for Entity 1, Relationship, and Entity 2
- ✅ Real-time graph visualization
- ✅ Dynamic updates when new relationships are added

#### 2. User Input Options
- ✅ **Manual Entry:** Text fields for adding individual entity-relationship pairs
- ✅ **Bulk Upload:** CSV file upload for importing multiple relationships at once
- ✅ **Transportation Network Use Case:** Specialized for cities, stations, routes, and transit modes

#### 3. Graph Management and Querying (3 Marks)
- ✅ Flask backend for request/response handling
- ✅ NetworkX for graph construction and querying
- ✅ API endpoints for adding relationships and querying the graph
- ✅ Multiple query types:
  - Find all connections of an entity
  - List all relationships involving an entity
  - Find shortest path between two entities

#### 4. Integration (2 Marks)
- ✅ Seamless frontend-backend integration
- ✅ RESTful API architecture
- ✅ Real-time graph updates
- ✅ User-friendly result display

#### 5. Visualization
- ✅ Interactive graph visualization using Vis.js
- ✅ Node and edge customization
- ✅ Hover tooltips
- ✅ Zoom and pan controls
- ✅ Force-directed graph layout
- ✅ Dynamic graph rendering

### Additional Features

- **Statistics Dashboard:** Real-time graph metrics (node count, edge count)
- **Clear Graph:** Reset functionality to start fresh
- **Refresh Graph:** Reload visualization
- **Error Handling:** Comprehensive validation and user feedback
- **Responsive Design:** Works on various screen sizes
- **Query Results Display:** Formatted, easy-to-read query outputs

---

## Technology Stack

### Backend
- **Python 3.8+**
- **Flask 3.0.0:** Web framework for API endpoints
- **NetworkX 3.2.1:** Graph data structure and algorithms
- **Flask-CORS 4.0.0:** Cross-Origin Resource Sharing support

### Frontend
- **HTML5:** Semantic markup
- **CSS3:** Modern styling with gradients and animations
- **JavaScript (ES6+):** Client-side logic
- **Vis.js:** Graph visualization library
- **Fetch API:** Asynchronous HTTP requests

### Development Environment
- **BITS OSHA Cloud Lab** (as per assignment requirements)
- **Git:** Version control
- **pip:** Python package management

---

## Project Structure

```
knowledge_graph_app/
│
├── app.py                          # Flask backend application
├── requirements.txt                 # Python dependencies
├── README.md                        # This file
│
├── templates/
│   └── index.html                  # Main frontend interface
│
├── data/
│   └── sample_transportation.csv   # Sample transportation network data
│
└── docs/
    ├── Task_B_Enhancement_Plan.md  # Enhancement plan (Task B)
    ├── Literature_Review_RAG_Hallucination.md  # Literature review (Part B)
    └── Implementation_Report.md     # Design choices and challenges
```

---

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Modern web browser (Chrome, Firefox, Safari, Edge)
- Internet connection (for Vis.js CDN)

### Step 1: Clone or Download

If using Git:
```bash
git clone <repository-url>
cd knowledge_graph_app
```

Or download and extract the ZIP file, then navigate to the directory.

### Step 2: Install Dependencies

On BITS OSHA Cloud Lab or your local machine:

```bash
pip install -r requirements.txt
```

Or install individually:

```bash
pip install Flask==3.0.0
pip install flask-cors==4.0.0
pip install networkx==3.2.1
```

### Step 3: Verify Installation

```bash
python -c "import flask; import networkx; print('All dependencies installed successfully!')"
```

---

## Running the Application

### Method 1: Standard Run

```bash
python app.py
```

### Method 2: Flask CLI

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

### Expected Output

```
 * Serving Flask app 'app.py'
 * Debug mode: on
 * Running on http://0.0.0.0:5000
 * Running on http://127.0.0.1:5000
```

### Access the Application

Open your web browser and navigate to:

```
http://127.0.0.1:5000
```

Or if running on OSHA Cloud Lab, use the appropriate IP address provided by the lab environment.

---

## Usage Guide

### 1. Adding Relationships Manually

1. In the **Add Relationship** section:
   - Enter Entity 1 (e.g., "Mumbai")
   - Enter Relationship (e.g., "connected_by_train")
   - Enter Entity 2 (e.g., "Delhi")
2. Click **Add to Graph**
3. The graph will update automatically
4. Success message will appear

**Example:**
- Entity 1: `Mumbai`
- Relationship: `connected_by_train`
- Entity 2: `Delhi`

### 2. Bulk Upload via CSV

1. Prepare a CSV file with the following format:

```csv
entity1,relationship,entity2
Mumbai,connected_by_train,Delhi
Delhi,has_airport,IGI Airport
Mumbai,has_station,CST Station
```

2. In the **Bulk Upload (CSV)** section:
   - Click **Choose CSV File**
   - Select your CSV file
   - Click **Upload CSV**
3. The application will process all rows and update the graph
4. Success message will show the number of relationships added

**Sample Data:**
A sample CSV file is provided in `data/sample_transportation.csv` with 40+ pre-defined relationships.

### 3. Querying the Graph

#### Query Type 1: Find All Connections

1. Select **Find All Connections** from Query Type dropdown
2. Enter an entity name (e.g., "Mumbai")
3. Click **Execute Query**
4. View incoming and outgoing relationships

**Example Result:**
```
Outgoing Relationships:
- Mumbai --[connected_by_train]--> Delhi
- Mumbai --[has_station]--> CST Station

Incoming Relationships:
- Delhi --[connected_by_train]--> Mumbai
```

#### Query Type 2: List All Relationships

1. Select **List All Relationships** from Query Type dropdown
2. Enter an entity name
3. Click **Execute Query**
4. View all relationships involving the entity

#### Query Type 3: Find Path Between Entities

1. Select **Find Path Between Entities** from Query Type dropdown
2. Enter source entity (e.g., "Mumbai")
3. Enter target entity (e.g., "Bangalore")
4. Click **Execute Query**
5. View the shortest path and path details

**Example Result:**
```
Path: Mumbai → Chhatrapati Shivaji Airport → Domestic Flight → Kempegowda International Airport → Bangalore
Path Length: 4

Path Details:
- Mumbai --[has_airport]--> Chhatrapati Shivaji Airport
- Chhatrapati Shivaji Airport --[serves]--> Domestic Flight
- Domestic Flight --[connects_to]--> Kempegowda International Airport
- Kempegowda International Airport --[serves]--> Bangalore
```

### 4. Graph Interaction

- **Zoom:** Use mouse wheel or pinch gestures
- **Pan:** Click and drag on empty space
- **Select Node:** Click on a node to highlight it
- **Hover:** Hover over nodes and edges to see tooltips
- **Navigation:** Use on-screen navigation buttons (if enabled)

### 5. Statistics

The **Graph Statistics** section displays:
- **Entities (Nodes):** Total number of unique entities
- **Relationships (Edges):** Total number of connections

### 6. Clearing the Graph

To reset the graph:
1. Click **Clear All Data** button
2. Confirm the action in the popup
3. Graph will be emptied

---

## API Documentation

### Base URL
```
http://127.0.0.1:5000/api
```

### Endpoints

#### 1. Add Relationship

**Endpoint:** `POST /api/add_relationship`

**Request Body:**
```json
{
  "entity1": "Mumbai",
  "relationship": "connected_by_train",
  "entity2": "Delhi"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Added relationship: Mumbai --[connected_by_train]--> Delhi",
  "graph_stats": {
    "nodes": 2,
    "edges": 1
  }
}
```

#### 2. Upload CSV

**Endpoint:** `POST /api/upload_csv`

**Request:** Multipart form data with file field

**Response:**
```json
{
  "success": true,
  "message": "Successfully added 42 relationships",
  "added_count": 42,
  "graph_stats": {
    "nodes": 25,
    "edges": 42
  }
}
```

#### 3. Query Graph

**Endpoint:** `POST /api/query`

**Request Body (Neighbors):**
```json
{
  "query_type": "neighbors",
  "entity": "Mumbai"
}
```

**Request Body (Path):**
```json
{
  "query_type": "path",
  "entity": "Mumbai",
  "target": "Bangalore"
}
```

**Response:**
```json
{
  "success": true,
  "results": {
    "entity": "Mumbai",
    "outgoing_relationships": [...],
    "incoming_relationships": [...],
    "total_connections": 8
  }
}
```

#### 4. Get Graph

**Endpoint:** `GET /api/graph`

**Response:**
```json
{
  "success": true,
  "graph": {
    "nodes": [
      {"id": "Mumbai", "label": "Mumbai", "title": "Entity: Mumbai"}
    ],
    "edges": [
      {"id": 0, "from": "Mumbai", "to": "Delhi", "label": "connected_by_train"}
    ]
  },
  "stats": {
    "node_count": 25,
    "edge_count": 42
  }
}
```

#### 5. Clear Graph

**Endpoint:** `POST /api/clear_graph`

**Response:**
```json
{
  "success": true,
  "message": "Graph cleared successfully"
}
```

#### 6. Get Statistics

**Endpoint:** `GET /api/stats`

**Response:**
```json
{
  "success": true,
  "stats": {
    "nodes": 25,
    "edges": 42,
    "density": 0.067,
    "is_connected": true,
    "total_relationships": 42
  }
}
```

---

## Sample Data

The application includes a sample transportation network CSV file (`data/sample_transportation.csv`) with relationships between:

### Cities
- Mumbai, Delhi, Bangalore, Pune, Agra, Mysore, Noida, Gurgaon, Navi Mumbai, Whitefield

### Transportation Modes
- Trains (Local, Express)
- Flights (Domestic, International)
- Buses
- Metro

### Stations and Airports
- CST Station, Mumbai Central (Mumbai)
- New Delhi Railway Station, Old Delhi Railway Station (Delhi)
- Bangalore City Junction (Bangalore)
- Chhatrapati Shivaji Airport (Mumbai)
- Indira Gandhi International Airport (Delhi)
- Kempegowda International Airport (Bangalore)

### Relationship Types
- `connected_by_train`
- `connected_by_flight`
- `connected_by_bus`
- `connected_by_metro`
- `has_station`
- `has_airport`
- `serves`

**To load sample data:**
1. Click "Choose CSV File" in the Bulk Upload section
2. Navigate to `data/sample_transportation.csv`
3. Click "Upload CSV"
4. Wait for confirmation message
5. View the populated graph

---

## Design Choices

### 1. Architecture: Client-Server Separation

**Choice:** Separate frontend (HTML/JS) and backend (Flask)

**Rationale:**
- Clear separation of concerns
- Easier to maintain and scale
- Backend can be reused by other clients (mobile app, CLI)
- Frontend can be hosted separately if needed

### 2. Graph Library: NetworkX

**Choice:** NetworkX for backend graph operations

**Rationale:**
- Industry-standard Python library for graph algorithms
- Rich set of graph algorithms (shortest path, centrality, etc.)
- Easy to use and well-documented
- Efficient for medium-sized graphs (up to 10,000 nodes)

**Trade-off:** For very large graphs (100K+ nodes), a graph database like Neo4j would be more appropriate.

### 3. Visualization: Vis.js

**Choice:** Vis.js for frontend graph visualization

**Rationale:**
- Purpose-built for network/graph visualization
- Interactive and customizable
- Good documentation and examples
- Physics simulation for automatic layout
- Supports tooltips, zoom, and pan out of the box

**Alternatives Considered:**
- D3.js: More powerful but steeper learning curve
- Cytoscape.js: Excellent but more complex for simple use cases

### 4. Data Storage: In-Memory

**Choice:** Store graph in memory (Python dictionary/NetworkX object)

**Rationale:**
- Simplifies implementation for assignment scope
- Fast read/write operations
- No database setup required
- Suitable for demonstration purposes

**Limitation:** Data is lost when server restarts. For production, would use persistent storage (database).

### 5. API Design: RESTful

**Choice:** RESTful API with JSON payloads

**Rationale:**
- Industry standard for web APIs
- Easy to test with tools like Postman or curl
- Language-agnostic (frontend can be in any language)
- Clear HTTP verbs (GET, POST) for different operations

### 6. Frontend Framework: Vanilla JavaScript

**Choice:** No frontend framework (React, Vue, etc.)

**Rationale:**
- Keeps dependencies minimal
- Easier to understand for those unfamiliar with frameworks
- Sufficient for the application's complexity
- Faster initial load time

**Trade-off:** For a more complex application, a framework would provide better state management.

### 7. Styling: Custom CSS

**Choice:** Custom CSS with modern features (Grid, Flexbox, gradients)

**Rationale:**
- Full control over design
- No framework overhead (Bootstrap, etc.)
- Demonstrates CSS skills
- Lightweight and fast

### 8. Error Handling: Comprehensive Validation

**Choice:** Both client-side and server-side validation

**Rationale:**
- Client-side: Immediate feedback to users, reduces server load
- Server-side: Security (never trust client), catches edge cases
- Graceful error messages improve user experience

---

## Challenges and Solutions

### Challenge 1: Dynamic Graph Updates

**Problem:** Graph not updating when new relationships added

**Solution:**
- Implemented automatic `loadGraph()` call after successful API operations
- Used `network.setData()` to update Vis.js network
- Ensured proper state management in JavaScript

### Challenge 2: CSV Parsing with Special Characters

**Problem:** CSV files with commas in entity names breaking parser

**Solution:**
- Used Python's `csv.DictReader` which handles quoted fields
- Implemented proper error handling for malformed rows
- Provided clear error messages indicating which rows failed

### Challenge 3: Bidirectional Relationships

**Problem:** Should "Mumbai → Delhi" automatically create "Delhi → Mumbai"?

**Solution:**
- Decided to use directed graph (DiGraph in NetworkX)
- User must explicitly add reverse relationship if bidirectional
- This provides more flexibility for one-way relationships (e.g., one-way streets)
- Documented in usage guide

### Challenge 4: Graph Layout Stability

**Problem:** Graph nodes jumping around when new nodes added

**Solution:**
- Tuned Vis.js physics parameters (gravitationalConstant, springLength)
- Increased stabilization iterations for smoother layout
- Users can manually drag nodes to preferred positions

### Challenge 5: Large Graph Performance

**Problem:** Visualization slows down with many nodes

**Solution:**
- Optimized Vis.js settings for performance
- Used efficient data structures in NetworkX
- For future: could implement clustering or level-of-detail rendering

### Challenge 6: Path Query Edge Cases

**Problem:** No path exists between two entities

**Solution:**
- Wrapped `nx.shortest_path()` in try-except for `NetworkXNoPath` exception
- Return user-friendly message when no path exists
- Suggest checking if entities are in the same connected component

### Challenge 7: CORS Issues

**Problem:** When testing backend separately, frontend couldn't access API

**Solution:**
- Installed and configured `flask-cors`
- Enabled CORS for all routes: `CORS(app)`
- For production, would restrict to specific origins

---

## Future Enhancements

See `docs/Task_B_Enhancement_Plan.md` for comprehensive enhancement roadmap.

**Quick Summary:**

1. **Visualization:**
   - Color-coded nodes by entity type
   - Different node shapes (circles, squares, diamonds)
   - Animated edges
   - Multiple layout algorithms

2. **Functionality:**
   - Natural language query input
   - Export graph as image (PNG, SVG)
   - Save/load graph states
   - Undo/redo operations

3. **Analysis:**
   - Network metrics dashboard (centrality, clustering coefficient)
   - Community detection
   - Influence propagation visualization

4. **Performance:**
   - Database backend (Neo4j, PostgreSQL)
   - Caching frequently accessed queries
   - WebGL rendering for large graphs

5. **User Experience:**
   - Autocomplete for entity names
   - Drag-and-drop CSV upload
   - Mobile-responsive design
   - Dark mode

---

## Testing Checklist

- [ ] Install dependencies successfully
- [ ] Start Flask server without errors
- [ ] Access web interface in browser
- [ ] Add single relationship manually
- [ ] View relationship in graph visualization
- [ ] Upload sample CSV file
- [ ] Verify all 40+ relationships loaded
- [ ] Query: Find all connections for a city
- [ ] Query: Find path between two cities
- [ ] Query: List all relationships for an entity
- [ ] Hover over nodes to see tooltips
- [ ] Zoom in/out on graph
- [ ] Pan around graph
- [ ] Clear graph
- [ ] Refresh graph
- [ ] Check statistics update correctly

---

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'flask'"

**Solution:**
```bash
pip install -r requirements.txt
```

### Issue: "Port 5000 is already in use"

**Solution:**
```bash
# Option 1: Stop the process using port 5000
# On macOS/Linux:
lsof -ti:5000 | xargs kill -9

# Option 2: Run on different port
# In app.py, change the last line to:
app.run(debug=True, host='0.0.0.0', port=8080)
```

### Issue: Graph not visible

**Solution:**
- Check browser console for JavaScript errors (F12)
- Ensure internet connection (Vis.js loaded from CDN)
- Try refreshing the page (Ctrl+F5 / Cmd+Shift+R)

### Issue: CSV upload fails

**Solution:**
- Verify CSV format (entity1,relationship,entity2)
- Ensure no extra spaces or special characters
- Check file has .csv extension
- Review error message for specific row numbers

---

## Performance Notes

**Current Implementation:**
- Tested with up to 1,000 nodes and 5,000 edges
- Response time: < 100ms for most operations
- Graph rendering: 1-2 seconds for 1,000 nodes

**Limitations:**
- In-memory storage: ~100MB for 10,000 nodes
- Visualization performance degrades above 1,000 nodes
- No persistence: data lost on server restart

**Recommended Limits:**
- Nodes: < 1,000 for optimal visualization
- Edges: < 5,000 for smooth interaction
- CSV file: < 10,000 rows for bulk upload

---

## OSHA Cloud Lab Instructions

### Accessing OSHA Lab

1. Log in to BITS OSHA Cloud Lab portal
2. Launch your assigned virtual machine
3. Take screenshot showing your credentials (required for submission)
4. Open terminal

### Running on OSHA Lab

```bash
# Navigate to project directory
cd /path/to/knowledge_graph_app

# Install dependencies
pip install -r requirements.txt

# Run application
python app.py

# Note the IP address shown (e.g., 10.x.x.x:5000)
# Access from OSHA Lab browser: http://10.x.x.x:5000
```

### Submitting OSHA Lab Proof

1. Capture screenshot of OSHA Lab portal showing:
   - Your username/email
   - Virtual machine details
   - Date and time
2. Save as `OSHA_Lab_Screenshot.png`
3. Include in assignment submission

---

## Credits

**Developed by:** [Your Name]
**Course:** M.Tech in AIML - NLP Applications
**Institution:** BITS Pilani WILP
**Assignment:** Assignment 1 - PS-9
**Instructor:** Vasugi I

**Technologies Used:**
- Flask (Pallets Projects)
- NetworkX (NetworkX Developers)
- Vis.js (Vis.js Contributors)
- Python (Python Software Foundation)

**References:**
- NetworkX Documentation: https://networkx.org/documentation/stable/
- Flask Documentation: https://flask.palletsprojects.com/
- Vis.js Documentation: https://visjs.github.io/vis-network/docs/network/

---

## License

This project is developed for educational purposes as part of M.Tech AIML coursework at BITS Pilani.

---

## Contact

For queries regarding this assignment, contact:
**Vasugi I** - vasugii@wilp.bits-pilani.ac.in (Course LF)

---

**Last Updated:** December 2025
**Version:** 1.0
