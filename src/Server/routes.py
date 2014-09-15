from Server.Controller.start_game_controller import StartGameController
from Server.Controller.get_game_controller import GetGameController
from Server.Controller.buy_card_controller import BuyCardController
from Server.Controller.choose_controller import ChooseController
from Server.Controller.end_turn_controller import EndTurnController
from Server.Controller.pick_card_controller import PickCardController
from Server.Controller.play_card_controller import PlayCardController

from kao_flask.endpoint import Endpoint
from kao_flask.controllers.html_controller import HTMLController

routes = [Endpoint('/', get=HTMLController('Server/templates/index.html')),
          Endpoint('/api/startgame', post=StartGameController()),
          Endpoint('/api/game/<int:gameId>', get=GetGameController()),
          Endpoint('/api/game/<int:gameId>/buy', post=BuyCardController()),
          Endpoint('/api/game/<int:gameId>/choose', post=ChooseController()),
          Endpoint('/api/game/<int:gameId>/endturn', post=EndTurnController()),
          Endpoint('/api/game/<int:gameId>/pickcard', post=PickCardController()),
          Endpoint('/api/game/<int:gameId>/play', post=PlayCardController())]