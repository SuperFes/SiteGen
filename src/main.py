from shutil import copytree, rmtree

from mdtohtml import generate_page

def copy_static():
    rmtree("./public")
    copytree("./static", "./public")

def generate():
    generate_page("./content/index.md", "./templates/html", "./public/index.html")

def main():
    copy_static()
    generate()

if __name__ == "__main__":
    main()
