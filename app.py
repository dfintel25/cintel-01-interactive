# Import necessary tools
import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render

# Format the output as a page
ui.page_opts(title="cintel-01-interactive plotting", fillable=True)

# Create sidebar with a slider input for number of bins
with ui.sidebar():
    ui.input_slider(
        "selected_number_of_bins",  # id
        "Number of Bins",           # label
        min=0,                      # min number of bins
        max=200,                    # max number of bins
        value=100                   # initial value
    )

# Create a function to output a histogram
@render.plot(alt="A histogram showing the distribution")
def histogram():
    np.random.seed(19680801)
    x = 100 + 15 * np.random.randn(437)
    plt.hist(
        x,
        bins=input.selected_number_of_bins(),  # number of bins from slider
        density=True                           # normalize histogram
    )
    plt.title("Normalized Histogram")
    plt.xlabel("Value")
    plt.ylabel("Density")

