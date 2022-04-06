# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

    def maxArea(self, height: List[int]) -> int:
        # Two For Loops method:
        # Look up height[L], height[R], width=(R-L)
        # area[L,R] = min(HL, HR) x width

        best_area = 0
        heights = []
        for L in range(0, len(height)):
            for R in range(L, len(height)):
                area = min(height[L], height[R]) * (R - L)
                heights.append(area)

        return max(heights)

    def maxArea(self, height: List[int]) -> int:
        # Out working in method:
        # Look up height[L=0], height[R=len(height)-1]
        # Move L or R forward based on min(height[L or R])

        best_area = 0
        L = 0
        R = len(height) - 1
        for j in range(0, len(height)):
            if L > len(height) - 2 or R < 1:
                break
            shorter = L if min(height[L], height[R]) == height[L] else R
            area = min(height[L], height[R]) * (R - L)
            if area > best_area:
                best_area = area
            if shorter == L:
                L += 1
            else:
                R += 1
        return best_area
