
from flask import Flask
application = app = Flask(__name__)
@app.route('/')
def helloworld():
   return "hello World"
if __name__ == '__main__':   
   app.run()    

