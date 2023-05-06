import tkinter as tk

celestial_bodies = {
"Mercury": 0.378,
"Venus": 0.907,
"Moon": 0.166,
"Mars": 0.377,
"Io": 0.1835,
"Europa": 0.1335,
"Ganymede": 0.1448,
"Callisto": 0.1264
}

# Define the weight allowances for the two types of astronauts
flight_crew_allowance = 100
mission_specialist_allowance = 150

# Define the assumptions for the number of astronauts
num_crew_astronauts = 3
num_mission_specialists = 3

# Define the GUI
root = tk.Tk()
root.title("Astronaut Mass Calculator")

# Create labels for the celestial bodies and their mass multipliers
celestial_body_label = tk.Label(root, text="Celestial Body")
celestial_body_label.grid(row=0, column=0)

mass_multiplier_label = tk.Label(root, text="Mass Multiplier")
mass_multiplier_label.grid(row=0, column=1)

# Create a label to display the personal mass allowances
personal_mass_label = tk.Label(root, text="Available Personal Mass")
personal_mass_label.grid(row=0, column=2)


# Create a listbox to display the celestial bodies and their mass multipliers
celestial_body_listbox = tk.Listbox(root)
for body, multiplier in celestial_bodies.items():
    celestial_body_listbox.insert(tk.END, f"{body} ({multiplier})")
    celestial_body_listbox.grid(row=1, column=0)

# Create labels for the weight allowances for the two types of astronauts
flight_crew_label = tk.Label(root, text=f"Crew : {flight_crew_allowance} kg")
flight_crew_label.grid(row=2, column=0)

mission_specialist_label = tk.Label(root, text=f"Mission Specialist: {mission_specialist_allowance} kg")
mission_specialist_label.grid(row=3, column=0)

# Create entry fields for the mass of each astronaut
crew_mass_entries = []
for i in range(num_crew_astronauts):
    label = tk.Label(root, text=f"Crew Astronaut {i+1} Mass (kg)")
    label.grid(row=i+4, column=0)
    entry = tk.Entry(root)
    entry.grid(row=i+4, column=1)
    crew_mass_entries.append(entry)

specialist_mass_entries = []
for i in range(num_mission_specialists):
    label = tk.Label(root, text=f"Mission Specialist {i+1} Mass (kg)")
    label.grid(row=i+4+num_crew_astronauts, column=0)
    entry = tk.Entry(root)
    entry.grid(row=i+4+num_crew_astronauts, column=1)
    specialist_mass_entries.append(entry)

crew_personal_mass_labels = []
for i in range(num_crew_astronauts):
    label = tk.Label(root, text=f"{i+1}: ")
    label.grid(row=i+1, column=2)
    crew_personal_mass_labels.append(label)

specialist_personal_mass_labels = []
for i in range(num_mission_specialists):
    label = tk.Label(root, text=f"{i+1}: ")
    label.grid(row=i+1+num_crew_astronauts, column=2)
    specialist_personal_mass_labels.append(label)

# Create a label to display the results
result_label = tk.Label(root)
result_label.grid(row=4+num_crew_astronauts+num_mission_specialists+1, column=1)

# Get the selected celestial body and its mass multiplier
def calculate():
    if not celestial_body_listbox.curselection():
        result_label.config(text="Please select a celestial body.")
        result_label.grid(row=4+num_crew_astronauts+num_mission_specialists+1, column=1)
        return
    selected_body = celestial_body_listbox.get(celestial_body_listbox.curselection())
    selected_body = selected_body.split(" ")[0]
    selected_multiplier = celestial_bodies[selected_body]
    
    # Check if all mass entries are valid numbers
    for entry in crew_mass_entries + specialist_mass_entries:
        if entry.get():
            try:
                float(entry.get())
            except ValueError:
                result_label.config(text="Please enter valid numbers for astronaut masses.")
                result_label.grid(row=4+num_crew_astronauts+num_mission_specialists+1, column=1)
                return
    
    total_mass = 0
    for entry in crew_mass_entries + specialist_mass_entries:
        if entry.get():
            total_mass += float(entry.get())
    total_mass *= selected_multiplier
    
    # Check if the total mass exceeds the total mass allowance
    if total_mass > (flight_crew_allowance * num_crew_astronauts) + (mission_specialist_allowance * num_mission_specialists):
        result_label.config(text="Total mass exceeds total mass allowance.")
        result_label.grid(row=4+num_crew_astronauts+num_mission_specialists+1, column=1)
        return
    
    crew_mass_allowance = flight_crew_allowance * num_crew_astronauts
    specialist_mass_allowance = mission_specialist_allowance * num_mission_specialists
    total_mass_allowance = crew_mass_allowance + specialist_mass_allowance
    personal_mass_allowance = total_mass_allowance - total_mass
    avg_personal_mass_allowance = personal_mass_allowance / (num_crew_astronauts + num_mission_specialists)

    # Calculate the personal mass allowance for each astronaut
    crew_personal_mass = []
    for i, entry in enumerate(crew_mass_entries):
        if entry.get():
            crew_mass = float(entry.get())
            personal_mass = flight_crew_allowance - crew_mass
            crew_personal_mass.append(personal_mass)
            crew_personal_mass_labels[i].config(text=f"{i+1}: {personal_mass:.2f} kg")

    specialist_personal_mass = []
    for i, entry in enumerate(specialist_mass_entries):
        if entry.get():
            specialist_mass = float(entry.get())
            personal_mass = mission_specialist_allowance - specialist_mass
            specialist_personal_mass.append(personal_mass)
            specialist_personal_mass_labels[i].config(text=f"{i+1}: {personal_mass:.2f} kg")

    # Calculate the weight of the average available personal mass allowance on the selected celestial body
    avg_personal_mass_allowance_weight = avg_personal_mass_allowance / selected_multiplier

    # Display the results
    result_label.config(text=f"Total Available Mass: {total_mass:.2f} kg\n"
                            f"Personal Mass Allowance: {personal_mass_allowance:.2f} kg\n"
                            f"Avg Personal Mass Allowance: {avg_personal_mass_allowance:.2f} kg\n"
                            f"Avg Personal Mass Allowance Weight: {avg_personal_mass_allowance_weight:.2f} kg")
    result_label.grid(row=1, column=1)


# Create a button to calculate the results
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=4+num_crew_astronauts+num_mission_specialists, column=0)


# Exit the program
exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.grid(row=17, column=2)

# Create a label to display the results
result_label = tk.Label(root)
result_label.grid(row=1, column=1)

root.mainloop()