from work_with_txt import read_file, write_file, delete_file, rename_file, copy_file, move_file, add_text, count_words, count_lines, count_characters, count_special_characters, count_digits, count_spaces

def work_with_txt():
    while True:
        print("----------------------------------------")
        print("1. Read file")
        print("2. Write file")
        print("3. Delete file")
        print("4. Rename file")
        print("5. Copy file")
        print("6. Move file")
        print("7. Add text to file")
        print("8. Count words in file")
        print("9. Count lines in file")
        print("10. Count characters in file")
        print("11. Count special characters in file")
        print("12. Count digits in file")
        print("13. Count spaces in file")
        print("14. Exit")
        choice = int(input("Enter your choice: "))
        file_path = input("Enter the file path: ")
        if choice == 1:
            read_file(file_path)
        elif choice == 2:
            write_file(file_path)
        elif choice == 3:
            delete_file(file_path)
        elif choice == 4:
            rename_file(file_path)
        elif choice == 5:
            copy_file(file_path)
        elif choice == 6:
            move_file(file_path)
        elif choice == 7:
            add_text(file_path)
        elif choice == 8:
            count_words(file_path)
        elif choice == 9:
            count_lines(file_path)
        elif choice == 10:
            count_characters(file_path)
        elif choice == 11:
            count_special_characters(file_path)
        elif choice == 12:
            count_digits(file_path)
        elif choice == 13:
            count_spaces(file_path)
        elif choice == 14:
            break
        else:
            print("Invalid choice")
