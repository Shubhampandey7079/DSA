#include <stdio.h>
#include <stdlib.h>


int diagonalSum(int** mat, int matSize, int* matColSize) {
    int sum = 0;
    int n = matSize;
    
    for (int i = 0; i < n; i++) {
       
        sum += mat[i][i];
        
     
        if (i != n - 1 - i) {
            sum += mat[i][n - 1 - i];
        }
    }
    
    return sum;
}