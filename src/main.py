from shutil import copytree, rmtree

def copy_static():
    rmtree("./public")
    copytree("./static", "./public")

def main():
    copy_static()

if __name__ == "__main__":
    main()
