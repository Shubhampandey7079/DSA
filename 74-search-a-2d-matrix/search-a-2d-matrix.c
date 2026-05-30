bool searchMatrix(int** matrix, int matrixSize, int* matrixColSize, int target) {
    if (matrixSize == 0 || matrixColSize == 0) {
        return false;
    }

    int rows = matrixSize;
    int cols = matrixColSize[0];
    int low = 0;
    int high = (rows * cols) - 1;

    while (low <= high) {
        int mid = low + (high - low) / 2;
        int mid_value = matrix[mid / cols][mid % cols];

        if (mid_value == target) {
            return true;
        } else if (mid_value < target) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    return false;
}