from typing import List, Optional

import json



with open("structure.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    
    
def dfs_search(node: dict, target_id: str) -> Optional[List[str]]:
    if node["uuid"] == target_id:
        return [node["uuid"]]
    
    for child in node.get("children", []):
        subpath = dfs_search(child, target_id)
        if subpath is not None:  # have found our target
            return [node["uuid"]] + subpath
    
    return None


def find_path(tree: List[dict], target_id: str) -> Optional[List[str]]:
    for node in tree:
        path = dfs_search(node, target_id)
        if path is not None:
            return path
    
    return None
    
    