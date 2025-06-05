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
    def draw_table(matriz, defEleLen):
        cols = len(matriz[0])
        result = []
        result.append("╔" + "╦".join(["═" * (defEleLen + 2)] * cols) + "╗")
        for i, fila in enumerate(matriz):
            result.append("║" + "║".join([f" {VectorPrint.format_item(item, defEleLen)} " for item in fila]) + "║")
            if i < len(matriz) - 1:
                result.append("╠" + "╬".join(["═" * (defEleLen + 2)] * cols) + "╣")
            else:
                result.append("╚" + "╩".join(["═" * (defEleLen + 2)] * cols) + "╝")
        return result

    @staticmethod
    def print(matrix, defEleLen=7):
        if not isinstance(matrix, list):
            print(str(matrix))
            return

        if all(not isinstance(item, list) for item in matrix):
            for line in VectorPrint.draw_table([matrix], defEleLen):
                print(line)
            return

        if all(isinstance(row, list) and all(not isinstance(col, list) for col in row) for row in matrix):
            for line in VectorPrint.draw_table(matrix, defEleLen):
                print(line)
            return

        submatrices = VectorPrint.flatten_to_2d_blocks(matrix)

        # Detectar si es una lista plana de bloques (como un vector de matrices)
        if isinstance(matrix, list) and all(isinstance(e, list) for e in matrix) and all(VectorPrint.is_matrix(sub) for sub in matrix):
            # Mostrar todos en una sola fila
            headers = [f"Bloque {i} de {len(submatrices)-1}" for i in range(len(submatrices))]
            block_lines = [VectorPrint.draw_table(m, defEleLen) for m in submatrices]

            # Calcular máximo de líneas por bloque
            max_lines = max(len(b) for b in block_lines)
            for b in block_lines:
                while len(b) < max_lines:
                    b.append(" " * len(b[0]))

            # Imprimir encabezados alineados
            header_line = "     ".join(h.ljust(len(block_lines[i][0])) for i, h in enumerate(headers))
            print(header_line)

            # Imprimir todas las líneas combinadas horizontalmente
            for i in range(max_lines):
                print("     ".join(block[i] for block in block_lines))
            return

        # Si no son bloques de vector plano, imprimir uno debajo del otro
        for idx, submatrix in enumerate(submatrices):
            print(f"Bloque {idx} de {len(submatrices)-1}")
            for line in VectorPrint.draw_table(submatrix, defEleLen):
                print(line)
            print()

    @staticmethod
    def is_matrix(mat):
        return isinstance(mat, list) and all(isinstance(row, list) and all(not isinstance(el, list) for el in row) for row in mat)

    @staticmethod
    def flatten_to_2d_blocks(data):
        """ Aplana recursivamente una estructura N-dimensional en una lista de matrices 2D """
        if not isinstance(data, list):
            return [data]
        
        if VectorPrint.is_matrix(data):
            return [data]
        
        blocks = []
        for item in data:
            blocks.extend(VectorPrint.flatten_to_2d_blocks(item))
        return blocks



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
        
        