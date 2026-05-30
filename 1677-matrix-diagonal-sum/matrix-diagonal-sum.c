#include <stdio.h>
#include <stdlib.h>

// The function name must match exactly what main calls
int diagonalSum(int** mat, int matSize, int* matColSize) {
    int sum = 0;
    int n = matSize;
    
    for (int i = 0; i < n; i++) {
        // Primary diagonal
        sum += mat[i][i];
        
        // Secondary diagonal (avoid double-counting the center element)
        if (i != n - 1 - i) {
            sum += mat[i][n - 1 - i];
        }
    }
    
    return sum;
}