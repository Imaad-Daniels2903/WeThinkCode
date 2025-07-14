def main():
    file = input("File name: ").strip()

    if "." not in file:
        print("application/octet-stream")

    else:
        file_list = file.split(".")
        extension = file_list[-1].lower()

        match extension:
            case "gif" | "png":
                type = f"image/{extension}"
                print(type)

            case "pdf" | "zip" :
                type = f"application/{extension}"
                print(type)

            case "jpg" | "jpeg":
                type = f"image/jpeg"
                print(type)

            case "txt":
                type = f"text/plain"
                print(type)

            case _:
                print("application/octet-stream")


if  __name__ == "__main__":
    main()
