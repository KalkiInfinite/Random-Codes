close all;
clear all;

t = 0:0.001:1;
signal = 0.8 * cos(2 * pi * 100 * t);
noisysig = signal + 1.0 * randn(size(t));

order = 10;
cutofffreq = 20;
samplingfreq = 1000;
[b, a] = butter(order, cutofffreq / (samplingfreq / 2));
filteredsig = filtfilt(b, a, noisysig);

figure;
subplot(3,1,1);
plot(t, signal);
title('Input Signal (Piyush 117)');
subplot(3,1,2);
plot(t, noisysig);
title('Added Noise Signal (Piyush 117)');
subplot(3,1,3);
plot(t, filteredsig);
title('Filtered Signal (Piyush 117)');
grid;