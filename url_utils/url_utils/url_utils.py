def parse_url(url: str) -> dict:
    """
    Parse a URL into its components.
    
    Args:
        url: The URL to parse.

    Returns:
        A dictionary containing the components of the URL:
        - protocol: The protocol used in the URL (e.g., http, https).
        - subdomains: The subdomains of the URL (e.g., www, blog).
        - domain: The main domain of the URL (e.g., example.com).
        - port: The port number of the URL.
        - path: The path of the URL.
        - parameters: The parameters of the URL.
        - anchor: The anchor of the URL.
    """
    result = {
        'protocol': '',
        'subdomains': '',
        'domain': '',
        'port': '',
        'path': '',
        'parameters': '',
        'anchor': '',
    }

    try:
        if '://' in url:
            result['protocol'], url = url.split('://', 1)
        else:
            result['protocol'] = 'http'

        if '#' in url:
            url, result['anchor'] = url.split('#', 1)

        if '?' in url:
            url, result['parameters'] = url.split('?', 1)

        if '/' in url:
            domain, result['path'] = url.split('/', 1)
            result['path'] = '/' + result['path']
        else:
            domain = url

        if ':' in domain:
            domain, result['port'] = domain.split(':', 1)

        domain_parts = domain.split('.')
        if len(domain_parts) > 2:
            result['subdomains'] = '.'.join(domain_parts[:-2])
            result['domain'] = '.'.join(domain_parts[-2:])
        else:
            result['domain'] = domain

    except Exception as e:
        print(f"Error parsing URL: {e}")

    return result

def remove_url_elements(url: str, elements: list) -> str:
    """
    Remove specified elements from a URL.

    Args:
        url: The original URL.
        elements: A list of elements to remove from the URL. Possible values are:
                    'protocol', 'subdomains', 'domain', 'port', 'path', 'parameters', 'anchor'.

    Returns:
        The URL with the specified elements removed.
    """
    parsed_url = parse_url(url)

    for element in elements:
        if element in parsed_url:
            parsed_url[element] = ''

    return build_url(**parsed_url)

def is_valid_url(url: str) -> bool:
    """
    Check if a URL is valid.

    Args:
        url: The URL to check.

    Returns:
        True if the URL is valid, False otherwise.
    """
    if not url.startswith(('http://', 'https://', 'ftp://', 'ftps://')):
        return False

    parts = parse_url(url)
    
    if not parts['domain']:
        return False

    if parts['port'] and not parts['port'].isdigit():
        return False

    return True

def extract_tld(url: str) -> str:
    """
    Extract the top-level domain (TLD) from a URL.

    Args:
        url: The URL to extract the TLD from.

    Returns:
        The top-level domain (TLD).
    """
    domain = parse_url(url)['domain']
    return domain.split('.')[-1]

def normalize_url(url: str) -> str:
    """
    Normalize a URL by removing unnecessary elements and converting it to lowercase.

    Args:
        url: The URL to normalize.

    Returns:
        The normalized URL.
    """
    parsed_url = parse_url(url)
    normalized_url = parsed_url['protocol'] + '://'
    if parsed_url['subdomains']:
        normalized_url += parsed_url['subdomains'] + '.'
    normalized_url += parsed_url['domain']
    if parsed_url['port']:
        normalized_url += ':' + parsed_url['port']
    normalized_url += parsed_url['path']
    if parsed_url['parameters']:
        normalized_url += '?' + parsed_url['parameters']
    if parsed_url['anchor']:
        normalized_url += '#' + parsed_url['anchor']
    return normalized_url.lower()

def compare_urls(url1: str, url2: str) -> bool:
    """
    Compare two URLs to see if they are equivalent after normalization.

    Args:
        url1: The first URL.
        url2: The second URL.

    Returns:
        True if the URLs are equivalent, False otherwise.
    """
    return normalize_url(url1) == normalize_url(url2)

def extract_query_params(url: str) -> dict:
    """
    Extract query parameters from a URL and return them as a dictionary.

    Args:
        url: The URL to extract query parameters from.

    Returns:
        A dictionary of query parameters.
    """
    params = {}
    parsed_url = parse_url(url)
    if parsed_url['parameters']:
        param_pairs = parsed_url['parameters'].split('&')
        for pair in param_pairs:
            key, value = pair.split('=')
            params[key] = value
    return params

def build_url(protocol: str, subdomains: str, domain: str, port: str, path: str, parameters: str, anchor: str) -> str:
    """
    Build a URL from its components.

    Args:
        protocol: The protocol used in the URL (e.g., http, https).
        subdomains: The subdomains of the URL (e.g., www, blog).
        domain: The main domain of the URL (e.g., example.com).
        port: The port number of the URL.
        path: The path of the URL.
        parameters: The parameters of the URL.
        anchor: The anchor of the URL.

    Returns:
        The constructed URL.
    """
    url = protocol + '://'
    if subdomains:
        url += subdomains + '.'
    url += domain
    if port:
        url += ':' + port
    if path:
        url += path
    if parameters:
        url += '?' + parameters
    if anchor:
        url += '#' + anchor
    return url

def get_base_url(url: str) -> str:
    """
    Get the base URL (protocol + domain + port) from a URL.

    Args:
        url: The URL to extract the base URL from.

    Returns:
        The base URL.
    """
    parsed_url = parse_url(url)
    base_url = parsed_url['protocol'] + '://'
    if parsed_url['subdomains']:
        base_url += parsed_url['subdomains'] + '.'
    base_url += parsed_url['domain']
    if parsed_url['port']:
        base_url += ':' + parsed_url['port']
    return base_url

def update_query_params(url: str, params: dict) -> str:
    """
    Update the query parameters of a URL.

    Args:
        url: The original URL.
        params: A dictionary of query parameters to update.

    Returns:
        The URL with updated query parameters.
    """
    parsed_url = parse_url(url)
    existing_params = extract_query_params(url)
    existing_params.update(params)
    new_params = '&'.join([f"{key}={value}" for key, value in existing_params.items()])
    parsed_url['parameters'] = new_params
    return build_url(**parsed_url)

# Example usage
if __name__ == "__main__":
    url = "https://sub.subdomain.example.com:8080/path?param=value#anchor"
    print(parse_url(url))
    print(remove_url_elements(url, ['protocol', 'port']))
    print(is_valid_url(url))
    print(extract_tld(url))
    print(normalize_url(url))
    print(compare_urls(url, "https://sub.subdomain.example.com:8080/path?param=value#anchor"))
    print(extract_query_params(url))
    print(build_url('https', 'sub.subdomain', 'example.com', '8080', '/path', 'param=value', 'anchor'))
    print(get_base_url(url))
    print(update_query_params(url, {'new_param': 'new_value'}))