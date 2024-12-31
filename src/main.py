from textnode import TextType, TextNode

def main():
    node = TextNode("Test node", TextType.Bold, "https://example.org/")
    print(node)

if __name__ == "__main__":
    main()
