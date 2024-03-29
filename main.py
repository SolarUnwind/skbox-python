import argparse



def main():
    parser = argparse.ArgumentParser(description="Invoke a module based on user input.")
    parser.add_argument("module_number", metavar='M', type=int, choices=range(3, 14), help="Module number (3 to 13)")

    args = parser.parse_args()

    if args.module_number == 3:
        print("Стартуем модуль 3!\n")
        import module3 as module3
    elif args.module_number == 4:
        print("Стартуем модуль 4!\n")
        import module4 as module4
    elif args.module_number == 5:
        print("Стартуем модуль 5!\n")
        import module5 as module5
    elif args.module_number == 6:
        print("Стартуем модуль 6!\n")
        import module6 as module6
    elif args.module_number == 7:
        print("Стартуем модуль 7!\n")
        import module7 as module7
    elif args.module_number == 8:
        print("Стартуем модуль 8!\n")
        import module8 as module8
    elif args.module_number == 9:
        print("Стартуем модуль 9!\n")
        import module9 as module9
    elif args.module_number == 10:
        print("Стартуем модуль 10!\n")
        import module10 as module10
    elif args.module_number == 11:
        print("Стартуем модуль 11!\n")
        import module11 as module11
    elif args.module_number == 12:
        print("Стартуем модуль 12!\n")
        import module12 as module12
    elif args.module_number == 13:
        print("Стартуем модуль 13!\n")
        import module13 as module13
    else:
        print("Неверный номер модуля. Следует выбрать между 3 до 13.")

if __name__ == "__main__":
    main()
