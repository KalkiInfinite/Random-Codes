import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

# Data in CSV format
data = """Time (seconds),Servo 1 Position (degrees),Servo 2 Position (degrees),Servo 3 Position (degrees)
0,-90,0,90
1,-85.5,4.5,82.5
2,-81,9,75
3,-76.5,13.5,67.5
4,-72,18,60
5,-67.5,22.5,52.5
6,-63,27,45
7,-58.5,31.5,37.5
8,-54,36,30
9,-49.5,40.5,22.5
10,-45,45,15
11,-40.5,40.5,7.5
12,-36,36,0
13,-31.5,31.5,-7.5
14,-27,27,-15
15,-22.5,22.5,-22.5
16,-18,18,-30
17,-13.5,13.5,-37.5
18,-9,9,-45
19,-4.5,4.5,-52.5
20,0,0,-60
21,4.5,-4.5,-67.5
22,9,-9,-75
23,13.5,-13.5,-82.5
24,18,-18,-90
25,22.5,-22.5,-82.5
26,27,-27,-75
27,31.5,-31.5,-67.5
28,36,-36,-60
29,40.5,-40.5,-52.5
30,45,-45,-45
"""
df = pd.read_csv(StringIO(data))
plt.figure(figsize=(10, 6))

plt.plot(df['Time (seconds)'], df['Servo 1 Position (degrees)'], label='Servo 1', marker='o', linestyle='-', color='blue')
plt.plot(df['Time (seconds)'], df['Servo 2 Position (degrees)'], label='Servo 2', marker='s', linestyle='-', color='green')
plt.plot(df['Time (seconds)'], df['Servo 3 Position (degrees)'], label='Servo 3', marker='^', linestyle='-', color='orange')
plt.title('Servo Positions Over Time', fontsize=16)
plt.xlabel('Time (seconds)', fontsize=14)
plt.ylabel('Position (degrees)', fontsize=14)
plt.axhline(0, color='gray', linewidth=0.5, linestyle='--') 
plt.legend(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tick_params(axis='both', which='major', labelsize=12)
plt.tick_params(axis='both', which='minor', labelsize=10)
plt.tight_layout()
plt.show()
