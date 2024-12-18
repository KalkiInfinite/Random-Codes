clear all;
close all;

% Time vector
t = -200:0.01:200;

% Load the ECG signal
load('0001m.mat'); 
ecg_signal = val(1, :); % Extracting the ECG signal from loaded data

% Original ECG Signal
subplot(2, 2, 1);
plot(ecg_signal);
title('Original ECG Signal');
xlabel('Samples');
ylabel('Amplitude');

% Amplitude scaling: Multiplication
subplot(2, 2, 2);
plot(ecg_signal * 2);
title('Amplitude Scaling: Multiplication');
xlabel('Samples');
ylabel('Amplitude');

% Amplitude scaling: Division
subplot(2, 2, 3);
plot(ecg_signal / 2);
title('Amplitude Scaling: Division');
xlabel('Samples');
ylabel('Amplitude');

% Inverse of ECG Signal
subplot(2, 2, 4);
plot(-ecg_signal);
title('Inverse of ECG Signal');
xlabel('Samples');
ylabel('Amplitude');
