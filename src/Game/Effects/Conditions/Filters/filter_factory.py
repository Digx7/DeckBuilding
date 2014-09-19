from comparison_filter import ComparisonFilter
from unique_filter import UniqueFilter

class FilterFactory:
    """ Factory to build Filters """
    
    def loadFitler(self, filterJSON):
        """ Load the Filter from the given JSON """
        if filterJSON["type"] == "COMPARISON":
            return ComparisonFilter(filterJson["field"], filterJson["values"], filterJSON["sourceType"], filterJson["operation"])
        elif filterJSON["type"] == "UNIQUE":
            return ComparisonFilter(filterJson["field"], filterJSON["sourceType"])
        else:
            print "Cannot find Filter:", filterJSON["type"]
        return None
        
FilterFactory = FilterFactory()