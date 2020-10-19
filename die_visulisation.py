from die import Die
import pygal

#creat a die d6
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
results = []
for roll in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

print(results)

#Analyze the results.
frequencies = []
max_results = die_1.num_sides + die_2.num_sides
for value in range(2, max_results+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

#Visualize the resulits.
hist = pygal.Bar()
hist.title = "Results of two rolling one D6 1000 times"
hist.x_labels = []
for roll_num in range (2,max_results+1):
    hist.x_labels.append(roll_num)

hist.x_title = "Results"
hist._y_title = "Frequency of Results"

hist.add('D6 + D6',frequencies)
hist.render_to_file('die_visual.svg')




