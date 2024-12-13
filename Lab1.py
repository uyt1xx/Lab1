def calculator():
    print("Простой калькулятор")
    print("Введите операцию в формате: число1 операция число2")
    print("Примеры: 2 + 2, 5 * 3, 10 / 2")
    print("Введите 'exit' для выхода.")

    while True:
        user_input = input("Введите выражение: ").strip()

        if user_input.lower() == 'exit':
            print("Выход из калькулятора. До свидания!")
            break

        try:
            # Используем eval для вычисления выражения
            result = eval(user_input)
            print(f"Результат: {result}")
        except Exception as e:
            print(f"Ошибка: {e}. Проверьте корректность ввода.")

if __name__ == "__main__":
    calculator()