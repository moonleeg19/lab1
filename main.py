from auth import login

def main():
    print("Привет, Git!")
    if login("admin", "1234"):
        print("Успешный вход!")
    else:
        print("Ошибка доступа")

if __name__ == "__main__":
    main()