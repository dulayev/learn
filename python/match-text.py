import collections

# MatchState = collections.namedtuple('MatchState', ['match_count', 'transitions'])

def create_text_stats(line):
    char_poses = {}
    for i, c in enumerate(line):
        char_poses.setdefault(c, []).append(i)
    return char_poses

def find_longest_match(line_stats, text):
    max_len = 0
    prev = {} # pos->len ending at this pos
    for c in text:
        curr = {}
        if c in line_stats:
            for pos in line_stats[c]:
                if pos - 1 in prev:
                    curr[pos] = prev[pos - 1] + 1
                else:
                    curr[pos] = 1
                if max_len < curr[pos]:
                    max_len = curr[pos]
        prev = curr
    return max_len

test_tuples = [
    ("fox", "fox on street", 3),
    ("fox", "holy fox on street", 3),
    ("fox", "holy fox", 3),
    ("eef", "---ef----", 2),
    ("eef", "---eef----", 3)
]

for t in test_tuples:
    assert(find_longest_match(create_text_stats(t[0]), t[1]) == t[2])

