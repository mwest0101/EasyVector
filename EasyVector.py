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
    def format_item(item, defEleLen):
        if item == "":
            return " " * defEleLen
        elif isinstance(item, str):
            return f"\"{item}\"".ljust(defEleLen)
        else:
            return str(item).ljust(defEleLen)

    @staticmethod
    def render_matrix_block(submatrix, defEleLen):
        if not isinstance(submatrix, list):
            contenido = Vector.format_item(submatrix, defEleLen)
            return [
                f"╔{'═' * (defEleLen + 2)}╗",
                f"║ {contenido} ║",
                f"╚{'═' * (defEleLen + 2)}╝"
            ]

        if all(not isinstance(i, list) for i in submatrix):
            fila = [Vector.format_item(x, defEleLen) for x in submatrix]
            top = "╔" + "╦".join(["═" * (defEleLen + 2)] * len(fila)) + "╗"
            mid = "║" + "║".join([f" {x} " for x in fila]) + "║"
            bot = "╚" + "╩".join(["═" * (defEleLen + 2)] * len(fila)) + "╝"
            return [top, mid, bot]

        # Submatriz 2D o más
        bloques = [Vector.render_matrix_block(row, defEleLen) for row in submatrix]
        altura_max = max(len(b) for b in bloques)
        ancho_max = max(len(line) for b in bloques for line in b)

        for i, b in enumerate(bloques):
            while len(b) < altura_max:
                b.insert(-1, "║" + " " * (len(b[0]) - 2) + "║")  # línea vacía antes del borde inferior

        return Vector.combine_blocks_vertically(bloques)

    @staticmethod
    def combine_blocks_vertically(bloques):
        result = []
        ancho = len(bloques[0][0])
        result.append("╔" + "═" * (ancho - 2) + "╗")
        for i, block in enumerate(bloques):
            result.extend(block[1:-1])  # sin marco superior/inferior del subbloque
            if i < len(bloques) - 1:
                result.append("╠" + "═" * (ancho - 2) + "╣")
        result.append("╚" + "═" * (ancho - 2) + "╝")
        return result

    @staticmethod
    def print(matrix, defEleLen=7):
        if not isinstance(matrix, list):
            print(str(matrix))
            return

        if all(not isinstance(item, list) for item in matrix):
            Vector.draw_table([matrix], defEleLen)
            return

        if all(isinstance(row, list) and all(not isinstance(el, list) for el in row) for row in matrix):
            Vector.draw_table(matrix, defEleLen)
            return

        filas = []
        for fila in matrix:
            fila_renderizada = [Vector.render_matrix_block(celda, defEleLen) for celda in fila]
            altura = max(len(b) for b in fila_renderizada)
            for b in fila_renderizada:
                while len(b) < altura:
                    b.insert(-1, "║" + " " * (len(b[0]) - 2) + "║")
            filas.append(fila_renderizada)

        ancho_celda = len(filas[0][0][0])
        columnas = len(filas[0])
        print("╔" + "╦".join(["═" * ancho_celda] * columnas) + "╗")
        for i, fila in enumerate(filas):
            for linea_idx in range(len(fila[0])):
                print("║", end="")
                for celda in fila:
                    print(celda[linea_idx], end="║")
                print()
            if i < len(filas) - 1:
                print("╠" + "╬".join(["═" * ancho_celda] * columnas) + "╣")
            else:
                print("╚" + "╩".join(["═" * ancho_celda] * columnas) + "╝")

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
