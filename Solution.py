from __future__ import division
class Solution:
    def food_ratio_distribution(self, ratios, portions):
        if ratios is None or len(ratios) <=0 or not isinstance(ratios, dict):
            print("Enter a valid ratio")

        if portions < 0:
            print('Enter a valid Portion')

        denominator = 0
        result_distribution = {}
        portions_remaining = {}

        for key, value in ratios.items():
            denominator += ratios[key]

        if denominator <= 0:
            return result_distribution

        largestRemainder = denominator/portions
        allocatedPortion = 0

        for key, value in ratios.items():
            autoPortion = ratios[key]/largestRemainder
            result_distribution[key] = int(autoPortion)
            portions_remaining[key] = autoPortion - result_distribution[key]
            allocatedPortion += result_distribution[key]

        remainderPortion = portions - allocatedPortion

        # Split left over portions
        for i in range(0, remainderPortion):
            max = 0
            max_index = 0
            for key,value in ratios.items():
                if portions_remaining[key] > max:
                    max = portions_remaining[key]
                    max_index = key

            result_distribution[max_index] += 1
            portions_remaining[max_index] = 0

        return result_distribution


s = Solution()
s.food_ratio_distribution({}, 1)
print(s.food_ratio_distribution({1: 1}, 2))
print(s.food_ratio_distribution({1: 1, 2: 1, 3: 1}, 11))
print(s.food_ratio_distribution({1: 0, 2: 0, 3: 4}, 7))        #-> {1: 0, 2: 0, 3: 7}
print(s.food_ratio_distribution({1: 0, 2: 0, 3: 4}, 3))        #-> {1: 0, 2: 0, 3: 3}
print(s.food_ratio_distribution({1: 4, 2: 9, 3: 1, 8: 7}, 5))  #-> {1: 1, 2: 2, 3: 0, 8: 2}
print(s.food_ratio_distribution({3: 4, 1: 9, 7: 1}, 14))       #-> {1: 9, 3: 4, 7: 1}
print(s.food_ratio_distribution({3: 4, 1: 9, 7: 1}, 5))        #-> {1: 3, 3: 2, 7: 0}
print(s.food_ratio_distribution({3: 4, 1: 9, 7: 1}, 75))       #-> {1: 48, 3: 22, 7: 5}

