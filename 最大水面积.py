class Solution1(object):
    def maxArea(self,height):
        Len = len(height)
        Maxx = 0
        for i in range(Len):
            for j in range(i + 1, Len):
                Maxx = max(min(height[i], height[j]) * (j - i),Maxx)
        return Maxx


class Solution(object):
    def maxArea(self, height):

        Len = len(height)
        left = 0
        right = Len - 1
        Maxx = (Len - 1) * min(height[right], height[left])
        while (right != left):
            Maxx = max(Maxx, (right - left) * min(height[left], height[right]))
            if (height[right] < height[left]):
                right = right - 1
            else:
                left = left + 1
        return Maxx