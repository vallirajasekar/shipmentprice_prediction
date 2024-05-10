from flask import Flask
from src.logger import logging
from src.exception import ApplicationException
import os,sys

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    try:
        raise Exception('We are testing our Custom Exception')
    except Exception as e:
        test=ApplicationException(e,sys)
    
        logging.info(test.error_message)
        logging.info('We are testing our Exception Module')
        
        return "Practice Make Man Perfect"

if __name__=='__main__':
   app.run(debug=True,port=8000)