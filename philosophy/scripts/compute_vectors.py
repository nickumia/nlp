import json
import numpy as np
from pathlib import Path
from typing import Dict, List, Tuple


def load_rules(rules_path: str) -> List[Dict]:
    with open(rules_path, 'r') as f:
        return json.load(f)


def rule_to_vector(rule: Dict) -> np.ndarray:
    axes = rule['axes']
    vector = np.array([
        axes['conflict'],
        axes['truth'],
        axes['order'],
        axes['will'],
        axes['risk'],
        axes['time']
    ])
    return vector


def compute_euclidean_distance(vec1: np.ndarray, vec2: np.ndarray) -> float:
    return np.linalg.norm(vec1 - vec2)


def compute_similarity_matrix(rules: List[Dict]) -> Dict[str, Dict[str, float]]:
    rule_ids = [rule['id'] for rule in rules]
    vectors = {rule['id']: rule_to_vector(rule) for rule in rules}
    
    similarity_matrix = {}
    for id1 in rule_ids:
        similarity_matrix[id1] = {}
        for id2 in rule_ids:
            if id1 != id2:
                distance = compute_euclidean_distance(vectors[id1], vectors[id2])
                similarity_matrix[id1][id2] = distance
    
    return similarity_matrix


def find_similar_rules(similarity_matrix: Dict[str, Dict[str, float]], 
                      threshold: float = 1.0) -> List[Tuple[str, str]]:
    similar_pairs = []
    rule_ids = list(similarity_matrix.keys())
    
    for i, id1 in enumerate(rule_ids):
        for id2 in rule_ids[i+1:]:
            distance = similarity_matrix[id1][id2]
            if distance < threshold:
                similar_pairs.append((id1, id2, distance))
    
    return sorted(similar_pairs, key=lambda x: x[2])


def find_opposing_rules(similarity_matrix: Dict[str, Dict[str, float]], 
                        threshold: float = 2.0) -> List[Tuple[str, str]]:
    opposing_pairs = []
    rule_ids = list(similarity_matrix.keys())
    
    for i, id1 in enumerate(rule_ids):
        for id2 in rule_ids[i+1:]:
            distance = similarity_matrix[id1][id2]
            if distance > threshold:
                opposing_pairs.append((id1, id2, distance))
    
    return sorted(opposing_pairs, key=lambda x: x[2], reverse=True)


def get_rule_vectors(rules: List[Dict]) -> Dict[str, np.ndarray]:
    return {rule['id']: rule_to_vector(rule) for rule in rules}


if __name__ == '__main__':
    rules_path = Path(__file__).parent.parent / 'data' / 'rules.json'
    rules = load_rules(rules_path)
    
    similarity_matrix = compute_similarity_matrix(rules)
    
    print("Similarity Matrix:")
    for id1, distances in similarity_matrix.items():
        print(f"\n{id1}:")
        for id2, dist in sorted(distances.items(), key=lambda x: x[1]):
            print(f"  {id2}: {dist:.3f}")
    
    print("\n\nMost Similar Rules (distance < 1.0):")
    similar = find_similar_rules(similarity_matrix, threshold=1.0)
    for id1, id2, dist in similar:
        print(f"  {id1} <-> {id2}: {dist:.3f}")
    
    print("\n\nMost Opposing Rules (distance > 2.0):")
    opposing = find_opposing_rules(similarity_matrix, threshold=2.0)
    for id1, id2, dist in opposing:
        print(f"  {id1} <-> {id2}: {dist:.3f}")
