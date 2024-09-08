import flet as ft

def main(page: ft.Page):

    def convertir_binario(e):
        try:
            decimal = int(campo.value)
            if decimal == 0:
                resultado.value = "0"
                page.update()
                return
            binario = ""
            while decimal > 0:
                residuo = decimal % 2
                binario = str(residuo) + binario
                decimal = decimal // 2
            resultado.value = "Número convertido a binario: " + binario
            page.update()
        except ValueError:
            resultado.value = "Por favor, ingrese un número entero válido."
            page.update()

    def convertir_octal(e):
        try:
            decimal = int(campo.value)
            octal = ""
            page.update()
            while decimal > 0:
                residuo = decimal % 8
                octal = str(residuo) + octal
                decimal = decimal // 8
            resultado.value = "Número convertido a octal: " + octal
            page.update()
        except ValueError:
            resultado.value = "Por favor, ingrese un número entero válido."
            page.update()

    def convertir_hexadecimal(e):
        try:
            decimal = int(campo.value)
            hexa = hex(decimal)[2:]
            resultado.value = "Número convertido a hexadecimal: " + hexa
            page.update()
        except ValueError:
            resultado.value = "Por favor, ingrese un número entero válido."
            page.update()

    def convertir_terciario(numero):
        if numero == 0:
            return "0"
        digitos = []
        while numero:
            digitos.append(int(numero % 3))
            numero //= 3
        digitos.reverse()
        return ''.join(map(str, digitos))

    def conversion_final_terciario(e):
        decimal = int(campo.value)
        numero_terciario = convertir_terciario(decimal)
        resultado.value = "Número convertido a terciario: " + numero_terciario
        page.update()

    def convertir_cuaternario(numero):
        if numero == 0:
            return "0"
        digitos = []
        while numero:
            digitos.append(int(numero % 4))
            numero //= 4
        digitos.reverse()
        return ''.join(map(str, digitos))

    def conversion_final_cuaternario(e):
        decimal = int(campo.value)
        numero_cuaternario = convertir_cuaternario(decimal)
        resultado.value = "Número convertido a cuaternario: " + numero_cuaternario
        page.update()

    page.title = "Convertidor de números"
    page.bgcolor = "#98D8FF"
    page.fonts = {
        "Istok Web": "IstokWeb-Regular.ttf"
    }
    page.theme = ft.Theme(font_family="Istok Web")
    page.dark_theme = ft.Theme(font_family="Istok Web")
    page.window.width = 781
    page.window.height = 456
    container = ft.Container(
        content = ft.Text(value="Convertidor de números", font_family="Istok Web", color="black", size="32"),
        alignment=ft.alignment.center
    )
    page.add(container)
    container2 = ft.Container(
        content=ft.Text(value="Elaborado por Mario Guevara", font_family="Istok Web", color="black", size="20"),
        alignment=ft.alignment.center
    )
    page.add(container2)
    container3 = ft.Container(
        content=ft.Text(value="Ingrese un número entero:", font_family="Istok Web", color="black", size="16"),
        alignment=ft.alignment.center,
    )
    page.add(container3)
    campo = ft.TextField(text_size=16, width=550, bgcolor="white", border_width="2", border_color="black", color="black")
    container4 = ft.Container(
        content=campo,
        alignment=ft.alignment.center
    )
    page.add(container4)
    binario = ft.ElevatedButton("Convertir a binario", bgcolor="blue", color="white", on_click=convertir_binario)
    octal = ft.ElevatedButton("Convertir a octal", bgcolor="blue", color="white", on_click=convertir_octal)
    hexadecimal = ft.ElevatedButton("Convertir a hexadecimal", bgcolor="blue", color="white", on_click=convertir_hexadecimal)
    row = ft.Row(controls=[binario, octal, hexadecimal])
    container5 = ft.Container(
        content=row,
        padding=ft.padding.only(left=90)
    )
    page.add(container5)
    terciario = ft.ElevatedButton("Convertir a terciario", bgcolor="blue", color="white", on_click = conversion_final_terciario)
    cuaternario = ft.ElevatedButton("Convertir a cuaternario", bgcolor="blue", color="white", on_click = conversion_final_cuaternario)
    row2 = ft.Row(controls=[terciario, cuaternario])
    container6 = ft.Container(
        content=row2,
        padding=ft.padding.only(left=170)
    )
    page.add(container6)
    resultado = ft.Text(color="black", size="20")
    container7 = ft.Container(
        content=resultado,
        padding=ft.padding.only(top=20)
    )
    page.add(container7)
    page.update()

ft.app(main)