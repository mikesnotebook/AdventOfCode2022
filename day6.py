from collections import Counter
signal = open("day6_data.txt").read().strip()

found_packet = False
for i in range(0,len(signal)):
    if len(set(signal[i:i+4])) == 4 and not found_packet:
        print("found start of packet at position {}".format(i+4))
        found_packet = True
        
    if len(set(signal[i:i+14])) == 14:
        print("found start of message at position {}".format(i+14))
        break