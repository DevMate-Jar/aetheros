import tkinter as tk

recetas = {
    "Arroz con pollo": {
        "Arroz": 100,
        "Pollo": 50,
        "Agua": 350,
        "Pimiento": 20,
        "Precio": 6500,
        "Sal": "Al gusto"
        
    },
    "Pescado frito": {
        "Pescado": 150,
        "Harina": 30,
        "Aceite": 50,
        "Limón": 10,
        "Precio": 11200,
        "Sal": "Al gusto"
    },
    "Sushi": {
        "Arroz para sushi": 80,
        "Alga": 1,
        "Salmón": 40,
        "Pepino": 15,
        "Vinagre de arroz": 10,
        "Precio": 15000,
        "Sal": "Al gusto"
    },
    "Fideos con bolognesa": {
        "Fideos": 100,
        "Carne picada": 80,
        "Salsa de tomate": 100,
        "Cebolla": 30,
        "Aceite de oliva": 10,
        "Precio": 9300,
        "Sal": "Al gusto"
    }
}

def calcular_receta():
    try:
        plato = lista_platos.get()
        personas_extra = int(entry_personas.get())
        porcentaje_extra = float(entry_porcentaje.get())
        if personas_extra < 0 or porcentaje_extra < 0:
            resultado.set("No se permiten valores negativos! Intenta de vuelta :D")
            return
    except ValueError:
        resultado.set("Ingresa un valor valido!")
        return

    personas_iniciales = 1
    total_personas = personas_iniciales + personas_extra
    factor = (total_personas / personas_iniciales) * (1 + porcentaje_extra / 100)

    receta = recetas[plato]
    texto = f"Receta de {plato} para {total_personas} personas con {porcentaje_extra}% extra:\n\n"
    precio_base = receta.get("Precio", 0)
    precio_final = round(precio_base * factor, 2)
    for ingrediente, cantidad in receta.items():
        if ingrediente == "Precio":
            continue
        if isinstance(cantidad, (int, float)):
            texto += f"{ingrediente}: {round(cantidad * factor, 2)}g\n"
        else:
            texto += f"{ingrediente}: {cantidad}\n"
    texto += f"\nPrecio final estimado: ${precio_final}"
    resultado.set(texto)





ventana = tk.Tk()
ventana.title("Calculadora de Receta")
ventana.geometry("450x500")


tk.Label(ventana, text="Elige un plato:").pack()
lista_platos = tk.StringVar(ventana)
lista_platos.set(list(recetas.keys())[0]) 
tk.OptionMenu(ventana, lista_platos, *recetas.keys()).pack()


tk.Label(ventana, text="Personas adicionales:").pack()
entry_personas = tk.Entry(ventana)
entry_personas.pack()

tk.Label(ventana, text="Porcentaje extra por persona (%):").pack()
entry_porcentaje = tk.Entry(ventana)
entry_porcentaje.pack()


tk.Button(ventana, text="Calcular receta", command=calcular_receta).pack(pady=10)


resultado = tk.StringVar()
tk.Label(ventana, textvariable=resultado, justify="left").pack(pady=10)

boton_limpiar = tk.Button(ventana, text="Limpiar", command=lambda: resultado.set(""))
boton_limpiar.pack(pady=5)


texto_base = "Recetas disponibles:\n\n"
for nombre, receta in recetas.items():
    texto_base += f"➡ {nombre}\n"
resultado.set(texto_base)

ventana.mainloop()
