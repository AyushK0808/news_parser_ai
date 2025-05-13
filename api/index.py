import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

handler=app

if __name__ == "__main__":
    handler.run(debug=True)
