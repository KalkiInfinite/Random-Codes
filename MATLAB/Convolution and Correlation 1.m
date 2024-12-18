clear all;
close all;
t = 0:0.1:10;
x1 = 1.*(t >= 1) & (t <= 10);
x2 = 1.*(t >= 2) & (t <= 10);
x3 = conv(x1, x2);
n3 = length(x3);
t1 = 0:1:n3-1;

subplot(3,1,1);
plot(t, x1);
xlabel('t');
ylabel('x1(t)');
title('First Signal');

subplot(3,1,2);
plot(t, x2);
xlabel('t');
ylabel('x2(t)');
title('Second Signal');

subplot(3,1,3);
plot(t1, x3);
xlabel('t1');
ylabel('x3(t)');
title('Result of Convolution');
