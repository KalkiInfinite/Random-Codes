fs = 1000;
fc = 200;
t = (0:1/fs:0.2)';
x = sin(2*pi*30*t) + 2*sin(2*pi*60*t);
fDev = 50;
y = fmmod(x, fc, fs, fDev);

figure;
subplot(2, 1, 1);
plot(t, x);
xlabel('Time (s)');
ylabel('Amplitude');
legend('Original Signal');
grid on;
title('Original Signal');

subplot(2, 1, 2);
plot(t, y);
xlabel('Time (s)');
ylabel('Amplitude');
legend('Modulated Signal');
grid on;