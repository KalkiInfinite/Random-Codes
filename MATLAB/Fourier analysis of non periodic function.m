close all;
clear all;
fs = 15000;
ts = 1/fs;
tpulse = 10e-3;
f1 = 83;
f2 = 5800;
N = 20;
t = 0:ts:tpulse;
y = chirp(t, f1, t(end), f2);

subplot(3,1,1);
plot(t, y);
grid;
xlabel('t');
ylabel('Amplitude');
title('Non-Periodic Input Signal');

x1 = fft(y);
Xmag = abs(x1);

subplot(3,1,2);
plot(t, Xmag);
grid;
xlabel('t');
ylabel('Amplitude');
title('Magnitude of Non-Periodic FFT Signal');

Xphase = angle(x1) .* (100/pi);

subplot(3,1,3);
plot(t, Xphase);
grid;
xlabel('t');
ylabel('Angle in Degrees');
title('Phase of Non-Periodic FFT Signal');
