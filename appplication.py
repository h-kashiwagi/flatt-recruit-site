import os
import sys
from flaskr import create_app

print(os.getenv('FLASK_CONFIG'))
# 環境変数のFLASK_CONFIGをcreate_appに渡す
app = create_app(os.getenv('FLASK_CONFIG') or 'default')