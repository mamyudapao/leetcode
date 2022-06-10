class Solution:
  def getRow(self, rowIndex: int) -> List[int]:
    if rowIndex == 0:
      return [1]
    
    prevRow = self.getRow(rowIndex-1)
    if rowIndex == 1:
      return [1, 1]
    
    return [1] + [prevRow[i] + prevRow[i+1] for i in range(rowIndex-1)] + [1]