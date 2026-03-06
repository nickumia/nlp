import json
import networkx as nx
from pathlib import Path
from typing import Dict, List
import sys
sys.path.append(str(Path(__file__).parent))
from compute_vectors import compute_similarity_matrix, find_similar_rules, find_opposing_rules


def load_rules(rules_path: str) -> List[Dict]:
    with open(rules_path, 'r') as f:
        return json.load(f)


def load_relationships(relationships_path: str) -> List[Dict]:
    with open(relationships_path, 'r') as f:
        return json.load(f)


def build_graph(rules: List[Dict], relationships: List[Dict], 
                similarity_threshold: float = 1.0,
                opposing_threshold: float = 2.0) -> nx.Graph:
    G = nx.Graph()
    
    for rule in rules:
        G.add_node(
            rule['id'],
            name=rule['name'],
            rule=rule['rule'],
            axes=rule['axes'],
            whenWorks=rule.get('whenWorks', ''),
            whenFails=rule.get('whenFails', ''),
            influenceWeight=rule.get('influenceWeight', 0.5),
            notes=rule.get('notes', '')
        )
    
    for rel in relationships:
        source = rel['source']
        target = rel['target']
        rel_type = rel['type']
        
        if G.has_node(source) and G.has_node(target):
            G.add_edge(source, target, type=rel_type)
    
    similarity_matrix = compute_similarity_matrix(rules)
    
    similar_pairs = find_similar_rules(similarity_matrix, threshold=similarity_threshold)
    for id1, id2, distance in similar_pairs:
        if not G.has_edge(id1, id2):
            G.add_edge(id1, id2, type='similarity', weight=1.0 / (distance + 0.1))
    
    opposing_pairs = find_opposing_rules(similarity_matrix, threshold=opposing_threshold)
    for id1, id2, distance in opposing_pairs:
        if not G.has_edge(id1, id2):
            G.add_edge(id1, id2, type='opposing', weight=distance)
    
    return G


def add_explicit_rule_relationships(G: nx.Graph, rules: List[Dict]) -> nx.Graph:
    for rule in rules:
        rule_id = rule['id']
        
        for similar_id in rule.get('similarTo', []):
            if G.has_node(similar_id) and not G.has_edge(rule_id, similar_id):
                G.add_edge(rule_id, similar_id, type='similar')
        
        for opposes_id in rule.get('opposes', []):
            if G.has_node(opposes_id) and not G.has_edge(rule_id, opposes_id):
                G.add_edge(rule_id, opposes_id, type='oppose')
    
    return G


def build_complete_graph(rules_path: str, relationships_path: str,
                        similarity_threshold: float = 1.0,
                        opposing_threshold: float = 2.0) -> nx.Graph:
    rules = load_rules(rules_path)
    relationships = load_relationships(relationships_path)
    
    G = build_graph(rules, relationships, similarity_threshold, opposing_threshold)
    G = add_explicit_rule_relationships(G, rules)
    
    return G


if __name__ == '__main__':
    project_root = Path(__file__).parent.parent
    rules_path = project_root / 'data' / 'rules.json'
    relationships_path = project_root / 'data' / 'relationships.json'
    
    G = build_complete_graph(rules_path, relationships_path)
    
    print(f"Graph Statistics:")
    print(f"  Nodes (philosophical rules): {G.number_of_nodes()}")
    print(f"  Edges (relationships): {G.number_of_edges()}")
    
    print(f"\nEdge Types:")
    edge_types = {}
    for u, v, data in G.edges(data=True):
        edge_type = data.get('type', 'unknown')
        edge_types[edge_type] = edge_types.get(edge_type, 0) + 1
    for edge_type, count in sorted(edge_types.items()):
        print(f"  {edge_type}: {count}")
    
    print(f"\nNodes with highest influence weight:")
    nodes_by_weight = sorted(G.nodes(data=True), 
                            key=lambda x: x[1].get('influenceWeight', 0), 
                            reverse=True)
    for node_id, data in nodes_by_weight[:5]:
        print(f"  {data['name']}: {data.get('influenceWeight', 0)}")
