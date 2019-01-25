class ExecutionFlowMiddleware(object):
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        print("This line printed at pre-processing of request")
        response=self.get_response(request)
        print("This line printed at post-processing of request")
        return response

from django.http import HttpResponse
class AppMaintenanceMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        return HttpResponse('<h1>Currently application under maintenance.. Please try after 30mins!!')

class ErrorMessageMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        return self.get_response(request)
    def process_exception(self,request,exception):
        return HttpResponse('<h1>Currently we are facing some technical problems plz try after some time!!!</h1><h2>Raised Exception:{}</h1><h2>Exception Message:{}</h2>'.format(exception.__class__.__name__,exception))
