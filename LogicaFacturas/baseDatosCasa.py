import sqlite3 as dbapi

datos = (("77422183C", "Pepe", 30, "Hombre", "Sí"),
         ("83875923C", "Ana", 25, "Mujer", "Sí"),
         ("998776412C", "Roque", 40, "Hombre", "No"),
         ("66733289C", "Juan", 35, "Hombre", "No"),
         ("12345678A", "María", 28, "Mujer", "Sí"))

bbdd = dbapi.connect ("baseDatosCasa.dat")
c =bbdd.cursor()

try:
    c.execute("""create table listaPersonas (dni text,
                              nombre text,
                              edad text,
                              genero text,
                              fallecido text)
                             """)
except dbapi.DatabaseError as e:
    print ("Erro creando a táboa listaTelefonos: " + e)

try:
    for datos2 in datos:
        c.execute ("""insert into listaPersonas
                  values(?, ?, ?, ?, ?)""", datos2)# va linea por linea en la agenda y guarda cada linea en la variable datos. Luego hace el insert en la tabla con los datos de dicha variable.
    bbdd.commit()
except dbapi.DatabaseError as e:
    print ("Erro o insertar usuarios: "+ e)

c.close()
bbdd.close()