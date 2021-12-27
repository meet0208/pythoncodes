from http.client import HTTPConnection
conn = HTTPConnection("google.com")
conn.request("GET", "/")
result = conn.getresponse()
print(result)
contents = result.read()
print(contents)