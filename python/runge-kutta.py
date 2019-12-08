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


def SimpleStringFunction(t, Y):
    FY = [0] * len(Y)
    FY[0] = Y[1]
    l = 0.5;
    delta_l = math.sqrt(l * l + Y[0] * Y[0]) - l;
    k = 600;
    strength = k * delta_l;
    m = 0.001;
    FY[1] = -2 * strength * Y[0] / (m * l);
    return FY

dt = 1e-6;
# Определим начальные условия y(0)=0, y'(0)=1 задачи
Y0 = [ 0.1, 0 ];
# Установим начальные условия задачи
task = RungeKutta(0.0, Y0, SimpleStringFunction);
# решаем до 15 секунд
count = 0
min = 0
max = 0
while (task.t <= 15):
    if (max < task.Y[0]):
        max = task.Y[0]
    if (min > task.Y[0]):
        min = task.Y[0]
    if (count % 1000000 == 0):
        print("Time = {0} Func = {1} d Func / d x = {2}".format(task.t, task.Y[0], task.Y[1]))
        print("Time = {0:.5f} Min = {1}, Max = {2:.8f}".format(task.t, min, max))
        min = max = 0
    # рассчитать на следующем шаге, шаг интегрирования 
    task.NextStep(dt)
    count += 1
