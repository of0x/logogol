import os
from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
app.config.from_object(__name__)

ENV = 'prod'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://pgadmin:self2Geow@localhost/linkdb'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://dwvnvlerrnwgeq:' \
                                            'c2f5ac3c269f27b593bc1f2bc54d28d481fd81cf18f50bfe99613111f2e5aa22' \
                                            '@ec2-54-174-229-152.compute-1.amazonaws.com:5432/dfbru6mqud9k03'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# original way to configure DB (which looks better to me...)
# DATABASE = os.getenv("DATABASE_URL", "sqlite:///debug.db")
# DATABASE = app.config['SQLALCHEMY_DATABASE_URI']
# DATABASE = DATABASE.strip()


CORS(app, resources=r'/*', allow_headers="Content-Type")

import logogol.views