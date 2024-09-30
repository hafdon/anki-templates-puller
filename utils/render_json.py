import json

def render_json_with_line_breaks(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    def print_with_breaks(obj, indent=0):
        spacing = '  ' * indent
        if isinstance(obj, dict):
            for key, value in obj.items():
                print(f"{spacing}{key}:")
                print_with_breaks(value, indent + 1)
        elif isinstance(obj, list):
            for item in obj:
                print_with_breaks(item, indent + 1)
        else:
            if isinstance(obj, str):
                # Replace \n with actual line breaks
                obj = obj.replace('\\n', '\n')
            print(f"{spacing}{obj}")

    print_with_breaks(data)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python render_json.py path/to/file.json")
    else:
        render_json_with_line_breaks(sys.argv[1])
