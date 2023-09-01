# The question was very straightforward in my opinion, and they'd give one after the other. I think it was too easy, except it wasn't clear what they were looking for.

# feature1 : string categorical
# feature2 : numeric
# feature3 : numeric categorical
# feature4 : string splittable
# feature5 : string
# Q1 : Store this in some python data structure.
# Q2 : Write a function that accepts a tag and returnsall features that match it.

# def find_feature(tag : str) -> List[str]:
# 	...

# find_feature("string") -> feature1, feature4, feature5
# Q3 : Write a function that accepts tags and returns all features that can have any one of them.

# 		find_feature("categorical", "splittable") -> feature1, feature3, feature4
# Q4: Write a function that accepts tags and returns all features that can have all of them.

# 		find_feature("categorical", "string") -> feature1

from collections import defaultdict


class Solution:
    def __init__(self) -> None:
        self.tags_dict = defaultdict(list)

    def add(self, feature_tags):
        feature_tags_list = feature_tags.split("\n")
        for feature_tag in feature_tags_list:
            feature_meta = feature_tag.split(":")
            self.tags_dict[feature_meta[0]
                           ] = feature_meta[1].strip().split(" ")
        return self.tags_dict

    def find_feature_by_tag(self, tag):
        features = []
        for feature, tags in self.tags_dict.items():
            if tag in tags:
                features.append(feature)
        return features


solution = Solution()
feature_tag1 = "feature1: string category \n feature2: int \n feature3: string"
print(solution.add(feature_tag1))
print(solution.find_feature_by_tag('string'))
