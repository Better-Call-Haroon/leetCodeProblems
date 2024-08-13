#include <iostream>


int main()

{
    int arr[998];
    int start = 1;
    int counter = 0;
    for (int i = 0; i <= 998; i++) {
        arr[i] = start;
        start++;
    }
    for (int i = 0; i <= 998; i++) {
        if (arr[i] % 3==0 || arr[i] % 5 == 0) {
            counter = counter + arr[i];
        }
        
    }
    std::cout << counter << std::endl;

    return 0;
}
