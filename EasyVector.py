class VectorPrint:
    
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
            contenido = VectorPrint.format_item(submatrix, defEleLen)
            return [
                f"╔{'═' * (defEleLen + 2)}╗",
                f"║ {contenido} ║",
                f"╚{'═' * (defEleLen + 2)}╝"
            ]

        if all(not isinstance(i, list) for i in submatrix):
            fila = [VectorPrint.format_item(x, defEleLen) for x in submatrix]
            top = "╔" + "╦".join(["═" * (defEleLen + 2)] * len(fila)) + "╗"
            mid = "║" + "║".join([f" {x} " for x in fila]) + "║"
            bot = "╚" + "╩".join(["═" * (defEleLen + 2)] * len(fila)) + "╝"
            return [top, mid, bot]

        bloques = [VectorPrint.render_matrix_block(row, defEleLen) for row in submatrix]
        altura_max = max(len(b) for b in bloques)
        for b in bloques:
            while len(b) < altura_max:
                b.insert(-1, "║" + " " * (len(b[0]) - 2) + "║")
        return VectorPrint.combine_blocks_vertically(bloques)

    @staticmethod
    def combine_blocks_vertically(bloques):
        result = []
        ancho = len(bloques[0][0])
        result.append("╔" + "═" * (ancho - 2) + "╗")
        for i, block in enumerate(bloques):
            result.extend(block[1:-1])
            if i < len(bloques) - 1:
                result.append("╠" + "═" * (ancho - 2) + "╣")
        result.append("╚" + "═" * (ancho - 2) + "╝")
        return result

    @staticmethod
    def print(matrix, defEleLen=7):
        # Si no es lista, imprimir tal cual
        if not isinstance(matrix, list):
            print(str(matrix))
            return
        
        # Si es una matriz plana o vector
        if all(not isinstance(item, list) for item in matrix):
            VectorPrint.draw_table([matrix], defEleLen)
            return

        # Si es matriz bidimensional normal
        if all(isinstance(row, list) and all(not isinstance(el, list) for el in row) for row in matrix):
            VectorPrint.draw_table(matrix, defEleLen)
            return

        # Si es una estructura de más dimensiones
        # Recorrer recursivamente hasta que cada subnivel sea 2D
        submatrices = VectorPrint.flatten_to_2d_blocks(matrix)

        for idx, submatrix in enumerate(submatrices):
            print(f"Bloque #{idx}")
            VectorPrint.print(submatrix, defEleLen)
            print()

    @staticmethod
    def flatten_to_2d_blocks(data):
        """ Aplana recursivamente una estructura N-dimensional en una lista de matrices 2D """
        if not isinstance(data, list):
            return [data]
        
        if all(isinstance(row, list) and all(not isinstance(col, list) for col in row) for row in data):
            return [data]
        
        blocks = []
        for item in data:
            blocks.extend(VectorPrint.flatten_to_2d_blocks(item))
        return blocks

    @staticmethod
    def draw_table(matriz, defEleLen):
        cols = len(matriz[0])
        print("╔" + "╦".join(["═" * (defEleLen + 2)] * cols) + "╗")
        for i, fila in enumerate(matriz):
            print("║", end="")
            for item in fila:
                print(" " + VectorPrint.format_item(item, defEleLen) + " ║", end="")
            print()
            if i < len(matriz) - 1:
                print("╠" + "╬".join(["═" * (defEleLen + 2)] * cols) + "╣")
            else:
                print("╚" + "╩".join(["═" * (defEleLen + 2)] * cols) + "╝")


#--------------------------------------------------------------------------------------------
#===========================================================================================

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
    def print(data):
        VectorPrint.print(data)
        
        