Find a pattern represented as a linked list in a target linked list and return its index relative to the haystack list's head. Indexation is zero based. If the pattern is not in the list or any of the lists is null, return -1.

For example:

list    := 's'->'a'->'y'->'n'->'a'->'y'
pattern := 'n'->'a'->'y'

f(list, pattern) => 3


list    := 'n'->'a'->'y'->'s'->'a'->'y'
pattern := 'n'->'a'->'y'

f(list, pattern) => 0


list    := null
pattern := 'n'->'a'->'y'

f(list, pattern) => -1


list    := 'n'->'a'->'y'
pattern := null

f(list, pattern) => -1


list    := 'm'->'a'->'y'
pattern := 'n'->'a'->'y'

f(list, pattern) => -1
