class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        altitude=0
        max_altitude=0
        for num in gain:
            altitude+=num
            max_altitude=max(altitude,max_altitude)
        return max_altitude