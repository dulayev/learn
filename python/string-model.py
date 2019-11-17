
import matplotlib.pyplot as plt
import matplotlib.animation
import time

import math

steel_young_modulus = 210e9 # steel
string_len = 0.627
string_diameter = 0.15e-3
string_section_area = math.pi * (string_diameter ** 2) / 4
theory_coeff_firm = string_section_area * steel_young_modulus / string_len
# print(f"Коэфф. упругости из справочника: {theory_coeff_firm}")

exp_string_len = string_len / 2
exp_string_dev = 3e-3
exp_string_stretched = math.sqrt(exp_string_dev**2 + exp_string_len**2)
exp_string_ext = exp_string_stretched - exp_string_len


sin_alpha = exp_string_dev / exp_string_stretched
gravity_const = 9.81
exp_mass = 0.117
exp_strength = gravity_const * exp_mass / (2 * sin_alpha)

exp_coeff_firm = exp_strength / exp_string_ext

# print(f"Экспериментальный коэффициент упругости: {exp_coeff_firm}")

N = 1000
y = [0]*N
part_of_pulling_string = 0.2
max_pull = 0.01 #10 мм

#первая часть

number_of_pieces_1_part = int(N * part_of_pulling_string) 
little_y = max_pull/number_of_pieces_1_part

for i in range(1, number_of_pieces_1_part + 1):
    y[i] = little_y*i

#вторая часть
part_of_pulling_string_2 = 1 - part_of_pulling_string
number_of_pieces_2_part = N - number_of_pieces_1_part
#1000*(part_of_pulling_string_2)
little_y = max_pull / (number_of_pieces_2_part - 1)

for i in range(number_of_pieces_1_part + 1, N):
    y[i] = max_pull-little_y*(number_of_pieces_2_part-(N-i))

vy = [0]*N
next_y = [0]*N
delta_t = 1e-5 # 10 microseconds
delta_x = string_len / (N - 1)
mass = 1e-3 # 1 gramm

def calc_sin(dx, dy):
    return dy / math.sqrt(dx * dx + dy * dy)

def update(step):
    global y
    stretched_len = sum([math.sqrt((y[i+1] - y[i])**2 + delta_x**2) for i in range(N-1)])
    max_abs_y = max(map(abs, y))
    print(f"{step} L: {stretched_len} Ymax: {max_abs_y}")
    for i in range(1, N - 1):
        delta_y_left = y[i] - y[i-1]
        delta_y_right = y[i + 1] - y[i]
        sin_left = calc_sin(delta_x, delta_y_left)
        sin_right = calc_sin(delta_x, delta_y_right)
        strength = exp_coeff_firm * (stretched_len - string_len) / N
        a = strength * (sin_right - sin_left) / (mass / N)
        next_y[i] = y[i] + vy[i] * delta_t + a * delta_t * delta_t / 2
        vy[i] += a * delta_t
    y = next_y.copy()
    line.set_ydata(y)

plt.ion()
xdata = [i * string_len / (N - 1) for i in range(N)]
ydata = y
axes = plt.gca()
axes.set_xlim(0, string_len)
axes.set_ylim(-max_pull, max_pull)
line, = axes.plot(xdata, ydata, 'r-')

ani = matplotlib.animation.FuncAnimation( \
    plt.gcf(), update, frames=30, interval=200, repeat=False)
