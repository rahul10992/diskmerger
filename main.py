import os


def main():
    path = "/Users/rahul/Desktop/repo/RiderProjects/Sandbox/Sandbox/obj"
    parse_directory(path)

def parse_directory(path):
    if not os.path.exists(path):
        raise FileNotFoundError("Directory ", path, " Does not exist")

    files = os.listdir(path)
    for file in files:
        if not os.path.isdir(os.path.join(path, file)):
            extension = file.split(".")[-1]
            print(file, "extension:", extension)
        else:
            print("\nParsing Directory: ", os.path.join(path, file), "\n")
            parse_directory(os.path.join(path, file))
            # print("\n")

    print("\nFinished parsing ", os.path.join(path))

if __name__ == "__main__":
    main()