import json

import matplotlib.pyplot as plt

import config


def feature_filter(data):
    feature_filter_dict = {
        "Mult_count": {
            "keep": ["0", "1", "2", "3"],
            "transform": [],
            "other": "4+"
        },
        "Generated Range": {
            "keep": ["[2, 8)", "[8, 32)", "[32, 128)", "[128, 512)"],
            "transform": [
                ["[0.5, 2)", "[1/2, 2)"],
                ["[0.03125, 0.125)", "[0, 1/8)"],
                ["[0.125, 0.5)", "[1/8, 1/2)"],
                ["[512, 2048)", "[512, ~2k)"],
                ["[2048, 8192)", "[~2k, ~8k)"],
            ],
            "other": ">8k"
        },
        "Answer Range": {
            "keep": ["[2, 8)", "[8, 32)", "[32, 128)", "[128, 512)"],
            "transform": [
                ["[0.5, 2)", "[1/2, 2)"],
                ["[0.03125, 0.125)", "[0, 1/8)"],
                ["[0.125, 0.5)", "[1/8, 1/2)"],
                ["[512, 2048)", "[512, ~2k)"],
                ["[2048, 8192)", "[~2k, ~8k)"],
            ],
            "other": ">8k"
        },
        "operation_count": {
            "keep": ["0", "1", "2", "3", "4", "5"],
            "transform": [],
            "other": "6+"
        }
    }

    new_data = {}
    for model, features in data.items():
        new_model_features = {}
        for feature, values in features.items():
            filtered_features = {}
            other_total = 0
            other_correct = 0
            for x, (total, rate) in values.items():
                if x in feature_filter_dict[feature]['keep']:
                    filtered_features[x] = [total, rate]
                    continue
                found_in_transform = False
                for pre_trans, post_trans in feature_filter_dict[feature]['transform']:
                    if x == pre_trans:
                        filtered_features[post_trans] = [total, rate]
                        found_in_transform = True
                        break
                if not found_in_transform:
                    other_total += total
                    other_correct += total * rate

            if other_total != 0:
                filtered_features[feature_filter_dict[feature]['other']] = [other_total,
                                                                            round(other_correct / other_total, 3)]

            new_model_features[feature] = filtered_features
        new_data[model] = new_model_features
    return new_data


def main(regression_method):
    if regression_method == "linear":
        with open(config.analysis_output_dir + 'selected_features.json') as f:
            data = json.load(f)

        data = feature_filter(data)
        order_for_gen_range = ["[0, 1/8)", "[1/8, 1/2)", "[1/2, 2)", "[2, 8)", "[8, 32)", "[32, 128)", "[128, 512)",
                               "[512, ~2k)", "[~2k, ~8k)"]

        shape_val = 2
        plots = {
            "Mult_count": plt.subplot2grid((1 + shape_val * 3, 4), (1, 0), colspan=2, rowspan=shape_val),
            "Generated Range": plt.subplot2grid((1 + shape_val * 3, 4), (1+shape_val, 0), colspan=4, rowspan=shape_val),
            "Answer Range": plt.subplot2grid((1 + shape_val * 3, 4), (1+shape_val*2, 0), colspan=4, rowspan=shape_val),
            "operation_count": plt.subplot2grid((1 + shape_val * 3, 4), (1, 2), colspan=2, rowspan=shape_val),
        }
        feature_title = {
            "Generated Range": "Range of Generated Numbers",
            "Answer Range": "Range of Final Answers",
            "Mult_count": "Count of Multiplications",
            "operation_count": "Count of All Operations"
        }
        plt.tight_layout()
        cur_plot = None
        font_size = 14
        for model, features in data.items():
            for feature, values in features.items():
                cur_plot = plots[feature]
                keys = list(values.keys())
                if feature == "Generated Range":
                    keys = order_for_gen_range
                X = []
                y = []
                for x in keys:
                    (total, rate) = values[x]
                    X.append(x)
                    y.append(rate)
                cur_plot.set_xlabel(feature_title[feature], fontsize=font_size)
                cur_plot.set_ylabel("Accuracy", fontsize=font_size)
                if feature == "Generated Range" or feature == "Answer Range":
                    cur_plot.tick_params(axis='x', which='major', labelrotation=20)
                cur_plot.tick_params(axis='both', which='major', labelsize=font_size)
                cur_plot.plot(X, y, 'o-', label=model)
                cur_plot.grid(True, linestyle='--', alpha=0.6, axis='y')
            # plt.title(model)

        # plt.legend(loc='upper center', ncol=4, bbox_to_anchor=(0.5, 1.05))
        handles, labels = cur_plot.get_legend_handles_labels()
        plt.figlegend(handles, labels, loc='upper center', ncol=4, bbox_to_anchor=(0.5, 0.92), fontsize=font_size)
        plt.show()
