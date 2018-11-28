#!/usr/bin/env python3


def get_stream(path):
    with open(path, encoding='utf-8') as infile:
        return infile.read()


stream = get_stream("input.txt")


def find_in_list(list_, x, start=0):
    i = None
    try:
        i = list_.index(x, start)
    except ValueError:
        pass
    return i


# Stream types:
# S = Stream (main)
# < = Garbage
# { = Group
# ! = Ignored


class Stream:
    def __init__(self, text, stream_type=None):
        self.stream_type = stream_type or 'S'
        if self.stream_type == 'S':
            text = self.cancel_chars(list(text))
            text = self.identify_garbage(text)
        if self.stream_type in ['S', '{']:
            text = self.identify_groups(text)
        self.data = text

    def cancel_chars(self, text):
        start = find_in_list(text, '!')
        while start is not None:
            if (start + 1) < len(text):
                text[start] = Stream(text.pop(start + 1), '!')
            start = find_in_list(text, '!', start + 1)

        return text

    def identify_garbage(self, text):
        start = find_in_list(text, '<')
        while start is not None:
            end = text.index('>', start)
            text[start] = Stream(text[start + 1:end], '<')
            del text[start + 1:end + 1]
            start = find_in_list(text, '<', start + 1)

        return text

    def identify_groups(self, text):
        count = 0
        groups = []
        start = None

        for i in range(len(text)):
            if text[i] == '{':
                count += 1
                if count == 1:
                    start = i
            elif text[i] == '}':
                count -= 1
                if count == 0:
                    groups.append((start, i))

        removed = 0
        for group in groups:
            start = group[0] - removed
            end = group[1] - removed
            removed += (end - start)

            text[start] = Stream(text[start + 1:end], '{')
            del text[start + 1:end + 1]

        return text

    def count_groups(self):
        count = 0
        for s in self.data:
            if hasattr(s, 'stream_type') and s.stream_type == '{':
                count += 1
                count += s.count_groups()

        return count

    def score_groups(self, outer=0):
        score = 0
        if self.stream_type == '{':
            score += outer + 1
            outer += 1

        for s in self.data:
            if hasattr(s, 'stream_type') and s.stream_type == '{':
                score += s.score_groups(outer)

        return score

    def count_garbage(self):
        count = 0
        for s in self.data:
            if hasattr(s, 'stream_type'):
                if s.stream_type == '{':
                    count += s.count_garbage()
                elif s.stream_type == '<':
                    count += len(
                        [s for s in s.data if type(s) == str]
                    )
        return count

    def __repr__(self):
        if self.stream_type == 'S':
            return ''.join([str(d) for d in self.data])
        elif self.stream_type == '{':
            return ' {' + ''.join(str(d) for d in self.data) + '} '
        elif self.stream_type == '<':
            return ' <' + ''.join(str(d) for d in self.data) + '> '
        else:
            return ' !' + str(self.data) + ' '


s = Stream(stream)
#print('Stream:', s)
print('Num groups:', s.count_groups())
print('Score:', s.score_groups())
print('Garbage:', s.count_garbage())
