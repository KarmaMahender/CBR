import logging
import json
import pycurl
from io import BytesIO


class FileProcessor:
    def readjsontext(self, filename):
        f = open(filename, 'rb')
        data = f.read()
        data = json.loads(data.decode('utf-8'))
        f.close()
        return data

    def readjson(self, filename):
        f = open(filename, 'rb')
        data = f.read()
        f.close()
        return data

    def writejson(self, filename, data):
        f = open(filename, 'w')
        f.write(str(data))
        f.close()


class Logger:
    __log_format = '[%(asctime)s] [%(levelname)s] : %(message)s'
    __log_date_format = '%m/%d/%Y %I:%M:%S %p'

    def __init__(self, filename, level=logging.INFO, frmt=None, datefrmt=None):
        self.filename = filename
        self.level = level
        if None != Logger.__log_format:
            Logger.__log_format = frmt

        if None != Logger.__log_date_format:
            Logger.__log_date_format = datefrmt
        logging.basicConfig(filename=filename, level=level,
                            format=Logger.__log_format, datefmt=Logger.__log_date_format)

    def logexception(self, exp):
        logging.error(exp)

    def loginfo(self, message):
        logging.info(message)

    def logdebug(self, message):
        logging.debug(message)

    def logwarning(self, message):
        logging.warning(message)


class ResponseProcessor:
    __RESPONSE_CODE = 'RESPONSE_CODE'
    __TOTAL_TIME = 'TOTAL_TIME'
    __RESPONSE_BODY = 'RESPONSE_BODY'

    def setresponse(self, c, data):
        response = {}
        response[ResponseProcessor.__RESPONSE_CODE] = c.getinfo(c.RESPONSE_CODE)
        response[ResponseProcessor.__TOTAL_TIME] = c.getinfo(c.TOTAL_TIME)
        response[ResponseProcessor.__RESPONSE_BODY] = data
        return response

    def validateresponse(self, response):
        if response != None and ResponseProcessor.__RESPONSE_CODE in response.keys():
            if response[ResponseProcessor.__RESPONSE_CODE] == 200:
                return ''
            elif response[ResponseProcessor.__RESPONSE_CODE] == 301 or response[
                ResponseProcessor.__RESPONSE_CODE] == 302:
                return 'redirection happened'
            elif response[ResponseProcessor.__RESPONSE_CODE] == 400:
                return 'Bad Request'
            elif response[ResponseProcessor.__RESPONSE_CODE] == 401:
                return 'Unauthorized'
            elif response[ResponseProcessor.__RESPONSE_CODE] == 402:
                return 'Payment Required'
            elif response[ResponseProcessor.__RESPONSE_CODE] == 403:
                return 'Forbidden'
            elif response[ResponseProcessor.__RESPONSE_CODE] == 404:
                return 'Not Found'
            elif response[ResponseProcessor.__RESPONSE_CODE] == 405:
                return 'Method Not Allowed'
            elif response[ResponseProcessor.__RESPONSE_CODE] == 406:
                return 'Not Acceptable'
            elif response[ResponseProcessor.__RESPONSE_CODE] == 407:
                return 'Proxy Authentication Required'
            elif response[ResponseProcessor.__RESPONSE_CODE] == 408:
                return 'Request Time Out'
            elif response[ResponseProcessor.__RESPONSE_CODE] == 500:
                return 'Internal Server Error'
            elif response[ResponseProcessor.__RESPONSE_CODE] == 501:
                return 'Not Implemented'
            elif response[ResponseProcessor.__RESPONSE_CODE] == 502:
                return 'Bad Gateway'
            elif response[ResponseProcessor.__RESPONSE_CODE] == 503:
                return 'Service Unavailable'
            elif response[ResponseProcessor.__RESPONSE_CODE] == 504:
                return 'Gateway Timeout'


class InternetUtilities:

    __ResponseProcessor = ResponseProcessor()
    __logger = Logger(__name__ + '_errors.log')

    def getpycurl(self, url, headers):
        data = BytesIO()
        c = pycurl.Curl()
        c.setopt(c.URL, url)
        c.setopt(pycurl.HTTPHEADER, headers)
        c.setopt(c.WRITEDATA, data)
        c.perform()
        responsebody = json.loads(data.getvalue().decode('utf-8'))
        response = InternetUtilities.__ResponseProcessor.setresponse(c, responsebody)
        return response
