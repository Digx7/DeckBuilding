from request import Request

from Game.Effects.Filters.comparison_filter import ComparisonFilter
from Game.Effects.Filters.Criteria.fixed_criteria import FixedCriteria
from Game.Sources.source_factory import HAND

class DefendRequest(Request):
    """ Represents a Request to Defend """
    
    def __init__(self, attackCard, args):
        """ Initialize the Request with the attack """
        self.attackCard = attackCard
        self.args = args
        self.defenseRequest = ComparisonFilter(HAND, FixedCriteria("isDefense", True, "=="))
        Request.__init__(self, [args.player])
        
    @property
    def defenses(self):
        """ Return the relevant source if any """
        args = args.copy()
        args.parent = None
        return self.defenseRequest.evaluate(args)