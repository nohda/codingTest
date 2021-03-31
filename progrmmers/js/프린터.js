function solution(priorities, location) {
    var answer = 0;
    let arr = priorities.slice(0,priorities.length);
    let printNumber =  arr.sort(function(a, b) {
        return b - a;
      })[0];

    let maxNumber = priorities.findIndex((element)=>element === printNumber);
    console.log(printNumber,priorities,maxNumber);
    
    return answer;
}

priorities = [2, 1, 3, 2];
location = 2;
// priorities = [1, 1, 9, 1, 1, 1]
// location = 0

solution(priorities, location);