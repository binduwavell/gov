#! /usr/bin/env python3

import operator
import os

VOTES_PATH = 'votes'
CANDIDATES = 'candidates.txt'
LOWEST_PRIOR = 5


def load_candidates():
    candidates = {}
    for line in open(CANDIDATES, 'r'):
        key = line.split(' ')[-1].lower().strip()
        candidates[key] = {
            'fullname': line.strip(),
            'votes': 0,
            'agg_prior': 0,
            'mean_prior': 0
        }
    return candidates


def register_vote(filename, candidates):
    print("Processing: %s" % filename)
    for line in open(filename):
        data = line.split('.')
        priority = data[0]
        if priority.isdigit():
            candidate = data[1].split(' ')[-1].lower().strip()
            if candidate in candidates:
                candidates[candidate]['votes'] += 1
                candidates[candidate]['agg_prior'] += int(priority)
            else:
                print("nok - %s" % candidate)


def final_result(candidates):
    weights = {}
    for c in candidates:
        mean_prior = candidates[c]['agg_prior'] / candidates[c]['votes']
        candidates[c]['mean_prior'] = round(mean_prior, 1)
        weights[c] = candidates[c]['votes'] * 10 + (LOWEST_PRIOR - mean_prior)
    ranking = sorted(weights.items(), key=operator.itemgetter(1), reverse=True)
    print("============================================")
    print("           Board members")
    print("============================================")
    print("R  V   P   Candidate")
    print("--------------------------------------------")
    i = 1
    for r in ranking:
        votes = candidates[r[0]]['votes']
        prior = candidates[r[0]]['mean_prior']
        name = candidates[r[0]]['fullname']
        print("%s  %s  %s  %s" % (i, votes, prior, name))
        i += 1
        if i is 6:
            print("--------------------------------------------")
            print("           Not Elected")
            print("--------------------------------------------")
    print("============================================")


def main():
    candidates = load_candidates()
    # for candidate in candidates:
    #     print(candidate)
    #     print(candidates[candidate]['fullname'])
    for vote in os.listdir(VOTES_PATH):
        register_vote("%s/%s" % (VOTES_PATH, vote), candidates)
        # for line in open("%s/%s" % (VOTES_PATH, vote), 'r'):
        #     print(line)
    # print(sys.argv[0])
    final_result(candidates)


if __name__ == '__main__':
    main()
