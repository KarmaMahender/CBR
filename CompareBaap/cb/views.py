from django.shortcuts import render_to_response
import json
from cb.Flipkart.Affiliate_Flipkart import Flipkart
from cb.cblib.Affiliate_Utils import Logger
from cb.cblib.models.search import SearchResponses

__author__ = 'Nemesis'


class Views:
    __logger = Logger(__name__ + '_errors.log')

    def __init__(self):
        self._flipkart = Flipkart()

    def get_index(self, request):
        return render_to_response('index.html')

    def get_top_offers(self, request):
        response = self._flipkart.gettopoffers()

    def search(self, request, query):
        if not query:
            query = request.GET.get('q', '')
        Views.__logger.loginfo(query)
        if query:
            query = '%20'.join(query.split(' '))
            fk_response = self._flipkart.get_fk_search_by_keywords(10, query)

            if fk_response is None or len(fk_response) == 0:
                fk_response = self._flipkart.getproductsearchresultsbyid( query)
                if fk_response is None or len(fk_response) == 0:
                    fk_response = []

            sd_response = []  # self._flipkart.get_fk_search_by_keywords(10, query)
            if sd_response is None:
                sd_response = []
            ama_response = []  # self._flipkart.get_fk_search_by_keywords(10, query)
            if ama_response is None:
                ama_response = []
            response = SearchResponses(fk_response, sd_response, ama_response)
        else:
            response = SearchResponses([], [], [])

        return render_to_response('searchpartial.html', {'response': response})
