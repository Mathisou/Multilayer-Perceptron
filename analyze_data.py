import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys

def main():
    if len(sys.argv) != 2:
        print("usage: analyze_data.py [dataset]")
    else:
        try:
            data = pd.read_csv(sys.argv[1])
            features = data[["Feature " + str(i) for i in range(data.shape[1] - 3)]]
            print(features)
            result = data.loc[:, "Result"]
            print(result)
            _, ax = plt.subplots(nrows=6, ncols=5, figsize=(15, 18))

            for i, column in enumerate(features.columns):
                row = i // 5
                col = i % 5
                ax[row, col].scatter(result, features[column], label=column)
                ax[row, col].set_title(column)
                # ax[row, col].set_xlabel('Result')
                # ax[row, col].set_ylabel('Feature')

            plt.suptitle('Scatter Plots of Features vs. Result', fontsize=16)
            plt.tight_layout()
            plt.show()

        except FileNotFoundError:
            print(sys.argv[1] + " not found.")


if __name__ == "__main__":
    main()