import math
from copy import copy

import util
import config


class FeatureMap:
    default_map = {}
    default_keys = []
    question_id = 0

    @staticmethod
    def reinit():
        with open(config.analysis_output_dir + 'features.txt') as f:
            features = f.read().split('\n')
        features.sort()
        for feature in features:
            FeatureMap.default_map[feature] = 0
            FeatureMap.default_keys.append(feature)

    def __init__(self, add_new=True):
        self.feature_map = copy(FeatureMap.default_map)
        self.feature_id_map = copy(FeatureMap.default_map)
        self.id_question_map = dict()
        for key, value in self.feature_id_map.items():
            # For feature f, consists of list of tuples: (question_id, feature_value, correct_model)
            self.feature_id_map[key] = []
        self.add_new = add_new
        self.id = None

    def obtain_id(self, question):
        self.id = FeatureMap.question_id
        FeatureMap.question_id += 1
        self.id_question_map[self.id] = question
        self.feature_map = copy(FeatureMap.default_map)
        return self.id

    def add_to_feature_id_map(self, new_id, features, correctness):
        assert new_id == self.id
        for feature_name, feature_val in zip(FeatureMap.default_keys, features):
            if feature_val != 0:
                self.feature_id_map[feature_name].append((self.id, feature_val, correctness))

    def add_feature(self, feature_name, feature_value):
        if feature_name in self.feature_map:
            self.feature_map[feature_name] += feature_value
        else:
            if self.add_new:
                self.feature_map[feature_name] = feature_value
            else:
                raise NotImplementedError(f'Unseen feature: {feature_name}')

    def create_feature_vector(self):
        res = []
        for key in FeatureMap.default_keys:
            res.append(self.feature_map[key])

        return res

    def add_value_to_feature(self, value, prefix=""):
        if util.is_int(value):
            self.add_feature(f'{prefix}_int_num', 1)
        else:
            self.add_feature(f'{prefix}_float_num', 1)
        if util.is_same_num(value, 0):
            self.add_feature(f'{prefix}_is_zero', 1)
            return
        if value < 0.0:
            self.add_feature(f'{prefix}_is_negative', 1)
            value = -value
        log_4 = math.log(value, 4.0)
        if log_4 > 10.0:
            log_4 = 10
        if log_4 < -3.0:
            log_4 = -3
        self.add_feature(f'{prefix}_log_4_val_{round(log_4)}', 1)