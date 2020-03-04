from app import app

def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])   	
    app()
#if __name__ == "__main__":
#    application()                                                                                                                                                                                                                                                                                        
