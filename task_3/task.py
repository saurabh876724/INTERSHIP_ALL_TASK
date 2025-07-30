import numpy as np

def get_matrix(name):
    rows = int(input(f"\n{name} - Enter number of rows: "))
    cols = int(input(f"{name} - Enter number of columns: "))
    print(f"Enter elements for {name} row by row (space-separated):")
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        if len(row) != cols:
            print("Invalid row length. Please re-enter.")
            return get_matrix(name)
        matrix.append(row)
    return np.array(matrix)

def show_menu():
    print("\nSelect an operation:")
    print("1. Matrix Addition")
    print("2. Matrix Subtraction")
    print("3. Matrix Multiplication")
    print("4. Transpose of Matrices")
    print("5. Determinant of Matrices")
    print("6. Exit")

def perform_operations(A, B):
    while True:
        show_menu()
        choice = input("Enter your choice (1–6): ")

        if choice == '1':
            if A.shape == B.shape:
                print("\nMatrix Addition Result:\n", A + B)
            else:
                print("Addition not possible. Matrices must have the same shape.")
        elif choice == '2':
            if A.shape == B.shape:
                print("\nMatrix Subtraction Result:\n", A - B)
            else:
                print("Subtraction not possible. Matrices must have the same shape.")
        elif choice == '3':
            if A.shape[1] == B.shape[0]:
                print("\nMatrix Multiplication Result:\n", np.dot(A, B))
            else:
                print("Multiplication not possible. Columns of Matrix A must equal rows of Matrix B.")
        elif choice == '4':
            print("\nTranspose of Matrix A:\n", A.T)
            print("Transpose of Matrix B:\n", B.T)
        elif choice == '5':
            for idx, mat in enumerate([A, B], start=1):
                if mat.shape[0] == mat.shape[1]:
                    print(f"Determinant of Matrix {idx}:\n{np.linalg.det(mat)}")
                else:
                    print(f"Matrix {idx} is not square. Cannot compute determinant.")
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1 to 6.")

def main():
    print("📐 Matrix Operations Tool 📐")
    A = get_matrix("Matrix A")
    B = get_matrix("Matrix B")
    perform_operations(A, B)

if __name__ == "__main__":
    main()
