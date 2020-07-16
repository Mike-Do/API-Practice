# Note: Notation is as follows for a die: D[Num_Sides]
# So, a six-sided die is a D6.
from die import Die

import pygal

# Create two D6 dice.
die_1 = Die()
die_2 = Die()
# Make some rolls, and store result in a list.
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency =  results.count(value)
    frequencies.append(frequency)

# Visualize the results with a histogram.
hist = pygal.Bar()

hist.title = "Results of Rolling two D6 dice 1000 Times"
hist.labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('die_visual.svg')

print(frequencies)

