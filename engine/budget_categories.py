import json
from datetime import datetime
from pathlib import Path

from enums.engine_enums import RegisterHeaders


# Archivo JSON donde se almacenarán los datos
DATA_PATH = Path(__file__).resolve().parent.parent / "data"
DATA_PATH.mkdir(exist_ok=True)


class AccountingBook():

    def __init__(self):
        self._user = AccountingBook._user_login()
        self._data_file = f'{self._user}.json'
        self._data = self._load_data()
        self._menu()

    @staticmethod
    def _user_login():
        return input("Introduce tu nombre de usuario: ").strip()

    def _load_data(self):
        try:
            with open(f'{DATA_PATH}/{self._data_file}', "r") as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"No existen registros para el usuario {self._user}. ¿Quieres crear un nuevo libro de cuentas?\n")
            new_book = input("Escribe 1 en caso afirmativo. De lo contrario escribe 0: ")
            if new_book:
                return []  # Si el archivo no existe, devuelve una lista vacía
            print(f"¿Quieres leer el registro de un usuario distinto a {self._user}?")
            new_user = input("Escribe 1 en caso afirmativo. De lo contrario escribe 0: ")
            if new_user:
                self._user_login()
            else:
                print("Entonces, ¡hasta luego!")

    def _save_data(self):
        with open(f'{DATA_PATH}/{self._data_file}', "w") as file:
            json.dump(self._data, file, indent=4)

    @staticmethod
    def _ask_date() -> datetime:
        date = input("Fecha (YYYY-MM-DD, presiona Enter para hoy): ").strip()
        if not date:  # Si el usuario deja vacío, toma la fecha actual
            date = datetime.now().strftime("%Y-%m-%d")
        try:
            date = datetime.strptime(date, "%Y-%m-%d").strftime("%Y-%m-%d")
        except ValueError:
            print("Formato de fecha inválido. Intenta nuevamente.")
            AccountingBook._ask_date()
        return date

    @staticmethod
    def _ask_category() -> str:
        category = input("Categoría: ").strip()
        if not category:
            raise ValueError("La categoría no puede estar vacía. Intenta nuevamente.")
            AccountingBook._ask_category()
        else:
            return category

    @staticmethod
    def _ask_amount() -> float:
        amount = input("Importe (utiliza el punto como separador decimal): ").strip()
        try:
            amount = float(amount)
        except ValueError:
            print("Formato de importe inválido. Intenta nuevamente.")
            AccountingBook._ask_amount()
        return amount

    def _new_register(self):
        print("Introduce los datos de la transacción:")

        date = AccountingBook._ask_date()
        category = AccountingBook._ask_category()
        amount = AccountingBook._ask_amount()

        # Crear la transacción
        transaccion = {
            RegisterHeaders.DATE.value: date,
            RegisterHeaders.CATEGORY.value: category,
            RegisterHeaders.AMOUNT.value: amount
        }

        self._data.append(transaccion)
        self._save_data()

        print("¡Transacción añadida con éxito!")
        print(transaccion)

    def _display_data(self):
        if not self._data:
            print("No hay transacciones registradas.")
        else:
            print("\n--- Transacciones ---")
            for i, t in enumerate(self._data, start=1):
                print(f"{i}. {RegisterHeaders.DATE.value}: {t[RegisterHeaders.DATE.value]}, "
                      f"{RegisterHeaders.CATEGORY.value}: {t[RegisterHeaders.CATEGORY.value]}, "
                      f"{RegisterHeaders.AMOUNT.value}: {t[RegisterHeaders.AMOUNT.value]}")

    # Menú principal
    def _menu(self):
        while True:
            print("\n--- Gestor de Gastos ---")
            print("1. Añadir nuevo registro")
            print("2. Ver registros")
            print("3. Editar registro")  #TODO
            print("4. Añadir categoría de gasto")  #TODO
            print("5. Añadir categoría de ingreso")  #TODO
            print("6. Editar categoría de gasto")  #TODO
            print("7. Editar categoría de ingreso")  #TODO
            print("8. Salir")

            opcion = input("Selecciona una opción: ").strip()

            if opcion == "1":
                self._new_register()
            elif opcion == "2":
                self._display_data()
            elif opcion == "3":
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida. Intenta nuevamente.")


if __name__ == "__main__":
    AccountingBook()