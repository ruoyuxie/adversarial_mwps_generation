import json

import pandas as pd
import statsmodels.api as sm
from sklearn.linear_model import LogisticRegression

import question_parse
from problem_solving_tree import FeatureMap
import config


def linear_regression(column_names, feature_names, data):
    column_names += ['Target', 'const']

    x = [feature for feature, _ in data]
    y = [1 if res else 0 for _, res in data]

    all_data = [x + [_y, 1] for x, _y in zip(x, y)]
    df = pd.DataFrame(all_data, columns=column_names)

    x = pd.DataFrame()
    interested = []
    for column_name in df.columns:
        if column_name == "Target":
            continue
        if column_name in feature_names:
            x[feature_names[column_name]] = df[column_name]
            interested.append(feature_names[column_name])
        else:
            x[column_name] = df[column_name]

    y = df["Target"]

    est = sm.OLS(y, x)
    est2 = est.fit()
    with open(config.analysis_output_dir + 'coef_list.txt', 'w') as f:
        f.write(str(est2.summary()))


def logistic_regression(data):
    x = [feature for feature, _ in data]
    y = [1 if res else 0 for _, res in data]

    clf = LogisticRegression(random_state=0, max_iter=1000).fit(x, y)

    coef = clf.coef_[0]

    FeatureMap.reinit()
    feature_names = FeatureMap.default_keys

    assert len(coef) == len(feature_names)

    name_coef_map = list(zip(feature_names, coef))
    name_coef_map.sort(key=lambda x: x[1], reverse=True)

    output_string = ""
    for name, coef_val in name_coef_map:
        output_string += f'{name}: {coef_val}\n'

    with open(config.analysis_output_dir + 'coef_list.txt', 'w') as f:
        f.write(output_string)


def regression_main(method="logistic"):
    question_parse.process_features()

    with open(config.analysis_output_dir + 'feature_vectors.txt') as f:
        data = json.load(f)

    with open(config.analysis_output_dir + 'features.txt') as f:
        column_names = f.read().split('\n')

    with open('src/feature_renaming.json') as f:
        feature_names = json.load(f)

    if method == "logistic":
        logistic_regression(data)
    elif method == "linear":
        linear_regression(column_names, feature_names, data)
