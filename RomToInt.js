/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    var count=0;
    for(var i=0;i<s.length;i++){
        if(s[i]=='I'){
            count=count+1;
        }
        if(s[i]=='V'){
            count=count+5;
        }
        if(s[i]=='X'){
            count=count+10;
        }
        if(s[i]=='L'){
            count=count+50;
        }
        if(s[i]=='C'){
            count=count+100;
        }
        if(s[i]=='D'){
            count=count+500;
        }
        if(s[i]=='M'){
            count=count+1000;
        }
        if(s[i]=='I'&&s[i+1]=='V'){
            count=count+4;
            count=(count-1)-5;
        }
        if(s[i]=='I'&&s[i+1]=='X'){
            count=count+9;
            count=(count-1)-10;
        }
        if(s[i]=='X'&&s[i+1]=='L'){
            count=count+40;
            count=(count-10)-50;

        }
        if(s[i]=='X'&&s[i+1]=='C'){
            count=count+90;
            count=(count-10)-100;
        }
        if(s[i]=='C'&&s[i+1]=='D'){
            count=count+400;
            count=(count-100)-500;
        }
        if(s[i]=='C'&&s[i+1]=='M'){
            count=count+900;
            count=(count-100)-1000;
        }
    }
    return count;
    
};