import struct
import sys

import matplotlib.pyplot as plt
import serial


def run(port) -> None:
    with serial.Serial(port=port, baudrate=115200) as ser:

        num_values = 400
        ts = []
        xs = []
        ys = []
        zs = []

        plt.ion()
        fig, ax = plt.subplots()
        (line_x, line_y, line_z) = ax.plot([], [], [], [], [], [])
        plt.title("Monitor")
        plt.xlabel("Time")
        plt.ylabel("Value")
        plt.ylim(-1.2, 1.2)

        while plt.get_fignums():
            data = ser.read(16)
            (t, x, y, z) = struct.unpack("<4f", data)

            if len(ts) < num_values:
                ts.append(t)
                xs.append(x)
                ys.append(y)
                zs.append(z)
            else:
                ts[:-1] = ts[1:]
                ts[-1] = t
                xs[:-1] = xs[1:]
                xs[-1] = x
                ys[:-1] = ys[1:]
                ys[-1] = y
                zs[:-1] = zs[1:]
                zs[-1] = z

            line_x.set_xdata(ts)
            line_x.set_ydata(xs)
            line_y.set_xdata(ts)
            line_y.set_ydata(ys)
            line_z.set_xdata(ts)
            line_z.set_ydata(zs)
            if len(ts) >= 2:
                plt.xlim(ts[0], ts[-1])

            fig.canvas.draw_idle()
            fig.canvas.flush_events()


if __name__ == "__main__":
    if len(sys.argv) == 2:
        run(sys.argv[1])
    else:
        print("Usage: python monitor.py <port>")

