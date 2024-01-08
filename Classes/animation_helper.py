import sys
import time
import msvcrt

def animate_text(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()

        start_time = time.time()
        while time.time() < start_time + delay:
            if msvcrt.kbhit():
                msvcrt.getch()  # Consume the input
                break

