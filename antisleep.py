import sounddevice as sd
import numpy as np
import time

#print("Running")

SAMPLE_RATE = 44100
CHANNELS = 2
BLOCK = 1024

PULSE_INTERVAL_SEC = 6      
PULSE_LENGTH_MS = 2         
PULSE_AMPLITUDE = 0.02      

silence = np.zeros((BLOCK, CHANNELS), dtype=np.float32)

pulse_samples = int(SAMPLE_RATE * (PULSE_LENGTH_MS / 1000))
pulse = np.zeros((pulse_samples, CHANNELS), dtype=np.float32)


pulse[:, :] = PULSE_AMPLITUDE * np.sin(
    2 * np.pi * 1000 * np.arange(pulse_samples) / SAMPLE_RATE
).reshape(-1, 1)

with sd.OutputStream(
    samplerate=SAMPLE_RATE,
    channels=CHANNELS,
    dtype="float32",
    blocksize=BLOCK
):
    last_pulse = time.time()

    #try:
    while True:
            sd.sleep(10)

            if time.time() - last_pulse >= PULSE_INTERVAL_SEC:
                sd.play(pulse, blocking=True)
                last_pulse = time.time()
    #except KeyboardInterrupt:
        #print("Stopped")
