import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'),
              ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'),
              ('relev--ant', '-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]


def MED(S, T):
  # TO DO - modify to account for insertions, deletions and substitutions
  if (S == ""):
    return (len(T))
  elif (T == ""):
    return (len(S))
  else:
    if (S[0] == T[0]):
      return (MED(S[1:], T[1:]))
    else:
      return (1 + min(MED(S, T[1:]), MED(S[1:], T)))



def fast_MED(S, T, MED={}):
  # TODO -  implement top-down memoization
  def fast_MED(S, T, MED={}):
    if (S, T) in MED:
      return MED[(S, T)]

    if S == "":
      result = len(T)
    elif T == "":
      result = len(S)
    else:
      if S[0] == T[0]:
        result = fast_MED(S[1:], T[1:], MED)
      else:
        result = 1 + min(fast_MED(S, T[1:], MED), fast_MED(S[1:], T, MED),
                         fast_MED(S[1:], T[1:], MED))

    MED[(S, T)] = result
    return result


def fast_align_MED(S, T, MED={}):
  # TODO - keep track of alignment
  if (S, T) in MED:
    return MED[(S, T)]

  if S == "":
    alignment_S = "-" * len(T)
    alignment_T = T
  elif T == "":
    alignment_S = S
    alignment_T = "-" * len(S)
  elif S[0] == T[0]:
    A_S, A_T = fast_align_MED(S[1:], T[1:], MED)
    alignment_S = S[0] + A_S
    alignment_T = T[0] + A_T
  else:
    I_S, I_T = fast_align_MED(S, T[1:], MED)
    D_S, D_T = fast_align_MED(S[1:], T, MED)
    I_C = 1 + len(I_S)
    D_C = 1 + len(D_S)
    if I_C <= D_C:
      alignment_S = "-" + I_S
      alignment_T = T[0] + I_T
    else:
      alignment_S = S[0] + D_S
      alignment_T = "-" + D_T

  alignment_result = (alignment_S, alignment_T)
  MED[(S, T)] = alignment_result
  return alignment_result



for S, T in test_cases:
  assert fast_MED(S, T) == MED(S, T)

for i in range(len(test_cases)):
  S, T = test_cases[i]
  align_S, align_T = fast_align_MED(S, T)
  assert (align_S == alignments[i][0] and align_T == alignments[i][1])
