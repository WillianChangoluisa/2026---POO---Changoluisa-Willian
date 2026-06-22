# modelos/cliente.py
# Clase que representa a un cliente del restaurante

class Cliente:
    """Representa un cliente que realiza pedidos en el restaurante."""
    
    def __init__(self, id_cliente, nombre, telefono=None):
        """
        Inicializa un cliente con:
        - id_cliente: identificador unico del cliente
        - nombre: nombre completo del cliente
        - telefono: numero de contacto (opcional)
        """
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.telefono = telefono
        self.historial_pedidos = []  # lista para almacenar los pedidos del cliente
    
    def __str__(self):
        """Retorna una representacion legible del cliente."""
        telefono_str = self.telefono if self.telefono else "N/A"
        return f"Cliente {self.id_cliente}: {self.nombre} - Tel: {telefono_str}"
    
    def agregar_pedido(self, pedido):
        """Agrega un pedido al historial del cliente."""
        self.historial_pedidos.append(pedido)
    
    def obtener_historial(self):
        """Retorna el historial de pedidos del cliente."""
        return self.historial_pedidos
    
    def obtener_total_gastado(self):
        """Calcula el total gastado por el cliente en todos sus pedidos."""
        total = 0
        for pedido in self.historial_pedidos:
            total += pedido.get('total', 0)
        return total
