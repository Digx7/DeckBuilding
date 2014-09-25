
class PlayCard:
    """ Represents a Command to play a card """
    
    def __init__(self, card, owner):
        """ Initialize the Play Card Command """
        self.card = card
        self.owner = owner
        
    def perform(self):
        """ Perform the command """
        coroutine = self.owner.playCardFromHand(self.card)
        response = yield coroutine.next()
        while True:
            response = yield coroutine.send(response)