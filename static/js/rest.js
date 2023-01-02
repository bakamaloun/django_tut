var app = angular.module('rest',[]);
app.controller('restController', function($scope, $http){
    //$scope.restList = [{restText: 'requests0', sent: false}];
    $http.get('/rest_app/api/request').then(function(response){
        $scope.restList = [];
        for (var i = 0; i < response.data.length; i++){
            var rest = {};
            rest.restText = response.data[i].rest_text
            rest.sent = response.data[i].sent
            rest.id = response.data[i].id
            $scope.restList.push(rest);
        }
    });

    $scope.saveData = function(){
        var data = {rest_text: $scope.restInput, sent: false}
        $http.put('/rest_app/api/request', data)
    }

    $scope.restAdd = function(){
        $scope.restList.push({restText: $scope.restInput, sent: false});
        $scope.restInput = '';
    };

    $scope.remove = function(){
        var old_list = $scope.restList;
        $scope.restList = [];
        angular.forEach(old_list, function(x){
            if (x.sent){
                $http.delete('/rest_app/api/request/' + x.id + '');

            } else{
                $scope.restList.push(x);
            }

        })

    }
})