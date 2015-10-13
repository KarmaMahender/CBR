import CompareBaap.cb.cblib.Affiliate_Utils as AffiliateUtils
import json
from CompareBaap.cb.cblib.models.search import SearchResult


class Flipkart:
    __categories = {'Mobile': [
        'MOBILE',
        'MOBILE PHONES',
        'MOBILEPHONES',
        'PHONES'
        'MOBILE PHONE'
    ]
    }
    __urls = {
        'PRODUCT_FEED': 'https://affiliate-api.flipkart.net/affiliate/api/%s.json',
        'DOTD': 'https://affiliate-api.flipkart.net/affiliate/offers/v1/dotd/json',
        'TOP_OFFERS': 'https://affiliate-api.flipkart.net/affiliate/offers/v1/top/json',
        'ORDER_STATUS': 'https://affiliate-api.flipkart.net/affiliate/report/orders/detail/json?startDate=%s&endDate=%s&status=%s&offset=0',
        'SEARCH_KW': 'https://affiliate-api.flipkart.net/affiliate/search/json?query=%s&resultCount=%s',
        'SEARCH_PRODUCT': 'https://affiliate-api.flipkart.net/affiliate/product/json?id=%s'
    }
    __affid = 'anujaksha'
    __afftoken = 'da6fcf663bd3497dbf58f083a39521d8'
    __ = {}
    __cachedresponse = {}

    def __init__(self):
        self.__loggerErrors = AffiliateUtils.Logger(self.__class__.__name__ + '_errors.log')
        self.__logger= AffiliateUtils.Logger(self.__class__.__name__ + '.log')
        self.__responseprocessor = AffiliateUtils.ResponseProcessor()
        self.__curler = AffiliateUtils.InternetUtilities()
        self.__fileprocessor = AffiliateUtils.FileProcessor()
        self.__headers = ['content-type: application/json',
                          'Accept-Charset: UTF-8',
                          'Fk-Affiliate-Id:' + Flipkart.__affid + '',
                          'Fk-Affiliate-Token:' + Flipkart.__afftoken + '']

    def logmessage(self, response):
        message = self.__responseprocessor.validateresponse(response)
        if message == '':
            print('success')
            self.__logger.loginfo('success')
        else:
            print(message)
            self.__loggerErrors.loginfo(message)

    def getproductfeedresponse(self, filename='productfeedresponse.json'):
        '''
        Method to get product feed details from Flipkart
        '''
        self.__logger.loginfo('getproductfeedresponse() starts')
        self.__logger.loginfo('parameters : ', filename)
        response = {}
        url = Flipkart.__urls['PRODUCT_FEED'] % Flipkart.__affid

        with open(filename, 'wb') as f:
            c = self.__curler.getpycurl(url, f, self.headers)
            response = self.__responseprocessor.setresponse(c)
            c.close()

        self.__logger.loginfo('getproductfeedresponse() ends')
        return response

    def getkeys(self,D):
        '''
        Method to get all the categories available alongwith urls
        '''

        for key in D.keys():
            if isinstance(D[key], dict):
                if 'get' in D[key].keys():
                    Flipkart.__keys[D[key]['resourceName']] = D[key]['get']
                self.getkeys(D[key])

    def readproductfeedresponsedata(self,filename=r'productfeedresponse.json'):
        '''
        Method to read product feed response from file
        '''
        self.__logger.loginfo('readproductfeedresponsedata() starts')
        self.__logger.loginfo('parameters : ', filename)
        data = self.fileprocessor.readjsontext(filename)
        self.getkeys(data)
        self.__logger.loginfo('readproductfeedresponsedata() ends')

    def executecall(self, url):
        '''
        Method to execute service call to Flipkart and get results
        and store results in file
        '''

        self.__logger.loginfo('executecall() starts')
        self.__logger.loginfo('parameters : url : ' + url)
        response = {}
        try:
            response = self.__curler.getpycurl(url, self.__headers)
            self.__logger.loginfo('executecall() ends')
            # self.__loggerErrors.loginfo(response)
            return response

        except Exception as excp:
            self.__loggerErrors.logexception(excp)

        return {}

    def getdotd(self):
        '''
        Method to get Deals of the day
        '''

        self.__logger.loginfo('getdotd() starts')

        url = Flipkart.__urls['DOTD']
        response = self.executecall(url)

        self.__logger.loginfo('getdotd() ends')
        return response

    def gettopoffers(self):
        '''
        Method to get top offers details
        '''
        self.__logger.loginfo('gettopoffers() starts')

        url = Flipkart.__urls['TOP_OFFERS']
        response = self.executecall(url)

        self.__logger.loginfo('gettopoffers() ends')
        return response

    def getproductsearchresultsbyid(self, productId):
        '''
        Method to get product details based on product id
        '''

        self.__logger.loginfo('getproductsearchresults() starts')
        self.__logger.loginfo('parameters : productId : ' + productId)

        url = Flipkart.__urls['SEARCH_PRODUCT'] % productId
        response = self.executecall(url)

        self.__logger.loginfo('getproductsearchresults() ends')
        return response

    def getsearchonkeywords(self, count, keywords1):
        '''
        Method to get search results based on search keywords
        '''
        self.__logger.loginfo('getsearchonkeywords() starts')
        self.__logger.loginfo('parameters : Count : ' + str(count) + ' keywords : ' + keywords1)

        url = Flipkart.__urls['SEARCH_KW'] % (keywords1, str(count))
        response = self.executecall(url)

        self.__logger.loginfo('getsearchonkeywords() ends')
        return response

    def getorderstatus(self, startdate, enddate, status):

        '''
        startdate - format = yyyy-MM-dd
        enddate - format = yyyy-MM-dd
        '''
        self.__logger.loginfo('getorderstatus() starts')
        self.__logger.loginfo(
            'parameters : startdate : ' + str(startdate) + ' enddate : ' + str(enddate) + ' status : ' + status)

        url = Flipkart.__urls['ORDER_STATUS'] % (str(startdate), str(enddate), status)
        response = self.executecall(url)

        self.__logger.loginfo('getorderstatus() ends')
        return response

    def getallproducts(self):
        '''
        Method to get all products available in products feed
        '''
        self.__logger.loginfo('getallproducts() starts')
        for key in Flipkart.__keys():
            self.executecall(Flipkart.__keys[key])
        self.__logger.loginfo('getallproducts() ends')

    def getproductbycategory(self, url, category):
        '''
        Method to get product details by category
        '''
        self.__logger.loginfo('getproductbycategory() starts')

        self.__logger.loginfo('parameters : url : ' + str(url) + ' category : ' + str(category))
        response = self.executecall(url)

        self.__logger.loginfo('getproductbycategory() ends')
        return response

    def readproductdata(self, filename):
        '''
        Method to read file and data into JSON format in data object
        '''
        data = self.__fileprocessor.readjsontext(filename)
        return data

    def get_fk_search_by_productId(self, count, keywords1):
        cr = {}  # Flipkart.__cachedresponse
        if cr and keywords1 in cr:
            responses = cr[keywords1]
        else:
            response = self.getproductbycategory(count=count, keywords1=keywords1)
            if "RESPONSE_BODY" in response:
                productInfoList = response['RESPONSE_BODY']["productInfoList"]
                l = len(productInfoList)
                responses = [SearchResult(productInfoList[i]["productBaseInfo"]["productAttributes"]) for i in range(l)]
                cr[keywords1] = responses
            else:
                responses = None
        return responses

    def get_fk_search_by_keywords(self, count, keywords1):
        cr = {}  # Flipkart.__cachedresponse
        if keywords1 in Flipkart.__categories['Mobile']:
            response = self.getproductbycategory(count=count, keywords1=keywords1)
        else:
            response = self.getsearchonkeywords(count=count, keywords1=keywords1)
            if "RESPONSE_BODY" in response:
                productInfoList = response['RESPONSE_BODY']["productInfoList"]
                l = len(productInfoList)
                responses = [SearchResult(productInfoList[i]["productBaseInfo"]["productAttributes"]) for i in range(l)]
                cr[keywords1] = responses
            else:
                responses = None
        return responses
