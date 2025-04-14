import unittest

from  htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_HTML_Node(self):
        html_node1 = HTMLNode("p", "Lorem Ipsum Odorum Contice Vespucii.", [], {"style":"color:red;text-align:center"})        
        self.assertEqual(html_node1.tag,"p")
        self.assertEqual(html_node1.value, "Lorem Ipsum Odorum Contice Vespucii.")
        self.assertNotEqual(html_node1.children, [""])
        
if __name__ == "__main__":
    unittest.main()
