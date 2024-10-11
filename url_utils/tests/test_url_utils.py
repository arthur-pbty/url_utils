import unittest
from url_utils import (
    parse_url,
    remove_url_elements,
    is_valid_url,
    extract_tld,
    normalize_url,
    compare_urls,
    extract_query_params,
    build_url,
    get_base_url,
    update_query_params
)

class TestURLUtils(unittest.TestCase):
    def test_parse_url(self):
        url = "https://sub.subdomain.example.com:8080/path?param=value#anchor"
        parsed = parse_url(url)
        self.assertEqual(parsed['protocol'], 'https')
        self.assertEqual(parsed['subdomains'], 'sub.subdomain')
        self.assertEqual(parsed['domain'], 'example.com')
        self.assertEqual(parsed['port'], '8080')
        self.assertEqual(parsed['path'], '/path')
        self.assertEqual(parsed['parameters'], 'param=value')
        self.assertEqual(parsed['anchor'], 'anchor')

    # Ajoutez d'autres tests pour les autres fonctions

if __name__ == '__main__':
    unittest.main()