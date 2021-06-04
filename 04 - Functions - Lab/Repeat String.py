def text_repetition(string, n_repetitions):
    result = string * n_repetitions
    return result


text = input()
times = int(input())

print(text_repetition(text, times))

