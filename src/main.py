from textnode import TextNode, TextType

def main():
    txtNode = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(txtNode)

main()
