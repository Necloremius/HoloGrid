import webbrowser # builtin
import random # builtin
from gpiozero import Button # install this
from time import sleep # builtin
import timeit # benchmarking

# define button, set up collection of videos
button = Button(17)

vids = ["https://www.youtube.com/watch?v=vTufphdowOw", "https://www.youtube.com/watch?v=NLTqazgsSBM", "https://www.youtube.com/watch?v=ASX_d0H0HYw",
        "https://www.youtube.com/watch?v=d-Ja4cag0UY", "https://www.youtube.com/watch?v=JNmYHFV7-hE", "https://www.youtube.com/watch?v=CIszi2Kv_lk",
        "https://www.youtube.com/watch?v=bQHAuabOCS8", "https://www.youtube.com/watch?v=wDf6vOCehGE", "https://www.youtube.com/watch?v=GtRm_KSfMfg",
        "https://www.youtube.com/watch?v=fE1E9l5AQJw", "https://www.youtube.com/watch?v=R7SKPdSxbRw", "https://www.youtube.com/watch?v=bH_LwIbAy6I",
        "https://www.youtube.com/watch?v=jQvkxYUThrc"]

while True:
    if (button.is_pressed):
        webbrowser.open(random.choices(vids)[0], new=2)
        sleep(1)
