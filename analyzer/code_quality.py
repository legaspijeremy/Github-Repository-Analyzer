import ast

from radon import complexity
from radon.complexity import cc_visit
from radon.metrics import mi_visit


def get_python_files(repo):
    """
    Recursively collect all Python files in a repository.
    """
    python_files = []

    def traverse(contents):
        for item in contents:
            try:
                if item.type == "dir":
                    traverse(repo.get_contents(item.path))

                elif item.type == "file" and item.path.endswith(".py"):
                    python_files.append(item)

            except Exception:
                continue

    traverse(repo.get_contents(""))

    return python_files


def count_loc(code):
    """
    Count non-empty lines of code.
    """
    return len(
        [
            line
            for line in code.splitlines()
            if line.strip()
        ]
    )

def analyze_structure(code):

    function_lengths = []
    class_sizes = []

    try:
        tree = ast.parse(code)

        for node in ast.walk(tree):

            if isinstance(node, ast.FunctionDef):

                if hasattr(node, "end_lineno"):

                    length = (
                        node.end_lineno
                        - node.lineno
                        + 1
                    )

                    function_lengths.append(length)

            elif isinstance(node, ast.ClassDef):

                if hasattr(node, "end_lineno"):

                    size = (
                        node.end_lineno
                        - node.lineno
                        + 1
                    )

                    class_sizes.append(size)

    except Exception:
        pass

    return function_lengths, class_sizes

def analyze_complexity(code):

    try:
        results = cc_visit(code)

        if not results:
            return 0

        avg_complexity = (
            sum(result.complexity for result in results)
            / len(results)
        )

        return avg_complexity

    except Exception:
        return 0
    
def analyze_maintainability(code):

    try:
        return mi_visit(code, True)

    except Exception:
        return 0


def analyze_code_quality(repo):
    
    print("[INFO] Searching for Python files...")

    python_files = get_python_files(repo)

    print(f"[INFO] Found {len(python_files)} Python files.")
    print("[INFO] Calculating lines of code...")

    total_loc = 0
    function_lengths = []
    class_sizes = []
    complexities = []
    maintainability_scores = []

    for file in python_files:
        try:
            content = file.decoded_content.decode(
                "utf-8",
                errors="ignore"
            )

            total_loc += count_loc(content)
            funcs, classes = analyze_structure(content)

            function_lengths.extend(funcs)
            class_sizes.extend(classes)
            complexity = analyze_complexity(content)

            if complexity > 0:
                complexities.append(complexity)

            maintainability = analyze_maintainability(content)

            if maintainability > 0:
                maintainability_scores.append(maintainability) 
        
        except Exception:
            continue

    print("[INFO] Code quality analysis completed.")

    avg_function_length = (
        sum(function_lengths) / len(function_lengths)
        if function_lengths
        else 0
        )

    avg_class_size = (
        sum(class_sizes) / len(class_sizes)
        if class_sizes
        else 0
        )
    
    avg_complexity = (
        sum(complexities) / len(complexities)
        if complexities
        else 0
        )
    
    avg_maintainability = (
        sum(maintainability_scores)
        / len(maintainability_scores)
        if maintainability_scores
        else 0
        )

    return {
        "python_files": len(python_files),
        "total_loc": total_loc,
        "avg_function_length": round(avg_function_length, 2),
        "avg_class_size": round(avg_class_size, 2),
        "avg_complexity": round(avg_complexity, 2),
        "avg_maintainability": round(avg_maintainability, 2),
        }