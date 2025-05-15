import os

def find_git_root(start_path='.'):
    current = os.path.abspath(start_path)
    while current != os.path.dirname(current):
        if os.path.isdir(os.path.join(current, '.git')):
            return current
        current = os.path.dirname(current)
    return None

def list_folder_structure(base_path, prefix=''):
    ignore = {'.git', '.venv', '__pycache__'}
    try:
        items = sorted(os.listdir(base_path))
        for item in items:
            if item.startswith('.') or item in ignore:
                continue
            full_path = os.path.join(base_path, item)
            if os.path.isdir(full_path):
                print(f"{prefix}📁 {item}/")
                list_folder_structure(full_path, prefix + '    ')
            else:
                print(f"{prefix}📄 {item}")
    except PermissionError:
        print(f"{prefix}🔒 [Permission denied]")

if __name__ == "__main__":
    root = find_git_root()
    if root:
        print(f"\n🧭 Git root found at: {root}\n\n📂 Project Folder Structure:\n")
        list_folder_structure(root)
    else:
        print("❌ Git root not found. Are you inside a valid repo?")
