#include <iostream>
int main()
{
    int counter = 0;
    for (int i = 1; i < 1000; i++) {
        if (i % 3==0 || i % 5 == 0) {
            counter = counter + i;
        }        
    }
    std::cout << counter << std::endl;
    return 0;
}