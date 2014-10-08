'use strict';

var controllers = angular.module('DeckBuildingControllers', ['ui.bootstrap', 'ngCookies', 'DeckBuildingServices']);

controllers.controller('StartGameController', function ($scope, $http, $location) {
    $scope.startGame = function() {
        $http.post('/api/startgame').success(function(data) {
            $scope.game = data['game'];
            $location.path('/game/'+$scope.game.id);
        }).error(function(error) {
            alert(error);
        });
    };
});

controllers.controller('LobbiesController', function($scope, lobbiesService) {
    lobbiesService.startPolling($scope, function(lobbies) {
        $scope.lobbies = lobbies;
    });
    $scope.startNewLobby = lobbiesService.startNewLobby;
    $scope.joinLobby = lobbiesService.joinLobby;
    $scope.trackLobby = lobbiesService.trackLobby;
    $scope.goToLobby = lobbiesService.goToLobby;
});
controllers.controller('LobbyController', function($scope, lobbyService) {
    lobbyService.startPolling($scope, function(lobby) {
        $scope.lobby = lobby;
    });
    $scope.changeCharacter = function() {
        lobbyService.changeCharacter($scope.newCharacter);
    };
    $scope.changeName = function() {
        lobbyService.changeName($scope.newName);
    };
    $scope.startGame = lobbyService.startGame;
});
controllers.controller('GameController', function($scope, gameService) {
    gameService.startPolling($scope, function(game) {
        $scope.game = game;
    });
    $scope.actions = gameService.actions;
    $scope.endTurn = gameService.endTurn;
    $scope.chooseOption = gameService.chooseOption;
    $scope.pickCard = gameService.pickCard;
    $scope.defend = gameService.defend;
});
controllers.controller('GameResultsController', function($scope, $cookies, $http, $routeParams) {
    var rootUrl = '/api/game/'+$routeParams.gameId+'/player/'+$cookies.playerId+'/results';
    $http.get(rootUrl).success(function(data) {
        $scope.results = data;
    }).error(function(error) {
        console.log(error);
    });
});

controllers.controller('ChooseOptionController', function($scope, requestModalService, gameService) {
    $scope.request = gameService.getGame().request;
    
    $scope.chooseOption = function(index) {
        gameService.chooseOption(index);
        requestModalService.closeModal();
    };
});

controllers.controller('PickCardController', function($scope, requestModalService, gameService) {
    $scope.request = gameService.getGame().request;
    $scope.actions = {};
    $scope.indices = [];
    $scope.actions.pickCard = function(index) {
        $scope.indices.push(index);
        if ($scope.indices.length ===  $scope.request.number) {
            $scope.sendChoices();
        }
    };
    $scope.hasCard = function(index) {
        return $scope.indices.indexOf(index) > -1;
    };
    $scope.sendChoices = function() {
        gameService.pickCard($scope.indices);
        requestModalService.closeModal();
    };
});

controllers.controller('DefendController', function($scope, requestModalService, gameService) {
    $scope.request = gameService.getGame().request;
    $scope.actions = {};
    $scope.actions.pickCard = function(index) {
        gameService.defend(true, index);
        requestModalService.closeModal();
    };
    $scope.abortDefense = function() {
        gameService.defend(false);
        requestModalService.closeModal();
    };
});

controllers.controller('NotificationController', function($scope, notificationService, Poller) {
    $scope.notifications = [];
    Poller($scope, function() {
        $scope.notifications = notificationService.getNotifications();
    });
});

controllers.controller('ExamineCardIconController', function($scope, examineModalService) {
    $scope.examineCard = function(card) {
        examineModalService.open(card);
    };
});

controllers.controller('ExamineCardController', function($scope, examineModalService, card) {
    $scope.card = card;
    $scope.close = function() {
        examineModalService.close();
    };
});