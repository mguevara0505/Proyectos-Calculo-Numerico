import flet as ft


class ConvertidorNumeros:
    def __init__(self, page: ft.Page):
        self.page = page
        self.campo = None
        self.resultado = None

        self.setup_ui()

    def setup_ui(self):
        self.page.title = "Convertidor de números"
        self.page.bgcolor = "#98D8FF"
        self.page.fonts = {
            "Istok Web": "IstokWeb-Regular.ttf"
        }
        self.page.theme = ft.Theme(font_family="Istok Web")
        self.page.dark_theme = ft.Theme(font_family="Istok Web")
        self.page.window.width = 781
        self.page.window.height = 456

        self.page.add(self.create_container("Convertidor de números", 32))
        self.page.add(self.create_container("Elaborado por Mario Guevara", 20))
        self.page.add(self.create_container("Ingrese un número entero", 16))

        self.campo = ft.TextField(text_size=16, width=550,
                                  bgcolor="white", border_width="2", border_color="black", color="black")
        self.page.add(self.center_container(self.campo))

        self.page.add(self.create_button_row([
            ("Binario", self.convertir_binario),
            ("Octal", self.convertir_octal),
            ("Hexadecimal", self.convertir_hexadecimal),
            ("Terciario", self.conversion_final_terciario),
            ("Cuaternario", self.conversion_final_cuaternario)
        ]))

        self.resultado = ft.Text(color="black", size="20")
        self.page.add(self.center_container(self.resultado, top_padding=20))

        self.page.update()

    def create_container(self, text, size):
        return ft.Container(
            content=ft.Text(value=text, font_family="Istok Web", color="black", size=size),
            alignment=ft.alignment.center
        )

    def center_container(self, control, top_padding=0):
        return ft.Container(
            content=control,
            alignment=ft.alignment.center,
            padding=ft.padding.only(top=top_padding)
        )

    def create_button_row(self, buttons):
        row_items = [ft.ElevatedButton(label, bgcolor="blue", color="white", on_click=action) for label, action in buttons]
        return ft.Container(
            content=ft.Row(controls=row_items),
            padding=ft.padding.only(left=90)
        )

    def convertir_binario(self, e):
        self.convertir_numero(base=2)

    def convertir_octal(self, e):
        self.convertir_numero(base=8)

    def convertir_hexadecimal(self, e):
        self.convertir_numero(base=16)

    def convertir_numero(self, base):
        try:
            decimal = int(self.campo.value)
            if base == 2:
                resultado = bin(decimal)[2:]
            elif base == 8:
                resultado = oct(decimal)[2:]
            elif base == 16:
                resultado = hex(decimal)[2:]
            else:
                resultado = "Base no válida"

            self.resultado.value = resultado
            self.page.update()
        except ValueError:
            self.resultado.value = "Por favor, ingrese un número entero válido."
            self.page.update()

    def convertir_terciario(self, numero):
        if numero == 0:
            return "0"
        digitos = []
        while numero:
            digitos.append(int(numero % 3))
            numero //= 3
        digitos.reverse()
        return ''.join(map(str, digitos))

    def conversion_final_terciario(self, e):
        self.convertir_base(3)

    def convertir_cuaternario(self, numero):
        if numero == 0:
            return "0"
        digitos = []
        while numero:
            digitos.append(int(numero % 4))
            numero //= 4
        digitos.reverse()
        return ''.join(map(str, digitos))

    def conversion_final_cuaternario(self, e):
        self.convertir_base(4)

    def convertir_base(self, base):
        try:
            decimal = int(self.campo.value)
            if base == 3:
                resultado = self.convertir_terciario(decimal)
            elif base == 4:
                resultado = self.convertir_cuaternario(decimal)
            else:
                resultado = "Base no válida"

            self.resultado.value = resultado
            self.page.update()
        except ValueError:
            self.resultado.value = "Por favor, ingrese un número entero válido."
            self.page.update()


def main(page: ft.Page):
    ConvertidorNumeros(page)


ft.app(main)