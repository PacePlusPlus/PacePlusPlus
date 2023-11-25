import customtkinter as ctk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



def printReport():
    #test for creating an html file (easiest)

    #test for creating a pdf file 

    # test for creating a Latex --> PDF file for a better formatted pdf 



def createGraph():
    with plt.style.context("DCM\Themes\pine.mplstyle"):
        return create_subplots()



def create_subplots():
    """
    Creates a 2x2 grid of subplots with different types of plots.
    """
    np.random.seed(0)
    fig, ax = plt.subplots(2, 2, figsize=(8, 3))
    
    # Bar plot
    x = np.arange(10)
    y = np.random.rand(10)
    ax[0, 0].bar(x, y)

    # Scatter plot
    x = np.random.rand(100)
    y = np.random.rand(100)
    ax[0, 1].scatter(x, y, s=100)

    # Line plot
    ax[1, 0].plot(np.random.randn(30))

    # Boxplot
    data = [np.random.normal(0, std, size=100) for std in range(1, 4)]
    labels = ['x1', 'x2', 'x3']
    bplot1 = ax[1, 1].boxplot(data,
                     vert=True,  # vertical box alignment
                     patch_artist=True,  # fill with color
                     labels=labels)  # will be used to label x-ticks

    colors = ['pink', 'lightblue', 'lightgreen']
    for patch, color in zip(bplot1['boxes'], colors):
        patch.set_facecolor(color)
    fig.savefig('DCM\Themes\graph.pdf')  # Save the graph
    return fig


root = ctk.CTk()
root.title("CustomTkinter Template")

# Set the size of the window
root.geometry("800x600")

# Create a frame


frame = ctk.CTkScrollableFrame(root)
frame.pack(padx=20, pady=20, fill='both', expand=True)
ctk.CTkLabel(frame, text='Main Body Content', font=('Arial', 16, "bold")).pack()

# Add the graph to the frame
fig = createGraph()
canvas = FigureCanvasTkAgg(fig, master=frame)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(fill='x', expand=True)

# Create a button inside the frame
button = ctk.CTkButton(root, text="Click Me!", command=lambda: print("Button Clicked"))
button.pack(pady=2, padx = 2)

paragraph = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lacinia odio vitae vestibulum. \n Donec in efficitur ipsum, sed dapibus purus. Pellentesque in felis nulla. Curabitur pharetra finibus interdum.\n Sed hendrerit, diam in consequat gravida, eros augue blandit\n nunc, eget faucibus est sapien eget odio. Aenean sed lectus ac magna ultricies cursus\n. Praesent vitae eros eget tellus tristique bibendum. Donec rutrum sed sem\n quis venenatis."
ctk.CTkLabel(frame, text=paragraph, font=('Arial', 11)).pack(anchor="w")





# Start the application
root.mainloop()


