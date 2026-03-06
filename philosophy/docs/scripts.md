# Scripts Documentation

This directory contains the core processing modules for the philosophy mapping system.

## Overview

Each script can be run independently or as part of the main pipeline. They're designed to be modular and testable.

## Scripts

### compute_vectors.py

**Purpose**: Calculate similarity metrics between philosophical rules based on their axis scores.

**Key Functions**:
- `rule_to_vector()` - Converts rule axes to 6D vector
- `compute_euclidean_distance()` - Calculates distance between vectors
- `compute_similarity_matrix()` - Creates distance matrix for all rules
- `find_similar_rules()` - Identifies rules below similarity threshold
- `find_opposing_rules()` - Identifies rules above opposing threshold

**Usage**:
```bash
python scripts/compute_vectors.py
```

**Output**: Similarity matrix and lists of most similar/opposing rule pairs.

### build_graph.py

**Purpose**: Construct NetworkX graph from rules data and relationships.

**Key Functions**:
- `load_rules()` - Loads and validates rules from JSON
- `build_complete_graph()` - Main graph construction function
- Adds explicit relationships from rules.json
- Adds similarity-based relationships automatically

**Customization**:
```python
similarity_threshold = 1.0   # Lower = more similarity edges
opposing_threshold = 2.0     # Higher = more opposing edges
```

**Usage**:
```bash
python scripts/build_graph.py
```

**Output**: Graph statistics, edge type distribution, influence rankings.

### render_graph.py

**Purpose**: Generate visual graph artifacts (PNG, SVG, HTML).

**Key Functions**:
- `render_static_graph()` - Creates PNG/SVG using matplotlib
- `render_interactive_graph()` - Creates HTML using pyvis
- `get_edge_color()` - Maps relationship types to colors
- `get_node_color()` - Colors nodes based on axis scores

**Visual Mapping**:
- Green edges = support
- Red edges = oppose
- Gray edges = similar
- Blue edges = similarity (auto-generated)
- Purple edges = opposing (auto-generated)
- Orange dashed edges = contextual

**Node sizing**: Based on `influenceWeight` (larger = more influential)

**Usage**:
```bash
python scripts/render_graph.py
```

**Outputs**: 
- `output/philosophy_map.png` - High-resolution static graph
- `output/philosophy_map.svg` - Vector format graph
- `output/philosophy_map.html` - Interactive graph

### analysis.py

**Purpose**: Perform network analysis to identify patterns and key philosophies.

**Key Functions**:
- `compute_centrality()` - Calculates betweenness, degree, closeness
- `find_bridge_nodes()` - Identifies philosophies connecting clusters
- `find_clusters()` - Detects philosophical schools using modularity
- `find_outliers()` - Finds isolated philosophies
- `analyze_philosophical_axes()` - Statistics on axis distributions
- `generate_report()` - Creates comprehensive analysis report

**Metrics Calculated**:
- **Centrality**: Which philosophies are most influential/central
- **Bridges**: Which philosophies connect different philosophical schools
- **Clusters**: Groups of similar philosophies
- **Outliers**: Philosophies that don't fit any cluster
- **Axis Statistics**: Distribution of scores across each conceptual axis

**Usage**:
```bash
python scripts/analysis.py
```

**Output**: `output/analysis_report.txt` with detailed network analysis.

## Customization

### Adding New Analysis Metrics

Each script can be extended with new functions:

```python
def custom_metric(G: nx.Graph) -> dict:
    # Your analysis logic here
    return results

# Add to generate_report()
```

### Modifying Visualizations

**Colors**: Edit `get_edge_color()` and `get_node_color()` functions

**Layout**: Adjust spring layout parameters in `render_static_graph()`

**Filters**: Add edge filtering or node filtering options

## Data Flow

1. **rules.json** → compute_vectors.py → similarity matrix
2. **rules.json** + similarity → build_graph.py → NetworkX graph
3. **NetworkX graph** → render_graph.py → visual artifacts
4. **NetworkX graph** → analysis.py → analytical report

## Testing

Each script can be tested independently:

```bash
# Test vector calculations
python scripts/compute_vectors.py

# Test graph construction
python scripts/build_graph.py

# Test visualization
python scripts/render_graph.py

# Test analysis
python scripts/analysis.py
```

## Dependencies

All scripts share common dependencies:
- **NetworkX** - Graph data structure and algorithms
- **NumPy** - Vector mathematics
- **Matplotlib** - Static visualization
- **PyVis** - Interactive HTML visualization (optional)

## Error Handling

Scripts include basic error handling for:
- Missing or invalid JSON files
- Missing required fields in rule objects
- NetworkX graph construction errors
- File I/O errors

Check script output for specific error messages and troubleshooting hints.
