clear all;
close all;

s = tf('s'); % Define Laplace variable

% Define and calculate Transfer Functions
TF1 = (s^2 + 3*s + s) / (s^3 + 3*s^2 + 5*s + 7);
TF2 = 1 / (s - 5);
TF3 = 1 / (s^2);
TF4 = (s^3 + 5*s + 1) / (s^2 + 11*s);

subplot(2, 2, 1);
pzplot(TF1);
title('TF1');
grid on;

subplot(2, 2, 2);
pzplot(TF2);
title('TF2');
grid on;

subplot(2, 2, 3);
pzplot(TF3);
title('TF3');
grid on;

subplot(2, 2, 4);
pzplot(TF4);
title('TF4');
grid on;
