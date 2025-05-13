import sys
import os
from wsgiref.handlers import CGIHandler
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

def handler(event, context):
    return app

# For Vercel WSGI compatibility
def handle(req):
    return app(req['headers'], req['body'])

if __name__ == "__main__":
    app.run(debug=True)
