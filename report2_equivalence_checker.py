"""
Report 2 - Equivalence Relation Checker
Discrete Mathematics

Set: A = {1, 2, 3, 4, 5}
Input: a 5 x 5 binary relation matrix

Run:
    python report2_equivalence_checker.py
"""

N = 5
ELEMENTS = [1, 2, 3, 4, 5]


def print_matrix(matrix, title="Relation matrix"):
    """Print a relation matrix in a readable format."""
    print(f"\n{title}")
    print("    " + " ".join(str(x) for x in ELEMENTS))
    print("   " + "--" * N)
    for i, row in enumerate(matrix):
        print(f"{ELEMENTS[i]} |  " + " ".join(str(value) for value in row))


def input_matrix():
    """Receive a 5 x 5 matrix from the user, one row at a time."""
    print("\nEnter a 5 x 5 matrix.")
    print("For each row, enter five values (0 or 1), separated by spaces.")
    print("Example row: 1 0 0 1 0")

    matrix = []
    for row_number in range(N):
        while True:
            raw = input(f"Row {row_number + 1}: ").strip()
            values = raw.replace(",", " ").split()

            # Also accept compact input such as 10010.
            if len(values) == 1 and len(values[0]) == N and values[0].isdigit():
                values = list(values[0])

            if len(values) != N or any(value not in ("0", "1") for value in values):
                print("Invalid input. Please enter exactly five 0/1 values.")
                continue

            matrix.append([int(value) for value in values])
            break

    return matrix


def is_reflexive(matrix):
    """A relation is reflexive when every diagonal entry is 1."""
    return all(matrix[i][i] == 1 for i in range(N))


def is_symmetric(matrix):
    """A relation is symmetric when M[i][j] equals M[j][i]."""
    for i in range(N):
        for j in range(N):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True


def is_transitive(matrix):
    """A relation is transitive when i->j and j->k imply i->k."""
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if matrix[i][j] == 1 and matrix[j][k] == 1 and matrix[i][k] == 0:
                    return False
    return True


def check_properties(matrix):
    """Check and display the three required properties."""
    reflexive = is_reflexive(matrix)
    symmetric = is_symmetric(matrix)
    transitive = is_transitive(matrix)

    print("\nProperty check")
    print(f"1. Reflexive  : {'YES' if reflexive else 'NO'}")
    print(f"2. Symmetric  : {'YES' if symmetric else 'NO'}")
    print(f"3. Transitive : {'YES' if transitive else 'NO'}")

    is_equivalence = reflexive and symmetric and transitive
    print("Equivalence relation:", "YES" if is_equivalence else "NO")
    return is_equivalence


def reflexive_closure(matrix):
    """Add every missing diagonal pair (i, i)."""
    result = [row[:] for row in matrix]
    for i in range(N):
        result[i][i] = 1
    return result


def symmetric_closure(matrix):
    """Add the reverse pair for every existing pair."""
    result = [row[:] for row in matrix]
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                result[j][i] = 1
    return result


def transitive_closure(matrix, show_steps=False):
    """Compute transitive closure using Warshall's algorithm."""
    result = [row[:] for row in matrix]

    if show_steps:
        print_matrix(result, "Warshall algorithm - initial matrix")

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if result[i][k] == 1 and result[k][j] == 1:
                    result[i][j] = 1

        if show_steps:
            print_matrix(result, f"After step k = {ELEMENTS[k]}")

    return result


def equivalence_classes(matrix):
    """Return the equivalence class of each element."""
    classes = []
    used = set()

    for i in range(N):
        if ELEMENTS[i] in used:
            continue

        current_class = [
            ELEMENTS[j] for j in range(N) if matrix[i][j] == 1
        ]
        classes.append(current_class)
        used.update(current_class)

    return classes


def show_equivalence_classes(matrix):
    """Display equivalence classes if the relation is an equivalence relation."""
    if not (is_reflexive(matrix) and is_symmetric(matrix) and is_transitive(matrix)):
        print("\nEquivalence classes cannot be displayed because the relation")
        print("is not an equivalence relation.")
        return

    print("\nEquivalence classes:")
    for element in ELEMENTS:
        related = [x for x in ELEMENTS if matrix[element - 1][x - 1] == 1]
        print(f"[{element}] = {related}")


def apply_closures(matrix):
    """Apply each required closure only when its property is missing."""
    result = [row[:] for row in matrix]

    if not is_reflexive(result):
        print("\nApplying reflexive closure...")
        result = reflexive_closure(result)
        print_matrix(result, "After reflexive closure")

    if not is_symmetric(result):
        print("\nApplying symmetric closure...")
        result = symmetric_closure(result)
        print_matrix(result, "After symmetric closure")

    if not is_transitive(result):
        print("\nApplying transitive closure with Warshall's algorithm...")
        result = transitive_closure(result, show_steps=True)

    return result


def load_example():
    """A sample equivalence relation with classes {1, 2} and {3, 4, 5}."""
    return [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 1, 1],
        [0, 0, 1, 1, 1],
        [0, 0, 1, 1, 1],
    ]


def main():
    print("=" * 58)
    print("       EQUIVALENCE RELATION CHECKER - REPORT 2")
    print("=" * 58)
    print("Set A = {1, 2, 3, 4, 5}")
    print("\nChoose an input method:")
    print("1. Enter my own 5 x 5 matrix")
    print("2. Load the built-in example matrix")

    while True:
        choice = input("\nYour choice (1 or 2): ").strip()
        if choice == "1":
            matrix = input_matrix()
            break
        if choice == "2":
            matrix = load_example()
            print("\nBuilt-in example loaded.")
            break
        print("Please enter 1 or 2.")

    print_matrix(matrix, "Original relation matrix")
    original_is_equivalence = check_properties(matrix)

    if original_is_equivalence:
        print("\nThe original relation is already an equivalence relation.")
        show_equivalence_classes(matrix)
    else:
        print("\nThe original relation is not an equivalence relation.")
        answer = input("Apply the required closures? (y/n): ").strip().lower()

        if answer == "y":
            closed_matrix = apply_closures(matrix)
            print_matrix(closed_matrix, "Final matrix after closures")
            final_is_equivalence = check_properties(closed_matrix)

            if final_is_equivalence:
                print("\nAll three properties are now satisfied.")
                show_equivalence_classes(closed_matrix)
            else:
                print("\nThe resulting relation is not an equivalence relation.")
        else:
            print("Closure operations skipped.")

    print("\nProgram finished successfully.")


if __name__ == "__main__":
    main()
