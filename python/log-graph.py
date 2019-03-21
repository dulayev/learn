import matplotlib.pyplot as plt

pattern = "SomeFunction"

with open("C:\\sources\\logcat.log") as f:
	lines = f.readlines()

interval = None
freqs = []
counter = 0

for line in lines:
	try:
		cur_interval = float(line[12:16])
	except ValueError:
		continue
	if interval != cur_interval:
		if interval != None:
			freqs.append((interval, counter))
		interval = cur_interval
		counter = 0
	if line.find(pattern) >= 0:
		counter += 1

print(len(freqs))
args = [i[0] for i in freqs]
values = [i[1] for i in freqs]
plt.plot(args, values)
plt.show()
