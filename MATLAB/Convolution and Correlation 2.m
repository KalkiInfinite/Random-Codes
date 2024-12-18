close all;
clear all;
t = 0:0.01:10;
x1 = 2.*(t >= 1 & t <= 2);
xa = 1.*(t >= 0 & t <= 1);
xb = -1.*(t >= 1 & t <= 2);
x2 = xa + xb;
x3 = conv(x1, x2);
n3 = length(x3);
t1 = 0:1:n3-1;

subplot(3,1,1);
plot(t, x1);
xlabel('t');
ylabel('x1(t)');
title('First Signal x1(t)');

subplot(3,1,2);
plot(t, x2);
xlabel('t');
ylabel('x2(t)');
title('Second Signal x2(t)');

subplot(3,1,3);
plot(t1, x3);
xlabel('t');
ylabel('x3(t)');
title('Result of Convolution');