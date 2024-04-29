
# r = 10
# s = 0

# (r != 10) or not (s == -r) or not ((True or r >= 10) and not (s <= 0 and True))
#   False   or     True      or not (    True          and           False)
#   False   or     True      or                  True
#          True              or                  True
#                           True