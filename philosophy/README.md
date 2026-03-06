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

## Documentation

- **[Full Documentation](docs/README.md)** - Comprehensive guide to using the tool

## Installation

### Docker

Build and run using Docker:

```bash
# Build the image (preserves file ownership)
docker build --build-arg USER_ID=$(id -u) --build-arg GROUP_ID=$(id -g) -t philosophy-map .

# Run the graph generation
docker run -v $(pwd)/output:/app/output philosophy-map

# Run analysis
docker run -v $(pwd)/output:/app/output philosophy-map python scripts/analysis.py
```

## Usage

### Generate Graph Visualizations

Run the main rendering script:

```bash
python scripts/render_graph.py
```

### Run Network Analysis

Generate a detailed analysis report:

```bash
python scripts/analysis.py
```

### Test Individual Components

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

## Technology

- **Python** - Core language
- **NetworkX** - Graph structure and algorithms
- **NumPy** - Vector math
- **Matplotlib** - Static graph rendering
- **PyVis** - Interactive HTML graph export (optional)

## License

This project is intended as a research and exploration tool.
