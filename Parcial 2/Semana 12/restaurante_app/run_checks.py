import sys
from pprint import pprint
sys.path.insert(0, r'C:\Users\William.Changoluisa\PycharmProjects\2026---POO---Changoluisa-Willian\Parcial 2\Semana 12')

from restaurante_app.servicios.restaurante import Restaurante


def main():
    r = Restaurante()
    print('Productos (codigo:stock):', [f"{p.codigo}:{p.stock}" for p in r.listar_productos()])
    print('Usuarios:', [u.identificacion for u in r.listar_usuarios()])
    print('Ventas iniciales:', [v.to_dict() for v in r.listar_ventas()])

    p = r.buscar_producto('P1')
    u = r.buscar_usuario('U1')
    print('Buscar P1 ->', p.mostrar_informacion() if p else None)
    print('Buscar U1 ->', u.mostrar_informacion() if u else None)

    print('Ventas por U1 (antes):')
    pprint([v.to_dict() for v in r.consultar_ventas_por_usuario('U1')])

    print('Intentando vender 1 unidad de P1 a U1...')
    ok = r.vender_producto('P1', 'U1', 1)
    print('Venta realizada?', ok)

    print('Productos (después):', [f"{p.codigo}:{p.stock}" for p in r.listar_productos()])
    print('Ventas (después):')
    pprint([v.to_dict() for v in r.listar_ventas()])

    print('Indices: productos=', sorted(list(r._producto_por_codigo.keys())))
    print('Indices: usuarios=', sorted(list(r._usuario_por_id.keys())))
    print('Indices: ventas_por_usuario for U1 =')
    pprint([v.to_dict() for v in r._ventas_por_usuario.get('U1', [])])


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print('ERROR DURANTE CHECKS:', e)
        raise
