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
        
    def print(matrix, defEleLen=10):
       if not isinstance(matrix, list):
           print(matrix)
           return

       # Si es una matriz de matrices (más de 2 dimensiones)
       if any(isinstance(row, list) for row in matrix):
           # Asumimos que es una matriz de filas
           filas_formateadas = []

           # Primero formateamos cada celda individual
           for row in matrix:
               fila_formateada = []
               max_lineas = 1
               for item in row:
                   if isinstance(item, list):
                       bloque = Vector.render_submatrix(item, defEleLen)
                       fila_formateada.append(bloque)
                       max_lineas = max(max_lineas, len(bloque))
                   else:
                       bloque = [Vector.format_item(item, defEleLen)]
                       fila_formateada.append(bloque)
               # Normalizamos el alto de todas las celdas
               for i in range(len(fila_formateada)):
                   while len(fila_formateada[i]) < max_lineas:
                       fila_formateada[i].append(" " * defEleLen)
               filas_formateadas.append(fila_formateada)

           # Dibujamos la tabla completa
           ancho = len(filas_formateadas[0])
           print("╔" + "╦".join(["═" * (defEleLen + 2)] * ancho) + "╗")
           for i, fila in enumerate(filas_formateadas):
               for linea in range(len(fila[0])):  # todas las celdas tienen mismo alto
                   print("║", end="")
                   for celda in fila:
                       print(" " + celda[linea].ljust(defEleLen) + " ║", end="")
                   print()
               if i < len(filas_formateadas) - 1:
                   print("╠" + "╬".join(["═" * (defEleLen + 2)] * ancho) + "╣")
               else:
                   print("╚" + "╩".join(["═" * (defEleLen + 2)] * ancho) + "╝")
       else:
           # Vector simple
           print("╔" + "╦".join(["═" * (defEleLen + 2)] * len(matrix)) + "╗")
           print("║", end="")
           for item in matrix:
               print(" " + Vector.format_item(item, defEleLen) + " ║", end="")
           print()
           print("╚" + "╩".join(["═" * (defEleLen + 2)] * len(matrix)) + "╝")


    def format_item(item, defEleLen):
       if item == "":
           return " " * defEleLen
       elif isinstance(item, str):
           return f"\"{item}\"".ljust(defEleLen)
       else:
           return str(item).ljust(defEleLen)


    def render_submatrix(submatrix, defEleLen):
       """Devuelve una lista de líneas como representación de una submatriz"""
       if not isinstance(submatrix, list):
           return [Vector.format_item(submatrix, defEleLen)]
       if not any(isinstance(i, list) for i in submatrix):
           # Vector simple
           return ["[" + ", ".join(Vector.format_item(x, defEleLen).strip() for x in submatrix) + "]"]
       # Si es matriz 2D o más
       result = []
       for row in submatrix:
           if isinstance(row, list):
               line = "[" + ", ".join(Vector.format_item(x, defEleLen).strip() for x in row) + "]"
           else:
               line = "[" + Vector.format_item(row, defEleLen).strip() + "]"
           result.append(line)
       return result

    