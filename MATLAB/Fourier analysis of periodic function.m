close all;
clear all;
fs = 1000;
N = 1024;
t = [0:N-1] .* (1/fs);
x = 0.8 .* cos(2 .* pi .* 100 .* t);

subplot(3,1,1);
plot(t, x);
axis([0 0.05 -1 1]);
grid;
xlabel('t');
ylabel('Amplitude');
title('Periodic Input Signal');

x1 = fft(x);
k = 0:N-1;
Xmag = abs(x1);

subplot(3,1,2);
plot(k, Xmag);
grid;
xlabel('t');
ylabel('Amplitude');
title('Magnitude of Periodic FFT Signal');

Xphase = angle(x1) .* (100/pi);

subplot(3,1,3);
plot(k, Xphase);
grid;
xlabel('t');
ylabel('Angle in Degrees');
title('Phase of Periodic FFT Signal');
