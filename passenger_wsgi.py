import sys, os
cwd = os.getcwd()
videoportrait_directory = cwd + '/videoportrait'
sys.stdout = sys.stderr
sys.path.insert(0,videoportrait_directory)
sys.path.append(os.getcwd())
os.environ['DJANGO_SETTINGS_MODULE'] = "videoportrait.settings"
import django.core.handlers.wsgi
#from paste.exceptions.errormiddleware import ErrorMiddleware

application = django.core.handlers.wsgi.WSGIHandler()

# To cut django out of the loop, comment the above application = ... line ,
# and remove "test" from the below function definition.

def testapplication(environ, start_response):
    status = '200 OK'
    output = 'Hello World! Running Python version ' + sys.version + '\n\n'
    
    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    
    output += "motorshare directory = " + motorshare_directory + "\n\n"
    
    for i in sys.path:
        output += i + '\n\n'
   
    # to test paste's error catching prowess, uncomment the following line
    # while this function is the "application"

    #raise("error")

    start_response(status, response_headers)
    
    return [output]

#application = ErrorMiddleware(application, debug=True)

