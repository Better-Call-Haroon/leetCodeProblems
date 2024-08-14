#include <iostream>
int main()
{
    int sumSquare = 0;
    int squareSum = 0;
    int finalDif = 0;
    for (int i = 1; i <= 100; i++) {
        sumSquare+=(i * i);

    }
    for (int j = 1; j <= 100; j++) {
        squareSum += j;
    }
    squareSum = squareSum * squareSum;
    if (sumSquare < squareSum) {
        finalDif = squareSum - sumSquare;
    }
    else {
        finalDif = sumSquare-squareSum;
    }
    std::cout << finalDif << std::endl;
    return 0;
}
