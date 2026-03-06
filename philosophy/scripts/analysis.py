import networkx as nx
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent))
from build_graph import build_complete_graph
from collections import Counter


def compute_centrality(G: nx.Graph) -> dict:
    betweenness = nx.betweenness_centrality(G)
    degree = nx.degree_centrality(G)
    closeness = nx.closeness_centrality(G)
    
    centrality = {}
    for node in G.nodes():
        centrality[node] = {
            'betweenness': betweenness[node],
            'degree': degree[node],
            'closeness': closeness[node]
        }
    
    return centrality


def find_bridge_nodes(G: nx.Graph, threshold: float = 0.5) -> list:
    betweenness = nx.betweenness_centrality(G)
    bridges = sorted(betweenness.items(), key=lambda x: x[1], reverse=True)
    return [(node, score) for node, score in bridges if score > threshold]


def find_clusters(G: nx.Graph):
    try:
        from networkx.algorithms.community import greedy_modularity_communities
        communities = greedy_modularity_communities(G)
        return [list(community) for community in communities]
    except ImportError:
        return None


def find_outliers(G: nx.Graph, centrality: dict, threshold: float = 0.1) -> list:
    outliers = []
    for node, metrics in centrality.items():
        if metrics['betweenness'] < threshold and metrics['degree'] < threshold:
            outliers.append(node)
    return outliers


def analyze_edge_types(G: nx.Graph) -> dict:
    edge_type_counts = Counter()
    for u, v, data in G.edges(data=True):
        edge_type = data.get('type', 'unknown')
        edge_type_counts[edge_type] += 1
    return dict(edge_type_counts)


def analyze_philosophical_axes(G: nx.Graph) -> dict:
    axis_stats = {
        'conflict': [],
        'truth': [],
        'order': [],
        'will': [],
        'risk': [],
        'time': []
    }
    
    for node_id, data in G.nodes(data=True):
        axes = data['axes']
        for axis in axis_stats.keys():
            axis_stats[axis].append(axes[axis])
    
    axis_summary = {}
    for axis, values in axis_stats.items():
        axis_summary[axis] = {
            'min': min(values),
            'max': max(values),
            'mean': sum(values) / len(values),
            'std': (sum((x - sum(values) / len(values)) ** 2 for x in values) / len(values)) ** 0.5
        }
    
    return axis_summary


def generate_report(G: nx.Graph, output_path: Path):
    centrality = compute_centrality(G)
    bridges = find_bridge_nodes(G)
    clusters = find_clusters(G)
    outliers = find_outliers(G, centrality)
    edge_types = analyze_edge_types(G)
    axis_summary = analyze_philosophical_axes(G)
    
    with open(output_path, 'w') as f:
        f.write("Philosophical Rules Network Analysis Report\n")
        f.write("=" * 50 + "\n\n")
        
        f.write("Graph Statistics\n")
        f.write("-" * 30 + "\n")
        f.write(f"Total Nodes: {G.number_of_nodes()}\n")
        f.write(f"Total Edges: {G.number_of_edges()}\n")
        f.write(f"Network Density: {nx.density(G):.3f}\n")
        f.write(f"Average Clustering: {nx.average_clustering(G):.3f}\n\n")
        
        f.write("Edge Type Distribution\n")
        f.write("-" * 30 + "\n")
        for edge_type, count in sorted(edge_types.items()):
            f.write(f"  {edge_type}: {count}\n")
        f.write("\n")
        
        f.write("Bridge Nodes (High Betweenness Centrality)\n")
        f.write("-" * 30 + "\n")
        for node, score in bridges[:5]:
            node_data = G.nodes[node]
            f.write(f"  {node_data['name']}: {score:.3f}\n")
        f.write("\n")
        
        f.write("Top Nodes by Degree Centrality\n")
        f.write("-" * 30 + "\n")
        top_degree = sorted(centrality.items(), key=lambda x: x[1]['degree'], reverse=True)[:5]
        for node, metrics in top_degree:
            node_data = G.nodes[node]
            f.write(f"  {node_data['name']}: {metrics['degree']:.3f}\n")
        f.write("\n")
        
        if clusters:
            f.write("Philosophical Clusters\n")
            f.write("-" * 30 + "\n")
            for i, cluster in enumerate(clusters, 1):
                f.write(f"  Cluster {i}:\n")
                for node_id in cluster:
                    node_data = G.nodes[node_id]
                    f.write(f"    - {node_data['name']}\n")
            f.write("\n")
        
        if outliers:
            f.write("Outlier Philosophies (Low Centrality)\n")
            f.write("-" * 30 + "\n")
            for node_id in outliers:
                node_data = G.nodes[node_id]
                f.write(f"  - {node_data['name']}\n")
            f.write("\n")
        
        f.write("Philosophical Axis Statistics\n")
        f.write("-" * 30 + "\n")
        for axis, stats in axis_summary.items():
            f.write(f"  {axis}:\n")
            f.write(f"    Min: {stats['min']:.2f}\n")
            f.write(f"    Max: {stats['max']:.2f}\n")
            f.write(f"    Mean: {stats['mean']:.2f}\n")
            f.write(f"    Std: {stats['std']:.2f}\n")
        f.write("\n")
        
        f.write("Node Details\n")
        f.write("-" * 30 + "\n")
        for node_id, data in G.nodes(data=True):
            f.write(f"\n{data['name']} ({node_id})\n")
            f.write(f"  Source: {data['source']}\n")
            f.write(f"  Description: {data['description']}\n")
            f.write(f"  Influence Weight: {data.get('influenceWeight', 0)}\n")
            f.write(f"  Centrality Scores:\n")
            f.write(f"    Betweenness: {centrality[node_id]['betweenness']:.3f}\n")
            f.write(f"    Degree: {centrality[node_id]['degree']:.3f}\n")
            f.write(f"    Closeness: {centrality[node_id]['closeness']:.3f}\n")
            f.write(f"  Axis Scores:\n")
            for axis, value in data['axes'].items():
                f.write(f"    {axis}: {value}\n")
    
    print(f"Analysis report generated: {output_path}")


def main():
    project_root = Path(__file__).parent.parent
    rules_path = project_root / 'data' / 'rules.json'
    relationships_path = project_root / 'data' / 'relationships.json'
    output_dir = project_root / 'output'
    
    G = build_complete_graph(rules_path, relationships_path)
    
    report_path = output_dir / 'analysis_report.txt'
    generate_report(G, report_path)
    
    print("\nQuick Summary:")
    print(f"  Nodes: {G.number_of_nodes()}")
    print(f"  Edges: {G.number_of_edges()}")
    print(f"  Density: {nx.density(G):.3f}")
    print(f"  Average Clustering: {nx.average_clustering(G):.3f}")


if __name__ == '__main__':
    main()
