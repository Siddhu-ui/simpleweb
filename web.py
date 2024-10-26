from http.server import HTTPServer,BaseHTTPRequestHandler

content='''<html>
    <body>
        <head>
            <center> <h1>Camu slot time table</h1> </center>
         </head>
        <TABLE border="2" cellpadding="30">
            <caption>Weekely schedule</caption>
            <tr bgcolor="purple" style="color: rgb(242, 255, 0);">
               <h1> <th>Time</th> <th> Sunday</th> <th>Monday</th> <th>Tuesday</th> <th>Wednesday</th> <th>Thursday</th> <th>Friday</th> <th>Saturday</th></h1>
            </tr>

            <tr>
                <td bgcolor="purple" style="color: rgb(175, 184, 11);">8am-10am</td><td bgcolor="orange"></td><td bgcolor="orange"></td><td bgcolor="red">Career development</td><td bgcolor="orange"></td><td bgcolor="orange"></td><td bgcolor="sky blue">Maths</td><td bgcolor="orange"></td>
            </tr>
            <tr>
                <td bgcolor="purple" style="color: rgb(175, 184, 11);">10am-12am</td><td bgcolor="orange"></td><td bgcolor="blue">Web applications</td><td bgcolor="green">Digital electronics</td><td bgcolor="blue">web applications</td><td bgcolor="pink">C program</td><td bgcolor="gold">physics</td><td bgcolor="skyblue">Maths</td>
            </tr>
                <td bgcolor="purple" style="color: rgb(175, 184, 11);">1pm-3pm</td><td bgcolor="orange"></td><td bgcolor="yellow">Human values</td><td bgcolor="pink">c programming</td><td bgcolor="orange"></td><td bgcolor="gold">physics</td><td bgcolor="green">digital electronics</td><td bgcolor="blue">Web applications</td>
            <tr>

            </tr>
        </TABLE>
    </body>
</html> '''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',800)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()