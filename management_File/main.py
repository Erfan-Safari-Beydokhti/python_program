def main():
    while True:
        print("\n 📃Menu:")
        print("1. Add Customer")
        print("2. Exit")

        choice = input("Choose an option: ").strip()
        if choice == "1":
            pass
        elif choice =="2":
            print("Exiting ...")
            break
        else:
            print("Invalid option")
if __name__ == "__main__":
    main()