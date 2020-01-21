#!/usr/bin/env python3
from logogol import app
from logogol.database import init_db

if __name__ == "__main__":
    init_db()
    app.run(debug=True, threaded=True)