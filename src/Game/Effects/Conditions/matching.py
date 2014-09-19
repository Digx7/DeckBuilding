from Game.Effects.Conditions.Filters.comparison_filter import ComparisonFilter

class Matching:
    """ Represents a condition where a field must match a value """
    
    def __init__(self, field, values, sourceType, operation="IN"):
        """ Initialize the Matching Condition with the field to use and the values it can match """
        self.filter = ComparisonFilter(field, values, sourceType, operation)
        
    def evaluate(self, game, event=None):
        """ Evaluate the condition """
        return len(self.filter.evaluate(game, event=event)) > 0
        