class Vector:

    @staticmethod
    def Int(*dimensions):
        return Vector._create_vector(0, dimensions)

    @staticmethod
    def Char(*dimensions):
        return Vector._create_vector(' ', dimensions)

    @staticmethod
    def Float(*dimensions):
        return Vector._create_vector(0.0, dimensions)

    @staticmethod
    def String(*dimensions):
        return Vector._create_vector('', dimensions)

    @staticmethod
    def _create_vector(default_value, dimensions):
        if not dimensions:
            return default_value

        if len(dimensions) == 1:
            return [default_value] * dimensions[0]

        return [
            Vector._create_vector(
                default_value,
                dimensions[1:]
            ) for _ in range(dimensions[0])
        ]
        
        
    @staticmethod
    def _create_vector(default_value, dimensions):
        if not dimensions:
            return default_value

        if len(dimensions) == 1:
            return [default_value] * dimensions[0]

        return [
            Vector._create_vector(
                default_value,
                dimensions[1:]
            ) for _ in range(dimensions[0])
        ]
    @staticmethod
    def print(matrix, defEleLen=10):
        if not isinstance(matrix, list):
            print(str(matrix))
            return

        if all(not isinstance(item, list) for item in matrix):
            # Es un vector simple
            Vector.draw_table([matrix], defEleLen)
        elif all(isinstance(item, list) and all(not isinstance(subitem, list) for subitem in item) for item in matrix):
            # Es una matriz 2D
            Vector.draw_table(matrix, defEleLen)
        else:
            # Es una matriz de más dimensiones
            filas = []
            max_altura = 0
            for row in matrix:
                fila_renderizada = []
                max_lineas = 0
                for item in row:
                    bloque = Vector.render_matrix_block(item, defEleLen)
                    fila_renderizada.append(bloque)
                    max_lineas = max(max_lineas, len(bloque))
                # Rellenar para igualar altura
                for i in range(len(fila_renderizada)):
                    while len(fila_renderizada[i]) < max_lineas:
                        fila_renderizada[i].append(" " * (defEleLen + 4))
                filas.append(fila_renderizada)

            ancho = len(filas[0])
            print("╔" + "╦".join(["═" * (defEleLen + 4)] * ancho) + "╗")
            for i, fila in enumerate(filas):
                for linea in range(len(fila[0])):
                    print("║", end="")
                    for celda in fila:
                        print(" " + celda[linea].ljust(defEleLen + 2) + "║", end="")
                    print()
                if i < len(filas) - 1:
                    print("╠" + "╬".join(["═" * (defEleLen + 4)] * ancho) + "╣")
                else:
                    print("╚" + "╩".join(["═" * (defEleLen + 4)] * ancho) + "╝")

    @staticmethod
    def draw_table(matriz, defEleLen):
        cols = len(matriz[0])
        print("╔" + "╦".join(["═" * (defEleLen + 2)] * cols) + "╗")
        for i, fila in enumerate(matriz):
            print("║", end="")
            for item in fila:
                print(" " + Vector.format_item(item, defEleLen) + " ║", end="")
            print()
            if i < len(matriz) - 1:
                print("╠" + "╬".join(["═" * (defEleLen + 2)] * cols) + "╣")
            else:
                print("╚" + "╩".join(["═" * (defEleLen + 2)] * cols) + "╝")

    @staticmethod
    def format_item(item, defEleLen):
        if item == "":
            return " " * defEleLen
        elif isinstance(item, str):
            return f"\"{item}\"".ljust(defEleLen)
        else:
            return str(item).ljust(defEleLen)

    @staticmethod
    def render_matrix_block(submatrix, defEleLen):
        """Devuelve una lista de líneas con marco ASCII para una submatriz"""
        if not isinstance(submatrix, list):
            return [f"╔{'═' * (defEleLen + 2)}╗",
                    f"║ {Vector.format_item(submatrix, defEleLen)} ║",
                    f"╚{'═' * (defEleLen + 2)}╝"]

        if all(not isinstance(item, list) for item in submatrix):
            contenido = f"║" + "║".join([f" {Vector.format_item(x, defEleLen)} " for x in submatrix]) + "║"
            top = "╔" + "╦".join(["═" * (defEleLen + 2)] * len(submatrix)) + "╗"
            bot = "╚" + "╩".join(["═" * (defEleLen + 2)] * len(submatrix)) + "╝"
            return [top, contenido, bot]

        # Submatriz (2D)
        filas = []
        cols = len(submatrix[0])
        filas.append("╔" + "╦".join(["═" * (defEleLen + 2)] * cols) + "╗")
        for i, fila in enumerate(submatrix):
            line = "║"
            for item in fila:
                line += f" {Vector.format_item(item, defEleLen)} ║"
            filas.append(line)
            if i < len(submatrix) - 1:
                filas.append("╠" + "╬".join(["═" * (defEleLen + 2)] * cols) + "╣")
            else:
                filas.append("╚" + "╩".join(["═" * (defEleLen + 2)] * cols) + "╝")
        return filas
