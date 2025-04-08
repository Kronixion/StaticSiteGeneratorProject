import unittest

from textnode import TextNode, TextType

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
        node2_normal = TextNode("This is a normal text node", TextType.NORMAL)
        self.assertNotEqual(node1_italic, node2_normal)

        #Test URL None Property
        node3_link = TextNode("This is a link text node to boot.dev", TextType.LINK, "https://www.boot.dev")
        node4_link = TextNode("This is a link text node to boot.dev", TextType.LINK)
        self.assertNotEqual(node3_link, node4_link)

if __name__ == "__main__":
    unittest.main()
