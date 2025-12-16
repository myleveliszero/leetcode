
def searchMatrix(matrix, target: int) -> bool:
    cols, rows = len(matrix[0]), len(matrix)
    
    rows_l, rows_r = 0, rows-1
    while rows_l <= rows_r:
        m_rows = (rows_r-rows_l)//2 + rows_l
        cols_l, cols_r = 0, cols-1
        if matrix[m_rows][cols_l] <= target <= matrix[m_rows][cols_r]: 
            while cols_l <= cols_r:
                m_cols = (cols_r-cols_l)//2 + cols_l
                if matrix[m_rows][m_cols] == target:
                    return True
                elif matrix[m_rows][m_cols] > target:
                    cols_r = m_cols-1
                else:
                    cols_l = m_cols+1

        if matrix[m_rows][-1] < target:
            rows_l = m_rows+1
        else:
            rows_r = m_rows-1
                
    
    return False
            