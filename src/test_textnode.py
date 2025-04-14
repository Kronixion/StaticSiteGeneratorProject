import unittest

from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        #Testing Bold Equality
        node1_bold = TextNode("This is a text node", TextType.BOLD)
        node2_bold = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1_bold, node2_bold)

        #Testing Link Equality
        node1_link = TextNode("This is a link to google", TextType.LINK, "https://www.google.com")
        node2_link = TextNode("This is a link to google", TextType.LINK, "https://www.google.com")
        self.assertEqual(node1_link, node2_link)

        #Testing Italic Difference
        node1_italic = TextNode("This is a italic text node", TextType.ITALIC)
        node2_normal = TextNode("This is a normal text node", TextType.TEXT)
        self.assertNotEqual(node1_italic, node2_normal)

        #Test URL None Property
        node3_link = TextNode("This is a link text node to boot.dev", TextType.LINK, "https://www.boot.dev")
        node4_link = TextNode("This is a link text node to boot.dev", TextType.LINK)
        self.assertNotEqual(node3_link, node4_link)

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")

if __name__ == "__main__":
    unittest.main()
