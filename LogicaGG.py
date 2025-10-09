multiplicadores = {
    "Moto": 1.5,
    "Auto": 2.0, 
    "Camioneta": 3.0
}

estacionamiento = {
    "A1": {"tipo": "Auto", "patente": "ABC123", "horas": 3, "tarifa_base": 200, "pagado": False},
    "A2": {"tipo": "Moto", "patente": "XYZ789", "horas": 2, "tarifa_base": 200, "pagado": True},
    "B1": {"tipo": "Camioneta", "patente": "DEF456", "horas": 5, "tarifa_base": 200, "pagado": False},
    "B2": {"tipo": None, "patente": None, "horas": 0, "tarifa_base": 0, "pagado": False}
}

while True:
    print("\n--- Estado del Estacionamiento ---")
    for lugar, datos in estacionamiento.items():
        tipo = datos["tipo"]
        if tipo is not None:
            multiplicador = multiplicadores.get(tipo, 1.0)
            total = datos["horas"] * datos["tarifa_base"] * multiplicador
            estado_pago = "Pagado" if datos["pagado"] else "Debe pagar"
            print(f"Lugar: {lugar}")
            print(f"  Tipo: {tipo}")
            print(f"  Patente: {datos['patente']}")
            print(f"  Horas: {datos['horas']}")
            print(f"  Total a pagar: ${total}")
            print(f"  Estado: {estado_pago}\n")
        else:
            print(f"Lugar: {lugar} está libre.\n")
    
    opcion = input("¿Desea actualizar el estado de algún lugar? (s/n): ").strip().lower()
    if opcion != "s":
        print("Saliendo del sistema.")
        break

    lugar_mod = input("Ingrese el lugar a modificar (ej: A1, B2): ").strip().upper()
    if lugar_mod in estacionamiento:
        if estacionamiento[lugar_mod]["tipo"] is None:
            print("Ese lugar está libre. Ingrese los datos para ocuparlo.")
            tipo = input("Tipo (Moto/Auto/Camioneta): ").strip().capitalize()
            patente = input("Patente: ").strip().upper()
            horas = int(input("Horas: "))
            pagado = input("¿Pagó? (s/n): ").strip().lower() == "s"
            estacionamiento[lugar_mod] = {
                "tipo": tipo,
                "patente": patente,
                "horas": horas,
                "tarifa_base": 200,
                "pagado": pagado
            }
        else:
            print("Ese lugar está ocupado. Puede marcarlo como pagado o liberarlo.")
            accion = input("¿Marcar como pagado (p) o liberar (l)?: ").strip().lower()
            if accion == "p":
                estacionamiento[lugar_mod]["pagado"] = True
            elif accion == "l":
                estacionamiento[lugar_mod] = {
                    "tipo": None,
                    "patente": None,
                    "horas": 0,
                    "tarifa_base": 0,
                    "pagado": False
                }
            else:
                print("Acción no reconocida.")
    else:
        print("Lugar no válido.")