import json

class NumberAnalyzer:
    def __init__(self,numbers):
        self.numbers = numbers
    def get_positive_negative(self):
        positive_sum = sum(num for num in self.numbers if num >=0)
        negatives = [num for num in self.numbers if num<0]
        return positive_sum,negatives
    def get_odd_even(self):
        odd = [num for num in numbers if num % 2 !=0]
        even = [num for num in numbers if num %2 ==0]
        return odd,even

    def analyze(self):
        positive_sum,negatives = self.get_positive_negative()
        odd , even = self.get_odd_even()
        summary = self.get_summary()
        return{
            "positive_sum" :positive_sum,
            "negatives":negatives,
            "odd":odd,
            "even":even,
            "summary":summary
        }
    def get_total_count(self):
        return len(self.numbers)
    def get_total_negativecount(self):
        return len([num for num in self.numbers if num<0])
    def get_summary(self):
        total = self.get_total_count()
        negatives = self.get_total_negativecount()
        return f"Total numbers : {total}, Negatives numbers : {negatives}"
    

def get_numbers_api(numbers):
    analyzer = NumberAnalyzer(numbers)
    result = analyzer.analyze()
    return json.dumps(result, indent=1)

numbers = [1,-2,-5,2,6,4,7,3,7]
print(get_numbers_api(numbers))