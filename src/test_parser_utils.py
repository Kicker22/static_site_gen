import unittest
from transform import extract_markdown_images, extract_markdown_links

class TestMarkdownExtraction(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "Here is an ![image1](http://img1.com) and ![image2](http://img2.com)"
        )
        self.assertListEqual(
            matches, [("image1", "http://img1.com"), ("image2", "http://img2.com")]
        )

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "Click [Google](https://google.com) and [GitHub](https://github.com)"
        )
        self.assertListEqual(
            matches, [("Google", "https://google.com"), ("GitHub", "https://github.com")]
        )

    def test_ignores_images_in_link_extraction(self):
        text = "Here is a ![image](http://image.com) and [link](http://link.com)"
        matches = extract_markdown_links(text)
        self.assertListEqual(matches, [("link", "http://link.com")])
