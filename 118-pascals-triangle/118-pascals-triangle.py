class Solution:
    def generate(self, num_rows: int) -> List[List[int]]:
      triangle = []
      
      for row_num in range(num_rows):
        row = [None for _ in range(row_num+1)]
        row[0], row[-1] = 1, 1
        
        for i in range(1, len(row) -1):
          row[i] = triangle[row_num - 1][i-1] + triangle[row_num - 1][i]
        triangle.append(row)
      return triangle