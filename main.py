import argparse



def main():
    parser = argparse.ArgumentParser(description="Invoke a module based on user input.")
    parser.add_argument("module_number", metavar='M', type=int, choices=range(3, 12), help="Module number (3 to 11)")

    args = parser.parse_args()

    if args.module_number == 3:
        print("Стартуем модуль 3.")
        import module3 as module3
    elif args.module_number == 4:
        print("Стартуем модуль 4.")
    elif args.module_number == 5:
        print("Пока не готово.. жарится!")
    elif args.module_number == 6:
        print("Пока не готово.. варится!")
    elif args.module_number == 7:
        print("Пока не готово.. парится!")
    elif args.module_number == 8:
        print("Пока не готово.. готовится!")
    elif args.module_number == 9:
        print("Пока не готово.. пилится!")
    elif args.module_number == 10:
        print("Пока не готово.. осваиваится!")
    elif args.module_number == 11:
        print("Пока не готово.. обустраиваится!")
    else:
        print("Неверный номер модуля. Следует выбрать между 3 до 11.")

if __name__ == "__main__":
    main()
