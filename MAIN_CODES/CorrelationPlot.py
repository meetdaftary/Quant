import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class CorrelationMatrixPlotter:

    def __init__(self, data):

        self.data = data

    # def _print_highest_correlation_pairs(self, correlation_matrix):
    #     # Unstack the correlation matrix into a Series
    #     corr_pairs = correlation_matrix.unstack()

    #     # Filter out self-correlations
    #     corr_pairs = corr_pairs[corr_pairs.index.get_level_values(0) != corr_pairs.index.get_level_values(1)]

    #     # Sort pairs by absolute correlation value in descending order
    #     sorted_pairs = corr_pairs.abs().sort_values(ascending=False)

    #     # Display the top correlated pairs
    #     print("Top correlated pairs:")
    #     print(sorted_pairs.head(10))


    def plot_correlation_matrix(self, title):

        self.data.dropna(inplace=True)
        returns = self.data.pct_change().dropna()
        x=self.data.shape[1]

        correlation_matrix = returns.corr()
        figsize=(100,80)
        annot_size=5
        plt.figure(figsize=figsize)
        sns.heatmap(
            correlation_matrix, 
            annot=True, 
            fmt=".2f", 
            cmap="coolwarm", 
            cbar=True,
            square=True, 
            linewidths=0.5, 
            annot_kws={"size": annot_size}
        )
        plt.title(title, fontsize=16)
        plt.xticks(fontsize=10, rotation=45)
        plt.yticks(fontsize=10, rotation=0)
        plt.tight_layout()

        plt.show()

        s = correlation_matrix.unstack()
        so = s.sort_values(ascending=False, kind="quicksort")
        filtered_so = so.iloc[x::2]
        print("HIGH CORRELATION") 
        print(filtered_so.head(5))
        print("LOW CORRELATION") 
        print(filtered_so.tail(5))

        # self._print_highest_correlation_pairs(correlation_matrix)



