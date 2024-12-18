Fs = 1000;
t = 0:1/Fs:1;
fc = 100;
fm = 10;
Am = 20;
Am1 = 2;
Am2 = 1;
Ac = 2;

info_signal = Am * sin(2 * pi * fm * t);
info_signal1 = Am1 * sin(2 * pi * fm * t);
info_signal2 = Am2 * sin(2 * pi * fm * t);

carrier_signal = Ac * sin(2 * pi * fc * t);

modulated_signal = ammod(info_signal, fc, Fs, 0, Ac);
modulated_signal1 = ammod(info_signal1, fc, Fs, 0, Ac);
modulated_signal2 = ammod(info_signal2, fc, Fs, 0, Ac);

figure;
subplot(5, 1, 1);
plot(t, info_signal);
title('Information Signal');
xlabel('Time (s)');
ylabel('Amplitude');

subplot(5, 1, 2);
plot(t, carrier_signal);
title('Carrier Signal');
xlabel('Time (s)');
ylabel('Amplitude');

subplot(5, 1, 3);
plot(t, modulated_signal);
title('Amplitude Overmodulation');
xlabel('Time (s)');
ylabel('Amplitude');

subplot(5, 1, 4);
plot(t, modulated_signal1);
title('Amplitude Modulation (Normal Modulation)');
xlabel('Time (s)');
ylabel('Amplitude');

subplot(5, 1, 5);
plot(t, modulated_signal2);
title('Amplitude Undermodulation');
xlabel('Time (s)');
ylabel('Amplitude');