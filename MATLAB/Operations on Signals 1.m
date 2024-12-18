clear all;
close all;

% Time vector
t = 0:0.01:1;

% Generate sine waves
x1 = sin(2 * pi * 4 * t); % Sine wave with 4 Hz frequency
x2 = sin(2 * pi * 8 * t); % Sine wave with 8 Hz frequency

% Plot the 4 Hz sine wave
subplot(2, 2, 1);
plot(t, x1);
xlabel('Time (s)');
ylabel('Amplitude');
title('Sine Wave: 4 Hz');

% Plot the 8 Hz sine wave
subplot(2, 2, 2);
plot(t, x2);
xlabel('Time (s)');
ylabel('Amplitude');
title('Sine Wave: 8 Hz');

% Add the sine waves
y1 = x1 + x2;
subplot(2, 2, 3);
plot(t, y1);
xlabel('Time (s)');
ylabel('Amplitude');
title('Addition of Sine Waves');

% Multiply the sine waves
y2 = x1 .* x2;
subplot(2, 2, 4);
plot(t, y2);
xlabel('Time (s)');
ylabel('Amplitude');
title('Multiplication of Sine Waves');
