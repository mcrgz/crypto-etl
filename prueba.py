from datetime import datetime, timedelta

fecha_agregar = str((datetime.today()).date())

print(fecha_agregar)
NombreTabla = 'CoinsHistory'
where = ','.join([f":id{i}" for i in range(len([fecha_agregar]))])
campo = "CAST(fecha as date)"
query = f"DELETE FROM {NombreTabla} WHERE {campo} = ({where})"
params = {f"id{i}": id_val for i, id_val in enumerate(fecha_agregar)}

print(query)
print(params)
