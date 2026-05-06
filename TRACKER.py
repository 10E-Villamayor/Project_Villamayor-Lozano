from pyscript import display, document # pyright: ignore[reportMissingImports]
import numpy as np
import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)

import matplotlib.pyplot as plt
#  removing font cache msg
plt.figure()
plt.plot([0, 1], [0, 1])
plt.close()

days = np.array(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
absences = np.zeros(5)

def generate_graph():
    document.getElementById("plot-target").innerHTML = ""
    plt.figure(figsize=(7, 4))
    
    plt.plot(days, absences, marker='o', color="#6dab82", linewidth=2)
    
    plt.title('Weekly Attendance (Absences)')
    plt.xlabel('Day')
    plt.ylabel('Number of Absences')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.ylim(bottom=0)

    display(plt.gcf(), target="plot-target")
    plt.close()

def update_data(event):
    day_idx = int(document.getElementById("day-select").value)
    val = document.getElementById("absence-input").value
    
    if val:
        absences[day_idx] = int(val)
        document.getElementById("absence-input").value = ""
        generate_graph()

generate_graph()