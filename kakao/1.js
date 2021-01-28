function solution(n, record) {
    var answer = [];
    var total = [];
    for (var j =0; j<9; j++){
        let arr_in_arr = []
        total.push(arr_in_arr);   
    }
    for(var i = 0; i<record.length; i++){
        let attr_number = record[i].substr(0,1);
        let att_name = record[i].substr(1).replace(" ","");
        if(total[attr_number-1].length === 0){
            total[attr_number-1].push(att_name);
        }
        else{ 
            if(total[attr_number-1].includes(att_name)===false){
                total[attr_number-1].push(att_name);
                if(total[attr_number-1].length > 5){
                    total[attr_number-1].shift();
                }       
            }
        }
    }
    console.log(total)
    for(var k = 0; k< total.length; k++){
        for (var o in total[k]){
          answer.push(total[k][o]);
        }
    }
    console.log(answer)
    return answer;
}

var arr = ["1 fracta", "1 sina","1 hana","1 robel","1 abc", "1 sina", "1 lynn"];

// console.log(arr[0].split(''));
console.log(arr[0].substr(0,1));
// console.log(arr[0].substr(1));

var record = ["1 a","1 b","1 abc","3 b","3 a","1 abcd","1 abc","1 aaa","1 a","1 z","1 q", "3 k", "3 q", "3 z", "3 m", "3 b"];
var n = 1;
solution(n, record);
