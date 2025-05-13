import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

def handler(event, context):
    return app(event, context)

# Expose Flask app for local development
if __name__ == "__main__":
    app.run(debug=True)
