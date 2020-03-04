from app import app

def application(env, start_response):
<<<<<<< HEAD
    start_response('200 OK', [('Content-Type', 'text/html')])   	
    app()
#if __name__ == "__main__":
#    application()                                                                                                                                                                                                                                                                                        
=======
    start_response('200 OK', [('Content-Type', 'text/html')])
    app()                                                                                                                                                                                                                                                                              
>>>>>>> 08508ba8d5a1c3367178fac0c968461354f2f2da
