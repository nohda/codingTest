function solution(array, commands) {
    var answer = [];
    for(var i =0; i<commands.length; i++){
        let number_arr = commands[i];
        let arr = array.slice(number_arr[0]-1,number_arr[1]);
        arr.sort(function(a, b)  {
            return a - b;
          });
        answer.push(arr[number_arr[2]-1]);
    }
    return answer;
}

var array = [1, 5, 2, 6, 3, 7, 4];
var commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]];
solution(array,commands);
