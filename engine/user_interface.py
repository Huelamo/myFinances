import sys

from engine.accounting_book import AccountingBook
from enums.engine_enums import RegisterHeaders, DateElements
class UserInterface():

    def __init__(self):
        self._user = self._user_login()
        self._active_book = AccountingBook(user=self._user, load_data=True)
        self._menu()

    @staticmethod
    def _user_login():
        return input("Introduce tu nombre de usuario: ").strip()

    def _display_data(self):
        category = self._active_book._ask_category()
        filters = {RegisterHeaders.CATEGORY: category}

        year = input("Indica el año correspondiente en el que se produjo la transacción que deseas consultar. "
                     "Si quieres ver todo el histórico, pulsa la tecla Enter: ")
        if not year:
            self._active_book._display_data(filters=filters)
        else:
            filters.update({DateElements.YEAR: int(year)})
            month = input("Indica el número del mes correspondiente en el que se produjo la transacción que deseas "
                          "consultar. Si quieres consultar el año completo, pulsa la tecla Enter: ")
            if not month:
                self._active_book._display_data(filters=filters)
            else:
                day = input("Indica el día correspondiente en el que se produjo la transacción que deseas "
                            "consultar. Si quieres consultar el mes completo, pulsa la tecla Enter: ")
                if not day:
                    filters.update({DateElements.MONTH: int(month)})
                else:
                    filters.update({DateElements.MONTH: int(month), DateElements.DAY: int(day)})
                self._active_book._display_data(filters=filters)

    def _delete_user_data(self):

        print(f"Se procederá a eliminar los datos del usuario {self._user} y se cerrará la sesión. "
              f"¿Estás seguro/a de querer continuar?\n")
        print("1. No, he cambiado de idea.")
        print(f"2. Sí, quiero eliminar los datos del usuario {self._user}")

        user_confirmation = input("\nIntroduce tu respuesta: ")

        match user_confirmation:
            case "1":
                print(f"\nOperación cancelada. No se eliminaron los datos correspondientes al usuario {self._user}\n")
            case "2":
                self._active_book._delete_user_data(self._user)
                return
            case _:
                print("Respuesta no válida. Por favor, inténtalo de nuevo.\n")
                self._delete_user_data()

    def _menu(self):
        while True:
            print("\n--- Gestor de Gastos ---")
            print("1. Añadir nuevo registro")
            print("2. Ver registros")
            print("3. Editar registro")  #TODO
            print("4. Añadir categoría de gasto")
            print("5. Añadir categoría de ingreso")  #TODO
            print("6. Editar categoría de gasto")  #TODO
            print("7. Editar categoría de ingreso")  #TODO
            print("8. Eliminar datos de usuario")
            print("9. Restaurar datos de usuario")  #TODO
            print("10. Salir")

            opcion = input("\nSelecciona una opción: ").strip()

            match opcion:
                case "1":
                    self._active_book._new_register()
                    AccountingBook._save_to_file(self._active_book._data, self._active_book._data_file)
                case "2":
                    self._display_data()
                case "3":
                    raise NotImplementedError("Lamentablemente, esta opción todavía no está implementada. Elige otra.")
                case "4":
                    self._active_book._create_expense_category()
                case "5":
                    raise NotImplementedError("Lamentablemente, esta opción todavía no está implementada. Elige otra.")
                case "6":
                    raise NotImplementedError("Lamentablemente, esta opción todavía no está implementada. Elige otra.")
                case "7":
                    raise NotImplementedError("Lamentablemente, esta opción todavía no está implementada. Elige otra.")
                case "8":
                    self._delete_user_data()
                    return
                case "9":
                    raise NotImplementedError("Lamentablemente, esta opción todavía no está implementada. Elige otra.")
                case "10":
                    print("¡Hasta luego!")
                    return
                case _:
                    print("Opción no válida. Intenta nuevamente.")
                    self._menu()