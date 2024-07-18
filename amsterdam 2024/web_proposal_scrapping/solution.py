def solution(text):

    sentences = sorted(text.split(". "), key=lambda x: len(x), reverse=True)
    longest_without_comma = [s for s in sentences if "," not in s][0] + "."
    shortest = sentences[-1] + "."
    most_commas = sorted(sentences, key=lambda x: x.count(","))[-1] + "."

    return [longest_without_comma, shortest, most_commas]


print("\n".join(solution(open("input.txt").read())))
