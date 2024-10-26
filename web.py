from http.server import HTTPServer,BaseHTTPRequestHandler

content='''
<!DOCTYPE html>
<html>
<head>
<style>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 4px solid #8d8b8b;
  text-align:center;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>
</head>
<body>

<h2><CENTER>LAPTOP CONFRIGURATIONS</CENTER></h2>

<table>
  <tr>
    <th>Configuration</th>
    <th>Value</th>
  </tr>
  <tr>
    <td>Device Name</td>
    <td>DESKTOP-GQEUIBF</td>
  </tr>
  <tr>
    <td>Processor</td>
    <td>AMD Ryzen 7 73709HR w/Radeon 780M Graphics 3.80GHz</td>
  </tr>
  <tr>
    <td>Installed RAM</td>
    <td>16.0GB</td>
  </tr>
  <tr>
    <td>System Type</td>
    <td>64.bit OS</td>
  </tr>
  <tr>
    <td>Edition</td>
    <td>Windows 11 HSL</td>
  </tr>
  <tr>
    <td>Version</td>
    <td>21H2</td>
  </tr>
</table>
</body>
</html>
'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())


print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()