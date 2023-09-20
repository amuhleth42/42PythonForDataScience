class calculator:
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        if len(V1) != len(V2):
            print("Both lists must have the same length")
        else:
            res = sum([(x * y) for x, y in  zip(V1, V2)])
            print(f"Dot product is: {res}")


    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        if len(V1) != len(V2):
            print("Both lists must have the same length")
        else:
            res = [float(x + y) for x, y in  zip(V1, V2)]
            print(f"Add vector is: {res}")
    

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        if len(V1) != len(V2):
            print("Both lists must have the same length")
        else:
            res = [float(x - y) for x, y in zip(V1, V2)]
            print(f"Add vector is: {res}")
