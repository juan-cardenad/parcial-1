
from pasajero import Pasajero
from transportepublico import Vehiculotransportepublico, BusetaInterveredal, BusetaIntermunicipal, MotoTaxi
from trayecto import Trayecto

lista_vehiculos : list[Vehiculotransportepublico] = []

print("holaaa!")
def registrar_transporte() :
    agregar_otro_vehiculo = True
    contador_vehiculos = 0
    while (agregar_otro_vehiculo == True) :
        while (True) :
            try:
                placa = input(f"Ingrese la placa del vehiculo {contador_vehiculos + 1}: ").upper()
                if (placa.strip() == ""):
                    raise ValueError(f"la placa del vehiculo {contador_vehiculos + 1}  no puede estar vacía")
                if not placa.isalnum():
                    raise ValueError(f"La placa del vehículo {contador_vehiculos + 1} solo puede contener letras y números (no usar caracteres especiales).")
                if len(placa) != 6 :
                    raise ValueError(f"La placa del vehículo {contador_vehiculos + 1} debe tener exactamente 6 caracteres combinando letras y numeros.")
                if any(v.placa.upper() == placa for v in lista_vehiculos):
                    raise ValueError (f"Error: la placa {placa} ya está registrada en el sistema ")
                else:
                    break
            except ValueError as error:
                print(error)

        while (True) :
         print("Seleccione el tipo de vehículo:")
         print("1. Buseta interveredal")
         print("2. Buseta intermunicipal")
         print("3. Mototaxi")
         opcion = input("Ingrese una opción : ")

         if opcion == "1" :
            vehiculo = BusetaInterveredal(placa)
            break
         elif opcion == "2" :
            vehiculo = BusetaIntermunicipal(placa)
            break
         elif opcion == "3" :
            vehiculo = MotoTaxi(placa)
            break
         else:
            print("Error: elija una opcion entre 1 y 3")

        contador_vehiculos += 1
        lista_vehiculos.append(vehiculo)
        print(f" Vehículo {contador_vehiculos } con placa {placa} registrado correctamente como {vehiculo.tipo}")


        ingresar_otro_vehiculo = input("¿Desea ingresar otro vehiculo? (s/n): ").lower()
        if ingresar_otro_vehiculo == "n" :
          agregar_otro_vehiculo = False


def definir_rutas():
    if not lista_vehiculos:
        print("No hay vehículos registrados. Registre al menos uno para definir rutas.")
        return

    agregar_ruta_vehiculo = True
    while (agregar_ruta_vehiculo == True) :
        print("\nVehículos registrados:")
        for i, v in enumerate(lista_vehiculos):
            print(f"{i + 1}. {v.tipo} - Placa: {v.placa}")

        while True:
            try:
                opcion = int(input("Ingrese el numero del vehículo al que desea asignarle una ruta: "))
                if opcion < 1 or opcion > len(lista_vehiculos):
                    raise ValueError("Numero de vehículo invalido.")
                vehiculo_seleccionado = lista_vehiculos[opcion - 1]
                break
            except ValueError as error:
                print(error)

        agregar_otra_ruta_mismo_vehiculo = True
        while (agregar_otra_ruta_mismo_vehiculo == True ):
            while True:
                try:
                    origen = input(f"Ingrese el punto de origen para el vehiculo {opcion}: ").strip()
                    if origen.strip() == "":
                        raise ValueError(f"El origen del vehiculo {opcion } no puede estar vacío")
                    if origen.isdigit():
                        raise ValueError("el origen no puede ser un numero")
                    else:
                        break
                except ValueError as error:
                    print(error)

            while True:
                try:
                    destino = input(f"Ingrese el destino del vehiculo {opcion }: ")
                    if destino.strip() == "":
                        raise ValueError(f"El destino del vehiculo {opcion} no puede estar vacío")
                    if destino.isdigit():
                        raise ValueError("el destino no puede ser un numero")
                    else:
                        break
                except ValueError as error:
                    print(error)

            while True:
                try:
                    try:
                        valor_pasaje = float(input(f"Ingrese el valor del pasaje para esta ruta del vehiculo {opcion }: :"))
                    except ValueError:
                        raise ValueError(f"El valor del pasaje no es un numero")
                    if valor_pasaje <= 0:
                        raise ValueError(f"El valor del pasaje no puede ser menor o igual a 0")
                    else:
                        break
                except ValueError as error:
                    print(error)


            trayecto = Trayecto(origen, destino, valor_pasaje)
            vehiculo_seleccionado.trayecto.append(trayecto)
            print(f"Ruta asignada a {vehiculo_seleccionado.tipo} {vehiculo_seleccionado.placa}: {origen} -> {destino}, Pasaje: ${valor_pasaje}")

            otra_ruta = input("¿Desea agregar otra ruta a este mismo vehiculo? (s/n): ").lower()
            if otra_ruta == "n":
             agregar_otra_ruta_mismo_vehiculo = False

        ingresar_otra_ruta = input("¿Desea ingresar rutas a otros vehiculo? (s/n): ").lower()
        if ingresar_otra_ruta == "n":
            agregar_ruta_vehiculo = False

def registrar_pasajeros():
    if not lista_vehiculos:
        print("No hay vehiculos registrados. Primero registre vehiculos y rutas.")
        return

    continuar = True
    while continuar:
        print("\nVehiculos registrados:")
        for i, v in enumerate(lista_vehiculos):
            print(f"{i + 1}. {v.tipo} - Placa: {v.placa}")

        try:
            opcion = int(input("Seleccione el vehiculo para registrar pasajeros: "))
            if opcion < 1 or opcion > len(lista_vehiculos):
                raise ValueError("numero de vehiculo invalido.")
            vehiculo_seleccionado = lista_vehiculos[opcion - 1]
        except ValueError as error:
            print(error)
            continue

        if not vehiculo_seleccionado.trayecto:
            print("Este vehiculo no tiene rutas asignadas. Primero defina rutas.")
            continue

        registrar_mas_pasajeros = True
        while registrar_mas_pasajeros:
            print("\nRutas del vehiculo seleccionado:")
            for i, t in enumerate(vehiculo_seleccionado.trayecto):
                print(f"{i + 1}. {t.origen} -> {t.destino}, Valor pasaje: ${t.valor_pasaje}")
            try:
                trayecto_opcion = int(input("Seleccione el trayecto al que desea registrar pasajeros: "))
                if trayecto_opcion < 1 or trayecto_opcion > len(vehiculo_seleccionado.trayecto):
                    raise ValueError("numero de trayecto invalido.")
                trayecto_seleccionado = vehiculo_seleccionado.trayecto[trayecto_opcion - 1]
            except ValueError as error:
                print(error)
                continue

            while True:
                try:
                    edad = int(input("Ingrese la edad del pasajero: "))
                    if edad <= 0:
                        raise ValueError("La edad del pasajero no puede ser un numero negativo o cero.")
                    break
                except ValueError as error:
                    print(error)

            while True:
                try:
                    genero = input("Ingrese el genero del pasajero (M/F): ").strip().upper()
                    if genero not in ["M", "F"]:
                        raise ValueError("El genero debe ser 'M' o 'F'.")
                    break
                except ValueError as error:
                    print(error)

            pasajero = Pasajero(edad, genero)
            trayecto_seleccionado.registrar_pasajero(pasajero)
            print("Pasajero registrado correctamente.")

            otra_ruta = input("¿Desea registrar pasajeros en otro trayecto del mismo vehiculo? (s/n): ").lower()
            if otra_ruta == "n":
                registrar_mas_pasajeros = False
                continuar = False



def valor_total_recaudado():
    total = 0
    for vehiculo in lista_vehiculos:
        for trayecto in vehiculo.trayecto:
            total += trayecto.valor_pasaje * len(trayecto.pasajeros)
    print(f"El valor total recaudado por pasajes en toda la empresa es: ${total}")

def buseta_intermunicipal_mas_recaudacion():
    mayor_recaudacion = None
    buseta_ganadora = None

    for vehiculo in lista_vehiculos:
        if isinstance(vehiculo, BusetaIntermunicipal):
            total_vehiculo = sum(
                trayecto.valor_pasaje * len(trayecto.pasajeros)
                for trayecto in vehiculo.trayecto
            )
            if mayor_recaudacion is None or total_vehiculo > mayor_recaudacion:
                mayor_recaudacion = total_vehiculo
                buseta_ganadora = vehiculo

    if buseta_ganadora is None:
        print("No hay busetas intermunicipales registradas.")
    elif mayor_recaudacion == 0:
        print("Las busetas intermunicipales no tienen pasajeros registrados aún.")
    else:
        print(f"La buseta intermunicipal que más dinero recaudó es la placa {buseta_ganadora.placa} con ${mayor_recaudacion}")


def ruta_menos_recaudacion():
    menor_recaudacion = None
    ruta_perdedora = None
    vehiculo_ruta = None

    for vehiculo in lista_vehiculos:
        for trayecto in vehiculo.trayecto:
            total_trayecto = trayecto.valor_pasaje * len(trayecto.pasajeros)
            if menor_recaudacion is None or total_trayecto < menor_recaudacion:
                menor_recaudacion = total_trayecto
                ruta_perdedora = trayecto
                vehiculo_ruta = vehiculo

    if ruta_perdedora:
        print(f"La ruta que menos dinero recaudo es {ruta_perdedora.origen} -> {ruta_perdedora.destino} del vehiculo {vehiculo_ruta.tipo} placa {vehiculo_ruta.placa} con ${menor_recaudacion}")
    else:
        print("No hay rutas registradas.")

def comparar_recaudacion_tipos():
    total_interveredal = 0
    total_intermunicipal = 0

    for vehiculo in lista_vehiculos:
        total_vehiculo = sum(
            trayecto.valor_pasaje * len(trayecto.pasajeros)
            for trayecto in vehiculo.trayecto
        )
        if isinstance(vehiculo, BusetaInterveredal):
            total_interveredal += total_vehiculo
        elif isinstance(vehiculo, BusetaIntermunicipal):
            total_intermunicipal += total_vehiculo

    print(f"Total recaudado por busetas interveredales: ${total_interveredal}")
    print(f"Total recaudado por busetas intermunicipales: ${total_intermunicipal}")

    if total_interveredal == 0 and total_intermunicipal == 0:
        print("No hay pasajeros registrados en ninguna de las busetas.")
    elif total_interveredal > total_intermunicipal:
        print("Los transportes interveredales dejan más dinero.")
    elif total_interveredal < total_intermunicipal:
        print("Los transportes intermunicipales dejan más dinero.")
    else:
        print("Ambos tipos de transporte dejan la misma cantidad de dinero.")


def calcular_descuentos():
    total_descuentos = 0
    total_descuentos_femenino = 0

    for vehiculo in lista_vehiculos:
        for trayecto in vehiculo.trayecto:
            for pasajero in trayecto.pasajeros:
                if pasajero.edad < 18:
                    descuento = trayecto.valor_pasaje * 0.20
                    total_descuentos += descuento
                    if pasajero.genero == "F":
                        total_descuentos_femenino += descuento

    print(f"Dinero total de descuentos otorgados: ${total_descuentos}")
    print(f"Dinero total de descuentos otorgados a niñas: ${total_descuentos_femenino}")


def mostrar_menu():
    opcion = 0
    while opcion != 9:
        print("\n--- MENU PRINCIPAL ---")
        print("1. Registrar transporte")
        print("2. Definir rutas")
        print("3. Registrar pasajeros")
        print("4. Ver valor total recaudado")
        print("5. Ver buseta intermunicipal que mas recaudo")
        print("6. Ver ruta que menos recaudo")
        print("7. Comparar recaudacion entre interveredales e intermunicipales")
        print("8. Ver descuentos otorgados")
        print("9. Salir")

        try:
            opcion = int(input("Ingrese una opcion: "))
            if opcion < 1 or opcion > 9:
                raise ValueError("Opción fuera de rango (1-9).")
        except ValueError as error:
            print(error)
            continue

        if opcion == 1:
            registrar_transporte()
        elif opcion == 2:
            definir_rutas()
        elif opcion == 3:
            registrar_pasajeros()
        elif opcion == 4:
            valor_total_recaudado()
        elif opcion == 5:
            buseta_intermunicipal_mas_recaudacion()
        elif opcion == 6:
            ruta_menos_recaudacion()
        elif opcion == 7:
            comparar_recaudacion_tipos()
        elif opcion == 8:
            calcular_descuentos()
        elif opcion == 9:
            print("Saliendo.. .")


def main():
    mostrar_menu()



if __name__ == "__main__":
    main()

























