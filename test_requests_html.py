from requests_html import HTMLSession

session = HTMLSession()
response = session.get('https://www.google.com')
print(response.status_code)
