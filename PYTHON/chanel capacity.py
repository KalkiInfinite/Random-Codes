import math

m = int(input("Enter the number of messages: "))

for i in range(1, m + 1):
    p = float(input("Enter the probability of message {}: ".format(i)))
    if p > 0:
        Hmax = math.log2(m)
        print("Maximum Entropy:", Hmax)

        r = int(input("Enter rate of messages per second: "))
        print("Maximum Entropy:", Hmax, "bits/message")

        Cmax = r * Hmax
        print("Maximum Channel Capacity:", Cmax, "bps")

        H = p * math.log2(1 / p)

        B = float(input("Enter the bandwidth of message, B in Hertz (Hz): "))

        def convert_dB_to_numerical(SbyN):
            return math.pow(10, SbyN / 10)

        SbyN = float(input("Enter the signal to noise ratio, S/N in decibels (dB): "))

        SbyN_linear = convert_dB_to_numerical(SbyN)

        C = B * math.log2(1 + SbyN_linear)
        print("Channel Capacity:", C, "bps")
