#Import necessary tools
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from shiny.express import ui, input, render
from matplotlib import cm
from matplotlib.colors import Normalize

# Format the output as a page
ui.page_opts(title="cintel-01-interactive, version 2!", fillable=True)

# Reactive histogram plot with gradient coloring
@render.plot(alt="Histogram with gradient coloring")
def histogram():
    np.random.seed(19680801)
    x = 100 + 15 * np.random.randn(437)

    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 5))

    # Get histogram data
    counts, bin_edges = np.histogram(
        x, bins=input.selected_number_of_bins(), density=True
    )
    bin_centers = 0.5 * (bin_edges[1:] + bin_edges[:-1])

    # Normalize the bin center values for color mapping
    norm = Normalize(vmin=min(bin_centers), vmax=max(bin_centers))
    cmap = cm.get_cmap('RdYlGn')  # Red to green

    # Plot each bar with a color based on its bin center value
    for count, left, right, center in zip(counts, bin_edges[:-1], bin_edges[1:], bin_centers):
        plt.bar(
            x=left,
            height=count,
            width=right - left,
            align='edge',
            color=cmap(norm(center)),
            edgecolor='black',
            alpha=0.8
        )

    # Optional Kernel Density Estimation "KDE" overlay
    if input.show_kde():
        sns.kdeplot(x, color="blue", linewidth=1)

    plt.title(f"Normalized Histogram ({input.selected_number_of_bins()} Bins)")
    plt.xlabel("Value")
    plt.ylabel("Density")
    plt.grid(True)
    plt.tight_layout()

# Sidebar for inputs
with ui.sidebar():
    ui.input_slider(
        "selected_number_of_bins", "Number of Bins",
        min=5, max=100, value=20
    )
    ui.input_checkbox("show_kde", "Show KDE (Density Curve)", value=False)
