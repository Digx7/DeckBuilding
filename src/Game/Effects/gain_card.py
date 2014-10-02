from Game.Sources.source_factory import SourceFactory, DISCARD_PILE

class GainCard:
    """ Represents an effect to Gain a card """
    
    def __init__(self, fromSourceType, toSourceType=None):
        """ Initialize the Effect with the card to remove from play before discarding """
        self.fromSourceType = fromSourceType
        if toSourceType is None:
            toSourceType = DISCARD_PILE
        self.toSourceType = toSourceType
        
    def perform(self, context):
        """ Perform the Game Effect """
        fromSource = SourceFactory.getSourceForEffect(self.fromSourceType, context)
        toSource = SourceFactory.getSourceForEffect(self.toSourceType, context)
        
        for card in fromSource:
            coroutine = context.owner.gainCard(card, fromSource, toSource=toSource)
            try:
                response = yield coroutine.next()
                while True:
                    response = yield coroutine.send(response)
            except StopIteration:
                pass