def findAll(pattern, text):
    text_index = 0
    results = []

    while True:
        text_index = text.find(pattern, text_index)

        if (text_index == -1):
            break
        else:
            results.append(text_index)
            text_index += 1

    return results