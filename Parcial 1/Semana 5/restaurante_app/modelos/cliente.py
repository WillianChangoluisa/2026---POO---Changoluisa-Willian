# Clase Cliente: representa una persona registrada en el sistema del restaurante

class Cliente:
    """Representa un cliente registrado en el sistema del restaurante."""
    
    def __init__(self, nombre_cliente: str, correo_electronico: str, numero_telefono: str, es_cliente_frecuente: bool):
        """
        Inicializa un cliente con sus datos personales.
        
        Args:
            nombre_cliente (str): Nombre completo del cliente
            correo_electronico (str): Correo electrónico del cliente
            numero_telefono (str): Número de teléfono del cliente
            es_cliente_frecuente (bool): Indica si es cliente frecuente para descuentos
        """
        self.nombre_cliente: str = nombre_cliente
        self.correo_electronico: str = correo_electronico
        self.numero_telefono: str = numero_telefono
        self.es_cliente_frecuente: bool = es_cliente_frecuente
    
    def obtener_estado_cliente(self) -> str:
        """Retorna el estado del cliente: Regular o Frecuente."""
        return "Cliente Frecuente" if self.es_cliente_frecuente else "Cliente Regular"
    
    def actualizar_estado_frecuente(self, estado_nuevo: bool) -> None:
        """Actualiza el estado de cliente frecuente."""
        self.es_cliente_frecuente = estado_nuevo
        estado = "promovido a cliente frecuente" if estado_nuevo else "actualizado a cliente regular"
        print(f"{self.nombre_cliente} ha sido {estado}")
    
    def __str__(self) -> str:
        """Retorna una representación en texto del cliente."""
        return (
            f"Cliente: {self.nombre_cliente}\n"
            f"  Estado: {self.obtener_estado_cliente()}\n"
            f"  Correo: {self.correo_electronico}\n"
            f"  Teléfono: {self.numero_telefono}"
        )
