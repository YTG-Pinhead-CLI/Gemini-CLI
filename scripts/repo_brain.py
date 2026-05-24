import os
import json

def get_repo_structure(root_dir='.'):
    nodes = []
    links = []
    
    # Ignore patterns
    ignore_dirs = {'.git', 'node_modules', '__pycache__', '.gemini'}
    
    # Root node
    nodes.append({"id": "root", "name": os.path.basename(os.path.abspath(root_dir)), "group": 0, "size": 20})

    for root, dirs, files in os.walk(root_dir):
        # Filter directories
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        
        rel_path = os.path.relpath(root, root_dir)
        parent_id = "root" if rel_path == "." else rel_path
        
        # Add directories as nodes
        if rel_path != ".":
            nodes.append({
                "id": rel_path,
                "name": os.path.basename(root),
                "group": 1,
                "size": 15
            })
            # Link to parent
            grandparent = os.path.dirname(rel_path)
            link_source = "root" if grandparent == "" else grandparent
            links.append({"source": link_source, "target": rel_path, "value": 1})

        # Add files
        for file in files:
            file_path = os.path.join(rel_path, file)
            file_id = file_path.replace("\\", "/")
            
            try:
                size = os.path.getsize(os.path.join(root, file))
            except OSError:
                size = 0
                
            nodes.append({
                "id": file_id,
                "name": file,
                "group": 2,
                "size": max(5, min(size // 1000, 30)), # Scale size
                "type": os.path.splitext(file)[1]
            })
            links.append({"source": parent_id, "target": file_id, "value": 1})

    return {"nodes": nodes, "links": links}

if __name__ == "__main__":
    data = get_repo_structure()
    with open('repo_data.json', 'w') as f:
        json.dump(data, f, indent=2)
    print("Repository structure saved to repo_data.json")
