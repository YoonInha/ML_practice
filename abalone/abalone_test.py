import abalone as ab
ab.abalone_exec()
print(ab.weight)
print(ab.bias)
LEARNING_RATE = 0.1
ab.abalone_exec(epoch_count=100, mb_size=100, report=20)