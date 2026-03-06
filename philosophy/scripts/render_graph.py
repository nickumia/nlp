import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent))
from build_graph import build_complete_graph


def get_edge_color(edge_type: str) -> str:
    colors = {
        'support': '#2ecc71',
        'oppose': '#e74c3c',
        'similar': '#95a5a6',
        'contextual': '#f39c12',
        'similarity': '#3498db',
        'opposing': '#9b59b6'
    }
    return colors.get(edge_type, '#7f8c8d')


def get_edge_style(edge_type: str) -> str:
    if edge_type == 'contextual':
        return '--'
    return '-'


def render_static_graph(G: nx.Graph, output_path: Path, figsize=(16, 12)):
    plt.figure(figsize=figsize)
    
    pos = nx.spring_layout(G, k=2, iterations=50, seed=42)
    
    edge_colors = []
    edge_styles = []
    edge_widths = []
    
    for u, v, data in G.edges(data=True):
        edge_type = data.get('type', 'unknown')
        edge_colors.append(get_edge_color(edge_type))
        edge_styles.append(get_edge_style(edge_type))
        
        if edge_type in ['support', 'similar', 'similarity']:
            edge_widths.append(1.5)
        elif edge_type in ['oppose', 'opposing']:
            edge_widths.append(2.5)
        else:
            edge_widths.append(1.0)
    
    node_sizes = []
    for node_id, data in G.nodes(data=True):
        node_sizes.append(1500)  # Fixed size for all nodes
    
    nx.draw_networkx_nodes(G, pos, node_size=node_sizes, 
                          node_color='#ecf0f1', edgecolors='#2c3e50', 
                          linewidths=2, alpha=0.9)
    
    for i, (u, v) in enumerate(G.edges()):
        nx.draw_networkx_edges(G, pos, edgelist=[(u, v)], 
                              edge_color=[edge_colors[i]], 
                              style=edge_styles[i],
                              width=edge_widths[i],
                              alpha=0.7)
    
    labels = {node_id: data['name'] for node_id, data in G.nodes(data=True)}
    nx.draw_networkx_labels(G, pos, labels, font_size=10, 
                           font_weight='bold', font_family='sans-serif')
    
    legend_elements = [
        plt.Line2D([0], [0], color='#2ecc71', lw=2, label='Support'),
        plt.Line2D([0], [0], color='#e74c3c', lw=2, label='Oppose'),
        plt.Line2D([0], [0], color='#95a5a6', lw=2, label='Similar'),
        plt.Line2D([0], [0], color='#3498db', lw=2, label='Similarity (auto)'),
        plt.Line2D([0], [0], color='#9b59b6', lw=2, label='Opposing (auto)'),
        plt.Line2D([0], [0], color='#f39c12', lw=2, linestyle='--', label='Contextual')
    ]
    
    plt.legend(handles=legend_elements, loc='upper right', 
              bbox_to_anchor=(1.15, 1))
    
    plt.title('Philosophical Rules Network', fontsize=16, fontweight='bold', pad=20)
    plt.axis('off')
    plt.tight_layout()
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.savefig(output_path.with_suffix('.svg'), format='svg', bbox_inches='tight')
    plt.close()
    
    print(f"Graph rendered to: {output_path}")
    print(f"Graph rendered to: {output_path.with_suffix('.svg')}")


def render_interactive_graph(G: nx.Graph, output_path: Path):
    try:
        from pyvis.network import Network
    except ImportError:
        print("pyvis not installed. Install with: pip install pyvis")
        return
    
    net = Network(height='800px', width='100%', bgcolor='#ffffff', 
                  font_color='black')
    
    net.from_nx(G)
    
    for node in net.nodes:
        node_data = G.nodes[node['id']]
        node['title'] = f"<b>{node_data['name']}</b><br>"
        node['title'] += f"<b>Rule:</b> {node_data['rule']}<br><br>"
        node['title'] += f"<b>When it works:</b> {node_data.get('whenWorks', 'N/A')}<br>"
        node['title'] += f"<b>When it fails:</b> {node_data.get('whenFails', 'N/A')}<br>"
        node['title'] += f"<b>Notes:</b> {node_data.get('notes', 'N/A')}"
        
        node['size'] = 25  # Fixed size for all nodes
        
        axes = node_data['axes']
        node['color'] = get_node_color(axes)
    
    for edge in net.edges:
        edge_data = G.edges[edge['from'], edge['to']]
        edge_type = edge_data.get('type', 'unknown')
        edge['color'] = get_edge_color(edge_type)
        edge['width'] = 2 if edge_type in ['oppose', 'opposing'] else 1
        edge['dashed'] = edge_type == 'contextual'
    
    net.set_options("""
    {
      "physics": {
        "enabled": true,
        "barnesHut": {
          "gravitationalConstant": -2000,
          "centralGravity": 0.3,
          "springLength": 200,
          "springConstant": 0.04
        }
      },
      "nodes": {
        "font": {
          "size": 14
        }
      },
      "edges": {
        "smooth": {
          "type": "continuous"
        }
      }
    }
    """)
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    net.save_graph(str(output_path))
    print(f"Interactive graph rendered to: {output_path}")


def get_node_color(axes: dict) -> str:
    conflict = axes['conflict']
    truth = axes['truth']
    
    if conflict > 0.5:
        return '#e74c3c'
    elif conflict < -0.5:
        return '#2ecc71'
    elif truth > 0.5:
        return '#3498db'
    elif truth < -0.5:
        return '#9b59b6'
    else:
        return '#95a5a6'


def main():
    project_root = Path(__file__).parent.parent
    rules_path = project_root / 'data' / 'rules.json'
    output_dir = project_root / 'output'
    
    G = build_complete_graph(rules_path)
    
    png_path = output_dir / 'philosophy_map.png'
    render_static_graph(G, png_path)
    
    html_path = output_dir / 'philosophy_map.html'
    render_interactive_graph(G, html_path)


if __name__ == '__main__':
    main()
