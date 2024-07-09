class MaquinaCafe:
    def __init__(self):
        self.vasos = {"pequeño": 3, "mediano": 5, "grande": 7}
        self.azucar = 0

    def tamaño_vaso(self, tamaño):
        return f"{self.vasos[tamaño]} Oz"

    def cantidad_azucar(self, cucharadas):
        self.azucar = cucharadas
        return f"{cucharadas} cucharadas"

    def recoger_vaso(self):
        return "Vaso recogido"

    def verificar_ingredientes(self, hay_vasos, hay_azucar, hay_cafe):
        if not hay_vasos:
            return "No hay vasos disponibles"
        if not hay_azucar:
            return "No hay azúcar disponible"
        if not hay_cafe:
            return "No hay café disponible"
        return "Ingredientes completos"
