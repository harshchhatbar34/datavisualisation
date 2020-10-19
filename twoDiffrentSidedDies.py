from die import Die
import pygal

#creat a die D6 and D10
die_1 = Die()
die_2 = Die(10)

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
hist.title = "Results of two rolling one D6 and one D10 1000 times"
hist.x_labels = ['2', '3', '4', '5', '6', '7','8', '9', '10', '11', '12', '13', '14', '15', '16']
hist.x_title = "Results"
hist._y_title = "Frequency of Results"

hist.add('D6 + D10',frequencies)
hist.render_to_file('die_visual.svg')




