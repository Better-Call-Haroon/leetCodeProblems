class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        std::vector<int> output;
        int count=0;
        int flag=1;
        for(int i=0;i<temperatures.size();i++){
            if(temperatures[i]<temperatures[i+1]){
                output[i]=1;
            }
            else{
                do{
                    count++;
                    if(flag<=temperatures.size()){
                    flag++;
                    }
                    else if(flag>temperatures.size())
                    {
                        
                        output[i]=0;
                        break;
                    }

                }
                while(temperatures[i]>temperatures[i+flag]);
                count=0;
                flag=1;
                output[i]=count;


            }
        }
        return output;
        
    }
};