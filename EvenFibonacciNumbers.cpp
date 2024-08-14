#include <iostream>
int main()
{
    int* arr= new int[4000000];
    arr[0] = 1;
    arr[1] = 2;
    int sum = 2;
    for (int i = 2;; i++) {
        arr[i] = arr[i - 1] + arr[i - 2];
        if (arr[i] > 4000000) {
            break;
        }
        if (arr[i] % 2 == 0) {
            sum = sum + arr[i];
        }
    }
    std::cout << sum << std::endl;
    return 0;
}
