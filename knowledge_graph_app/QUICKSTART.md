# Quick Start Guide

Get the Knowledge Graph Application running in 3 simple steps!

---

## Method 1: Using the Run Script (Recommended)

### On macOS/Linux:

```bash
cd knowledge_graph_app
./run.sh
```

### On Windows:

```bash
cd knowledge_graph_app
python app.py
```

Open your browser and go to: **http://127.0.0.1:5000**

---

## Method 2: Manual Setup

### Step 1: Install Dependencies

```bash
pip install Flask==3.0.0 flask-cors==4.0.0 networkx==3.2.1
```

### Step 2: Run the Application

```bash
python app.py
```

### Step 3: Open in Browser

Navigate to: **http://127.0.0.1:5000**

---

## Quick Demo

### 1. Add Your First Relationship

In the "Add Relationship" section:
- **Entity 1:** Mumbai
- **Relationship:** connected_by_train
- **Entity 2:** Delhi
- Click **Add to Graph**

Watch the graph update in real-time!

### 2. Load Sample Data

- Click **Choose CSV File**
- Select `data/sample_transportation.csv`
- Click **Upload CSV**
- See 40+ relationships populate the graph

### 3. Query the Graph

- Select **Find All Connections**
- Enter **Mumbai** as the entity
- Click **Execute Query**
- View all connections to and from Mumbai

### 4. Find a Path

- Select **Find Path Between Entities**
- **Entity:** Mumbai
- **Target Entity:** Bangalore
- Click **Execute Query**
- See the shortest path highlighted

---

## Troubleshooting

### Port 5000 Already in Use?

Edit `app.py` and change the last line to:
```python
app.run(debug=True, host='0.0.0.0', port=8080)
```

Then access at: http://127.0.0.1:8080

### Dependencies Not Installing?

Try upgrading pip first:
```bash
pip install --upgrade pip
```

Then retry installation.

---

## Next Steps

- Read the full `README.md` for detailed documentation
- Check `docs/Implementation_Report.md` for design details
- Review `docs/Task_B_Enhancement_Plan.md` for future features
- Explore `docs/Literature_Review_RAG_Hallucination.md` for Part B

---

**Need Help?** Contact: vasugii@wilp.bits-pilani.ac.in
