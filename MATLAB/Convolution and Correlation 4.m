close all;
clear all;
t = 0:0.01:2;
x1 = 8*sin(2*pi*10*t);
x2 = 10*sin(2*pi*t);
x3 = conv(x1, x2);
x4 = xcorr(x1, x2);
n3 = length(x3);
t1 = 0:1:n3-1;

subplot(2,2,1);
plot(t, x1);
xlabel('t');
ylabel('x1(t)');
title('First Signal x1(t)');

subplot(2,2,2);
plot(t, x2);
xlabel('t');
ylabel('x2(t)');
title('Second Signal x2(t)');

subplot(2,2,3);
plot(t1, x3);
xlabel('t');
ylabel('x3(t)');
title('Result of Convolution');

subplot(2,2,4);
plot(t1, x4);
xlabel('t');
ylabel('x4(t)');
title('Result of Correlation');