
import matplotlib.pyplot as plt
import matplotlib.animation
import time
import math

class RungeKutta:
    def __init__(self, t0, Y0, F):
        self.t = t0
        self.f = F
        N = len(Y0)
        self.Y = list(Y0) # deep for one level
        self.YY = [0] * N
        self.Y1 = [0] * N
        self.Y2 = [0] * N
        self.Y3 = [0] * N
        self.Y4 = [0] * N

    def NextStep(self, dt):
            if (dt < 0):
                return

            # рассчитать self.Y1
            self.Y1 = self.f(self.t, self.Y);

            N = len(self.Y)
            for i in range(N):
                self.YY[i] = self.Y[i] + self.Y1[i] * (dt / 2.0);

            # рассчитать self.Y2
            self.Y2 = self.f(self.t + dt / 2.0, self.YY);

            for i in range(N):
                self.YY[i] = self.Y[i] + self.Y2[i] * (dt / 2.0);

            # рассчитать self.Y3
            self.Y3 = self.f(self.t + dt / 2.0, self.YY);

            for i in range(N):
                self.YY[i] = self.Y[i] + self.Y3[i] * dt;

            # рассчитать self.Y4
            self.Y4 = self.f(self.t + dt, self.YY);

            # рассчитать решение на новом шаге
            for i in range(N):
                self.Y[i] = self.Y[i] + dt / 6.0 * (self.Y1[i] + 2.0 * self.Y2[i] + 2.0 * self.Y3[i] + self.Y4[i]);

            #print(self.Y, self.YY, self.Y1, self.Y2, self.Y3, self.Y4)

            # рассчитать текущее время
            self.t = self.t + dt;

def find_circle(points):
    ((x0, y0), (x1, y1), (x2, y2)) = points
    
    def find_line(x0, x1, y0, y1):
        a = x1 - x0
        b = y1 - y0
        c = (a * (x1 + x0) + b * (y1 + y0)) / 2
        return a, b, c

    al, bl, cl = find_line(x0, x1, y0, y1)
    ar, br, cr = find_line(x1, x2, y1, y2)

    det = al * br - ar * bl
    if abs(det) < 1e-10:
        return None
    x = (cl * br - cr * bl) / det
    y = (al * cr - ar * cl) / det
    r = math.sqrt((x - x1) **2 + (y - y1) **2)
    return x, y, r

def test_find_circle():
    xc, yc = 8, 5
    radius = 4
    points = [(xc + radius * math.sin(alpha), yc + radius * math.cos(alpha)) \
              for alpha in [0.5, 1.2, 2.0]]
    xc2, yc2, radius2 = find_circle(points)
    assert(xc == round(xc2, 7))
    assert(yc == round(yc2, 7))
    assert(radius == round(radius2, 7))

steel_young_modulus = 210e9 # steel
string_len = 0.627
string_diameter = 0.15e-3
string_section_area = math.pi * (string_diameter ** 2) / 4
theory_coeff_firm = string_section_area * steel_young_modulus / string_len
print(f"Коэфф. упругости из справочника: {theory_coeff_firm}")

exp_string_len = string_len / 2
exp_string_dev = 3e-3
exp_string_stretched = math.sqrt(exp_string_dev**2 + exp_string_len**2)
exp_string_ext = exp_string_stretched - exp_string_len


sin_alpha = exp_string_dev / exp_string_stretched
gravity_const = 9.81
exp_mass = 0.117
exp_strength = gravity_const * exp_mass / (2 * sin_alpha)

exp_coeff_firm = exp_strength / exp_string_ext

print(f"Экспериментальный коэффициент упругости: {exp_coeff_firm}")

N = 100
y = [0]*N
part_of_pulling_string = 0.2
max_pull = 0.01 #10 mm
finger_radius = 0.05 #50 mm
finger_x = part_of_pulling_string * string_len

def find_touch_point(cx, cy, radius):
    center_distance2 = cx**2 + cy**2
    point_distance = math.sqrt(center_distance2 - radius**2)
    cos_sum = (point_distance * cx - radius * cy) / center_distance2
    sin_sum = (point_distance * cy + radius * cx) / center_distance2
    return (point_distance * cos_sum, point_distance * sin_sum)

left_touch_point = find_touch_point(finger_x, max_pull, finger_radius)
right_touch_point = find_touch_point(string_len - finger_x, max_pull, finger_radius)

delta_x = string_len / (N - 1)

for i in range(N):
    x = i * delta_x
    if x < left_touch_point[0]:
        y[i] = left_touch_point[1] * x / left_touch_point[0]
    elif x > string_len - right_touch_point[0]:
        y[i] = right_touch_point[1] * (string_len - x) / right_touch_point[0]
    else:
        y[i] = max_pull + math.sqrt(finger_radius**2 - (finger_x - x)**2)

vy = [0]*N
delta_t = 1e-6 # 1 microsecond
mass = 1e-3 # 1 gramm

def diff_function(t, y):
    FV = y[N:] # copy second part as a dF/dt
    FA = [0] * N
    stretched_len = sum([math.sqrt((y[i+1] - y[i])**2 + delta_x**2) for i in range(N-1)])
    #max_abs_y = max(map(abs, y))
    #print(f"{step} L: {stretched_len} Ymax: {max_abs_y}")
    for i in range(1, N - 1):
        delta_y_left = y[i] - y[i-1]
        delta_y_right = y[i + 1] - y[i]
        sin_left = calc_sin(delta_x, delta_y_left)
        sin_right = calc_sin(delta_x, delta_y_right)
        strength_stretch = theory_coeff_firm * (stretched_len - string_len) / N

        x = i * delta_x
        points = [(x - delta_x, y[i - 1]), (x, y[i]), (x + delta_x, y[i + 1])]

        strength_bend = 0.0

        res = find_circle(points)
        if res != None:
            circle_x, circle_y, radius = res
            strength_bend_abs = (steel_young_modulus * math.pi * string_diameter**4) / \
                                (radius * 64 * delta_x)
            strength_bend = math.copysign(strength_bend_abs, y[i] - circle_y)
        
        FA[i] = (strength_stretch * (sin_right - sin_left) + strength_bend) / (mass / N)

    return FV + FA

task = RungeKutta(0.0, y + vy, diff_function)

def calc_sin(dx, dy):
    return dy / math.sqrt(dx * dx + dy * dy)

def update(step):
    for _ in range(100):
        task.NextStep(delta_t)
    line.set_ydata(task.Y[0:N])
    plt.savefig(f"c:\\images\\string-{step:05d}.png")
    # convert to video with:
    # ffmpeg.exe -framerate 30 -i string-%05d.png -vf format=yuv420p string.mp4

plt.ion()
xdata = [i * string_len / (N - 1) for i in range(N)]
ydata = y
axes = plt.gca()
axes.set_xlim(0, string_len)
axes.set_ylim(-max_pull - finger_radius, max_pull + finger_radius)
line, = axes.plot(xdata, ydata, 'r-')

ani = matplotlib.animation.FuncAnimation( \
    plt.gcf(), update, frames=1200, interval=1, repeat=False)
