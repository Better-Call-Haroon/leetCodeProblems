/**
 * @param {number} x
 * @return {boolean}
 */
var  isPalindrome = function(x) {
    
    var reverse=0;
    var temp=0;
    var lastdigit=0
    temp=x;
    while(x>0){
    lastdigit = x % 10;
    x= parseInt(x/10);

    
     reverse=(reverse * 10) + lastdigit;

    }
    if(reverse==temp){
        return 1
    }
    else{
        return 0
    }



    

};