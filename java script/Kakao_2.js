function solution(m, v) {
    var answer = 0;
    var arr = [];
    var count = 0;
    // var len = v.length;
    for(var i = 0; i<v.length; i++){
        arr.push(m-v[i]);
    }
    
    console.log(arr);
    return answer;
}

var m = 4;
var v = [2,3,1];
solution(m,v);