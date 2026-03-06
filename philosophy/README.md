# Philosophy Rule Mapping & Graph Generator

A local research tool that maps philosophical "rules for living" and visualizes their relationships through graph analysis.

## Overview

This system is **not a web application** and **does not require any backend infrastructure**. It is a **local graph-generation pipeline** that reads structured data files and produces **visual graph artifacts (PNG / SVG / HTML)** showing the relationships between philosophies.

The tool allows you to:
1. Define philosophical rules in JSON
2. Tag them along conceptual axes
3. Define explicit relationships between rules
4. Compute similarity relationships automatically
5. Generate visual graph artifacts

## Project Structure

```
philosophy/
├── data/
│   ├── rules.json              # Philosophical rules and axis scores
│   └── relationships.json      # Explicit relationships between rules
├── scripts/
│   ├── compute_vectors.py      # Vector math and similarity calculations
│   ├── build_graph.py          # Graph construction
│   ├── render_graph.py         # Visualization generation
│   └── analysis.py             # Network analysis and clustering
├── output/
│   ├── philosophy_map.png      # Static graph visualization
│   ├── philosophy_map.svg      # Vector graph visualization
│   ├── philosophy_map.html     # Interactive graph (optional)
│   └── analysis_report.txt    # Network analysis report
├── requirements.txt
└── README.md
```

## Installation

### Local Installation

1. Install Python dependencies:

```bash
pip install -r requirements.txt
```

### Docker

Build and run using Docker:

```bash
# Build the image
docker build -t philosophy-map .

# Run the graph generation
docker run -v $(pwd)/output:/app/output philosophy-map

# Run analysis
docker run -v $(pwd)/output:/app/output philosophy-map python scripts/analysis.py
```

For Windows PowerShell:

```powershell
# Build the image
docker build -t philosophy-map .

# Run the graph generation
docker run -v "${PWD}/output:/app/output" philosophy-map

# Run analysis
docker run -v "${PWD}/output:/app/output" philosophy-map python scripts/analysis.py
```

## Usage

### Generate Graph Visualizations

Run the main rendering script:

```bash
python scripts/render_graph.py
```

This will generate:
- `output/philosophy_map.png` - High-resolution static graph
- `output/philosophy_map.svg` - Vector format graph
- `output/philosophy_map.html` - Interactive graph (requires pyvis)

### Run Network Analysis

Generate a detailed analysis report:

```bash
python scripts/analysis.py
```

This creates `output/analysis_report.txt` with:
- Centrality metrics (betweenness, degree, closeness)
- Bridge nodes (philosophies that connect different clusters)
- Philosophical clusters
- Outlier detection
- Edge type distribution
- Axis statistics

### Test Vector Computations

Test similarity calculations:

```bash
python scripts/compute_vectors.py
```

This displays:
- Similarity matrix for all rules
- Most similar rules (by Euclidean distance)
- Most opposing rules (by Euclidean distance)

### Build Graph Structure

Test graph construction:

```bash
python scripts/build_graph.py
```

This displays:
- Graph statistics (nodes, edges)
- Edge type distribution
- Nodes with highest influence weight

## Data Format

### rules.json Schema

Each philosophical rule is defined with:

```json
{
  "id": "gandhi_nonviolence",
  "name": "Nonviolent Resistance",
  "source": "Mahatma Gandhi",
  "description": "Resist oppression through nonviolent means.",
  "axes": {
    "conflict": -1,
    "truth": 1,
    "order": -0.5,
    "will": 1,
    "risk": 0.4,
    "time": 0.8
  },
  "whenWorks": "When moral legitimacy matters.",
  "whenFails": "Against actors who ignore moral pressure.",
  "similarTo": ["mlk_nonviolence"],
  "opposes": ["trump_art_of_deal"],
  "influenceWeight": 0.9,
  "notes": "Requires patience and strategic non-cooperation."
}
```

**Axis values must be normalized between -1 and 1.**

### relationships.json Schema

Explicit relationships between rules:

```json
{
  "source": "gandhi_nonviolence",
  "target": "mlk_nonviolence",
  "type": "support"
}
```

**Valid relationship types:**
- `support` - One philosophy supports another
- `oppose` - Philosophies are in opposition
- `similar` - Philosophies are similar
- `contextual` - Context-dependent relationship

## Philosophy Vector Representation

Each rule is converted to a 6-dimensional vector:

```
vector = [conflict, truth, order, will, risk, time]
```

These vectors are used to:
- Compute similarity using Euclidean distance
- Determine philosophical distance
- Influence graph layout
- Identify clusters

**Interpretation:**
- Small distance → similar philosophies
- Large distance → opposing philosophies

## Graph Visualization

### Static Graph (PNG/SVG)

- **Force-directed layout** using NetworkX spring layout
- **Node size** → influenceWeight
- **Edge colors:**
  - Green = support
  - Red = oppose
  - Gray = similar
  - Blue = similarity (auto-generated)
  - Purple = opposing (auto-generated)
  - Orange dashed = contextual

### Interactive Graph (HTML)

- Hover over nodes to see rule details
- Drag nodes to explore layout
- Zoom and pan functionality
- No server required (runs locally)

## Customization

### Adjust Similarity Thresholds

Edit `scripts/build_graph.py`:

```python
similarity_threshold = 1.0   # Lower = more similarity edges
opposing_threshold = 2.0     # Higher = more opposing edges
```

### Modify Graph Layout

Edit `scripts/render_graph.py`:

```python
pos = nx.spring_layout(G, k=2, iterations=50, seed=42)
```

- `k` - Distance between nodes (higher = more spread)
- `iterations` - Layout iterations
- `seed` - Reproducible layout

### Change Visual Style

Edit `scripts/render_graph.py` to modify:
- Node colors
- Edge widths
- Figure size
- Font sizes

## Analysis Features

The analysis module computes:

- **Centrality metrics** - Identify influential philosophies
- **Bridge nodes** - Philosophies that connect clusters
- **Clustering** - Detect philosophical schools
- **Outliers** - Isolated philosophies
- **Edge analysis** - Relationship type distribution
- **Axis statistics** - Distribution across conceptual axes

## Workflow

1. **Edit data files:**
   - Modify `data/rules.json` to add/modify philosophical rules
   - Modify `data/relationships.json` to add/modify relationships

2. **Generate visualizations:**
   ```bash
   python scripts/render_graph.py
   ```

3. **View outputs:**
   - Open `output/philosophy_map.png` or `.svg` in image viewer
   - Open `output/philosophy_map.html` in web browser for interactive exploration

4. **Run analysis:**
   ```bash
   python scripts/analysis.py
   ```
   - Review `output/analysis_report.txt`

## Design Principles

- **Simplicity** - Clean, readable code
- **Clarity** - Well-documented modules
- **Reproducibility** - Deterministic graph layouts
- **Local execution** - No external dependencies or servers
- **Modular architecture** - Easy to extend and modify

## Technology

- **Python** - Core language
- **NetworkX** - Graph structure and algorithms
- **NumPy** - Vector math
- **Matplotlib** - Static graph rendering
- **PyVis** - Interactive HTML graph export (optional)

## License

This project is intended as a research and exploration tool.
