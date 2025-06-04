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
