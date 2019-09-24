

import cgi

form = cgi.FieldStorage()

print("Content-type:  text/html\n")

print("<HTML><HEAD></HEAD><BODY>")
print("parameters entered:  <BR>")
print("<p>name:  {}</p>".format(form.getvalue("person_name")))
print("<p>age:  {}</p>".format(form.getvalue("age")))
print("</BODY><HTML>")

