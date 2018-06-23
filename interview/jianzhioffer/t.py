# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
class Solution:
    def backtracing(self, matrix, m, n, i, j, route, path, pidx):
        if pidx == len(path):
            return True
        if i<0 or j<0 or i>=m or j>=n or route[i][j] or matrix[i][j] != path[pidx]:
            return False
        route[i][j] = True
        for pos in [(-1,0), (1, 0), (0, 1), (0, -1)]:
            if self.backtracing(matrix, m, n, i+pos[0], j+pos[1], route, path, pidx+1):
                return True
        # 回溯
        route[i][j] = False
        return False


    def hasPath(self, matrix, rows, cols, path):
        if len(path) == 0:
            return False
        mat = []
        n = 0
        item = []
        for x in matrix:
            n += 1
            if n % cols == 0 and len(item) > 0:
                item.append(x)
                mat.append(item)
                item = []
                n = 0
            else:
                item.append(x)
        print(mat)        
        route = [[False for x in range(cols)] for x in range(rows)]
        # 出发点不固定，故要遍历每个可能的出发点
        for i in range(rows):
            for j in range(cols):
                if self.backtracing(mat, rows, cols, i, j, route, path, 0):
                    return True
        return False 
if __name__ == '__main__':
    s = Solution()
    matrix = 'ABCESFCSADEE'
    f = s.hasPath(matrix, 3, 4, 'ABCCED')
    print(f)
