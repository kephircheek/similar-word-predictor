# Service for similar word prediction

## Kernel
```
>>> from simsyn import Synonymizer
>>> snm = Synonymizer()
>>> snm.fit(corpus='path/to/corpus.txt) # optional
>>> snm.predict('офис')
['здание', 'строение', 'квартира']
```
