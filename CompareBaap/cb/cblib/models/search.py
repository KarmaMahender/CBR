from CompareBaap.cb.cblib.Affiliate_Utils import Logger

__author__ = 'Nemesis'


class SearchResult(object):
    __logger = Logger(__name__ + '_errors.log')

    def __init__(self, response_body):

        if "color" in response_body and response_body["color"] is not None:
            self.color = response_body["color"]
        else:
            self.color = ""

        if "imageUrls" in response_body and response_body["imageUrls"] is not None:
            if "100x100" in response_body["imageUrls"] and response_body["imageUrls"]["100x100"] is not None:
                self.img_url = response_body["imageUrls"]["100x100"]
            elif "75x75" in response_body["imageUrls"]and response_body["imageUrls"]["75x75"] is not None:
                self.img_url = response_body["imageUrls"]["75x75"]
            elif "125x125" in response_body["imageUrls"]and response_body["imageUrls"]["125x125"] is not None:
                self.img_url = response_body["imageUrls"]["125x125"]
            elif "40x40" in response_body["imageUrls"]and response_body["imageUrls"]["40x40"] is not None:
                self.img_url = response_body["imageUrls"]["40x40"]
            elif "unknown" in response_body["imageUrls"]and response_body["imageUrls"]["unknown"] is not None:
                self.img_url = response_body["imageUrls"]["unknown"]
            else:
                self.img_url = ""
        else:
            self.img_url = ""

        if "title" in response_body and response_body["title"] is not None:
            self.title = response_body["title"]
        else:
            self.title = ""

        if "productUrl" in response_body and response_body["productUrl"] is not None:
            self.product_url = response_body["productUrl"]
        else:
            self.product_url = ""

        if "productBrand" in response_body and response_body["productBrand"] is not None:
            self.productBrand = response_body["productBrand"]
        else:
            self.productBrand = ""

        if "inStock" in response_body and response_body["inStock"] is not None:
            self.inStock = response_body["inStock"]
        else:
            self.inStock = False

        if "codAvailable" in response_body and response_body["codAvailable"] is not None:
            self.codAvailable = response_body["codAvailable"]
        else:
            self.codAvailable = False

        if "emiAvailable" in response_body and response_body["emiAvailable"] is not None:
            self.emiAvailable = response_body["emiAvailable"]
        else:
            self.emiAvailable = False

        if "maximumRetailPrice" in response_body and response_body["maximumRetailPrice"] is not None:
            if "amount" in response_body["maximumRetailPrice"] and response_body["maximumRetailPrice"]["amount"] is not None:
                self.maximumRetailPrice = response_body["maximumRetailPrice"]["amount"]
            else:
                self.maximumRetailPrice = 0.00
            if "currency" in response_body["maximumRetailPrice"] and response_body["maximumRetailPrice"]["currency"] is not None:
                self.maximumRetailCurrency = response_body["maximumRetailPrice"]["currency"]
            else:
                self.maximumRetailCurrency = "INR"
        else:
            self.maximumRetailPrice = 0.00
            self.maximumRetailCurrency = "INR"

        if "sellingPrice" in response_body and response_body["sellingPrice"] is not None:
            if "amount" in response_body["sellingPrice"] and response_body["sellingPrice"]["amount"] is not None:
                self.sellingPrice = response_body["sellingPrice"]["amount"]
            else:
                self.sellingPrice = 0.00
            if "currency" in response_body["sellingPrice"] and response_body["sellingPrice"]["currency"] is not None:
                self.sellingCurrency = response_body["sellingPrice"]["currency"]
            else:
                self.sellingCurrency = "INR"
        else:
            self.sellingPrice = 0.00
            self.maximumRetailCurrency = "INR"

        if "discountPercentage" in response_body and response_body["discountPercentage"] is not None:
            self.discountPercentage = response_body["discountPercentage"]
        else:
            self.discountPercentage = 0


class SearchResponses(object):
    def __init__(self, fk_response, sd_response, ama_response):
        self.FlipKartResponse = fk_response
        self.SnapdealResponse = sd_response
        self.AmamzonResponse = ama_response
