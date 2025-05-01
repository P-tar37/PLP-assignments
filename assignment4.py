def read_and_modify_file(filename):
    try:
        with open("input.txt", 'r') as file:
            content = file.read()

        Content_Upper = content.upper()

        new_filename = "modified_" + filename
        with open(new_filename, 'w') as outfile:
            outfile.write(Content_Upper)

        print("Done! The modified file has been saved as:", new_filename)

    except FileNotFoundError:
        print("The file was not found. Please check the name and try again.")
    except:
        print("Something went wrong while reading or writing the file.")


filename = input("Enter the filename to read and modify: ")
read_and_modify_file(filename)
