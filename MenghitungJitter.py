#Penjelasan Jitter
#Mengitung Nilai Selisih dari Nilai Waktu Respons Ping

import numpy as np

#Masukan Nilai Pingnya di Ping_times
#Contoh 10, 0.123, 22, dan seterusnya

ping_times=[0.618, 0.579, 0.637, 0.610]
std_dev= np.std(ping_times)

print("Jitter :", std_dev)

