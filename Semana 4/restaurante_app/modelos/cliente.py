# modelos/cliente.py
# Clase que representa a un cliente del restaurante

class Cliente:
    def __init__(self, id, nombre, telefono=None):
        """id: identificador único
        nombre: nombre completo del cliente
        telefono: contacto opcional
        pedidos: lista donde se almacenan pedidos realizados por el cliente
        """
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.pedidos = []  # cada pedido puede ser un dict con productos y total

    def __str__(self):
        telefono = self.telefono if self.telefono else 'N/A'
        return f"Cliente {self.id}: {self.nombre} - {telefono}"

    def agregar_pedido(self, pedido):
        """Agrega un pedido (dict) a la lista de pedidos del cliente."""
        self.pedidos.append(pedido)

    def listar_pedidos(self):
        return list(self.pedidos)
