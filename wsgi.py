from cgi import parse_qs


def application(environ, start_response):
    query = parse_qs(environ['QUERY_STRING'])
    
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return ['Hello world!\n'] + ['{0}={1}\n'.format(k,environ[k])
                                 for k in sorted(environ)] + [repr(query)]

