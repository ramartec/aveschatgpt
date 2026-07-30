from dao.orden_dao import OrdenDAO


ordenes = OrdenDAO.listar()

print()

print("ÓRDENES EN LA BASE DE DATOS")

print("--------------------------")

for orden in ordenes:

    print(
        orden.id_orden,
        orden.nombre
    )

print()

print("Total:", len(ordenes))