import os
from shutil import copytree, rmtree

from mdtohtml import generate_page

def copy_static():
    rmtree("./public")
    copytree("./static", "./public")

def generate_pages(rootdir="./content/", dir=""):
    """
    Generate all the pages from the /content directory, using the /templates directory, and output to the /public directory.
    :return:
    """
    template = "./templates/html"

    print("Generating pages for", os.path.join(rootdir, dir))

    for item in os.listdir(rootdir + dir):
        fullpath = os.path.join(rootdir, dir, item)

        if os.path.isdir(fullpath):
            generate_pages(rootdir, os.path.join(dir, item))
        else:
            if not os.path.exists(os.path.join("./public", dir)):
                os.makedirs(os.path.join("./public", dir))

            output_path = os.path.join("./public", dir, item.replace(".md", ".html"))

            if item.endswith(".md"):
                generate_page(fullpath, template, output_path)

def main():
    copy_static()
    generate_pages()

if __name__ == "__main__":
    main()
