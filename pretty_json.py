data = [
  {
    "word": "new",
    "score": 1001
  },
  {
    "word": "little",
    "score": 1000
  },
  {
    "word": "newborn",
    "score": 999
  },
  {
    "word": "first",
    "score": 998
  },
  {
    "word": "old",
    "score": 997
  },
  {
    "word": "poor",
    "score": 996
  },
  {
    "word": "healthy",
    "score": 995
  },
  {
    "word": "tiny",
    "score": 994
  },
  {
    "word": "young",
    "score": 993
  },
  {
    "word": "unborn",
    "score": 992
  },
  {
    "word": "dead",
    "score": 991
  },
  {
    "word": "beautiful",
    "score": 990
  },
  {
    "word": "premature",
    "score": 989
  },
  {
    "word": "born",
    "score": 988
  },
  {
    "word": "big",
    "score": 987
  },
  {
    "word": "second",
    "score": 986
  },
  {
    "word": "normal",
    "score": 985
  },
  {
    "word": "sick",
    "score": 984
  },
  {
    "word": "sweet",
    "score": 983
  },
  {
    "word": "fed",
    "score": 982
  },
  {
    "word": "dear",
    "score": 981
  },
  {
    "word": "pretty",
    "score": 980
  },
  {
    "word": "fat",
    "score": 979
  },
  {
    "word": "happy",
    "score": 978
  },
  {
    "word": "precious",
    "score": 977
  }
]
adjectives = [item["word"] for item in data] # extraction of adjective with for loop
adjectives_str = ",".join(adjectives) # combine the adjective with commas
print(f"Adjectives for the word baby: {adjectives_str}.")
    