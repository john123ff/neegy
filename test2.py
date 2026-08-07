# TODO 1: Import the pyplot module from the matplotlib library as 'plt'
import matplotlib.pyplot as plt

def create_plots():


    # Hardcoded 7-day data for our plots
    days = [1, 2, 3, 4, 5, 6, 7]
    temperature = [22, 24, 19, 23, 26, 28, 25]
    rainfall = [5, 2, 10, 0, 1, 0, 4]

    # TODO 2: Set up the figure and subplots (2 row, 2 columns)
    fig, axs = plt.subplots(2, 2)

    # TODO 3: Top-Left Plot (Temperature): Plot 'days' (x) and 'temperature' (y) on the first subplot (color 'red')
    x_values = [1, 2, 3]
    y1_values = [10, 20, 30]
    y2_values = [5, 15, 25]

    # TODO 4: Top-Right Plot (Rainfall): Plot days vs. rainfall.
    axs[0, 0].plot(days, rainfall, color='blue')  # Adding color
    axs[0, 0].set_title("Rainfall")               # Adding a title
    axs[0, 0].set_xlabel("Days")                        # Adding X label
    axs[0, 0].set_ylabel("Amount")                       # Adding Y label


    # TODO 5: Bottom-Left Plot (Humidity): Create your own fake data list for humidity (5 numbers). Plot days vs. humidity.
    axs[0, 1].plot(days, [20, 25, 30, 35, 40], color='orange')  # Adding color
    axs[0, 1].set_title("Humidity")               # Adding a title
    axs[0, 1].set_xlabel("Days")                         # Adding X label
    axs[0, 1].set_ylabel("Percentage")                     # Adding Y label

    # TODO 6: Bottom-Right Plot (Wind Speed): Create your own fake data list for wind_speed (5 numbers).
    # Plot days vs. wind_speed. Combine customizations: use a unique color, a dotted line style (':'). Add headers.
    axs[1, 0].plot(days, [10, 15, 20, 25, 30], color='green', linestyle=':')  # Adding color and line style
    axs[1, 0].set_title("Wind Speed")               # Adding a title
    axs[1, 0].set_xlabel("Days")                         # Adding X label
    axs[1, 0].set_ylabel("Speed")                     # Adding Y label

    # TODO 9: Display the plots neatly to the screen
    plt.tight_layout()
    plt.show()
    # pass # Remove this 'pass' once you start writing your code

    # This block runs the code when the script is executed
    if __name__ == "__main__":
        create_plots()