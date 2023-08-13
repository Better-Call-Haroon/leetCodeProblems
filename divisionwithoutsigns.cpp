#include<iostream>
using namespace std;
//integer a is the numerator here 
//integer b is the denomerator


float div(float a,float b){
    float count=1;
    if(a==b){
        return count;
    }
    else {
        do{
            if(a<b){
                cout<<"reminder is "<<a<<endl;
                return count-1;
                break;

            }
            else{

            
            a=a-b;

            count++;

            }
            
            
        

        }
        while(a!=b);
        cout<<"Reminder is 0"<<endl;

        
        return count;
    }

    

}
int main(){
    float x;
    cout<<"enter the number you want to be divided from some other number"<<endl;
    cin>>x;
    float y;
    cout<<"now enter the number you want the other number to divide from"<<endl;
    cin>>y;
    cout<<"value is "<<div(x,y)<<endl;


    return 0;
}