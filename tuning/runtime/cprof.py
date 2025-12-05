from func import fun
import cProfile
import pstats

with cProfile.Profile() as pr:
    fun()

stats = pstats.Stats(pr)
stats.sort_stats("cumtime").print_stats(20)