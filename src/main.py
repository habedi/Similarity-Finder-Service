import sys
import os

from flask import Flask
from libs.server import SimilarityFinder

if __name__ == "__main__":
    try:
        port = int(os.environ.get("SIMILARITY_FINDER_PORT", 8000))
        host = os.environ.get("SIMILARITY_FINDER_HOST", "127.0.0.1")

        flask_app = Flask("SimilarityFinderService")
        server = SimilarityFinder(flask_app)
        server.run(host=host, port=port, debug=True, use_reloader=False,
               threaded=True)
        
    except (SystemExit):
        sys.exit(0)
    except Exception as err:
        print(err)
        sys.exit(-1)
