All hash methods run in about 10 mins on SAC. The CNN method ran very slowly (an hour + on SAC as opposed to 10 mins) and crashed before it could save  its output. Not sure if that one has benefits the hash methods don't have, but use advisedly I suppose. As I couldn't get it to work, I haven't documented it. Official documentation can be found here: https://idealo.github.io/imagededup/user_guide/finding_duplicates/

To use in python, import the method you want to use with `from imagededup.methods import [WHICHEVER METHOD YOU WANT]`. Method options are "DHash", "PHash", "AHash", and "WHash".

After importing, instantiate a method variable `hasher = [METHOD]()`

Finally, run the deduper with the command `duplicates = [METHOD].find_duplicates(image_dir='path/to/images')`

This method will return a dictionary of all images in image_dir paired with a list of images flagged as duplicates formatted:
```{
  "image 1" : [
    "duplicate image 1",
    "duplicate image 2",
    ...
  ]
  "image 2" : []
  ...
  "duplicate image 1 : [
    "image 1",
    "duplicate image 2"
  ]
  ...
}
```

---

Useful optional arguments for find_duplicates are `scores=BOOL`, `outfile='PATH'`, and `max-distance-threshold=INT`

`scores` appends the similarity score to items flagged as duplicates when `scores=True`.
Scores are formatted:
```
{
  "image 1": [
    [
      "duplicate image 1",
      0
    ],
    [
      "duplicate image 2",
      3
    ],
    ...
  ]
}
```

In addition to returning the dictionary of duplicates, `outfile` writes the output to `PATH`. The outfile must use the .json format.

`max_distance_threshold` sets the sensitivity of duplicate identification for the hash-based functions. It takes an int between 0 and 64, inclusive. The lower the number, the lower the sensitivity to duplicates. MDT=0 will only flag exact duplicates, 10 is the default value, I found values between 1 and 5 to be most useful.

---

In addition to the `find_duplicates` method, dedup also provides a `find_duplicates_to_remove` method. Instead of outputting a dictionary, this simply outputs a list of all files flagged as duplicates. It does not proactively remove them, just returns the file names in a more conveneient format for deletion. Be advised that, both original images and their duplicates are likely to be flagged by this method. If this method is used and there's a family of n images which are duplicates or near-duplicates, this method will flag the entire family. It will not leave one member as a representative. If used carelessly, this might introduce bias into the data.

---


#Significant numbers of false-positive duplicates
from imagededup.methods import DHash
dhasher = DHash()
duplicates = dhasher.find_duplicates(image_dir='/fsx/home-despear/home/jdp/simulacra-aesthetic-captions', scores=False, outfile='/fsx/home-despear/dhash_sacdupes.json')


# Not many false positives, but not 0 either. Usable but will eliminate some good data
from imagededup.methods import DHash
dhasher = DHash()
duplicates = dhasher.find_duplicates(image_dir='/fsx/home-despear/home/jdp/simulacra-aesthetic-captions', scores=False, max_distance_threshold=5, outfile='/fsx/home-despear/dhash_mdt5_sacdupes.json')


#No false positives I could find, but all images flagged in SAC were soft gradients or something like that, so possible high rate of false negatives. Will need to test on a different dataset to be sure.
from imagededup.methods import DHash
dhasher = DHash()
duplicates = dhasher.find_duplicates(image_dir='/fsx/home-despear/home/jdp/simulacra-aesthetic-captions', scores=False, max_distance_threshold=1, outfile='/fsx/home-despear/dhash_mdt1_sacdupes.json')


#A lot (a LOT) of false positives. Avoid.
from imagededup.methods import WHash
whasher = WHash()
duplicates = whasher.find_duplicates(image_dir='/fsx/home-despear/home/jdp/simulacra-aesthetic-captions', scores=False, outfile='/fsx/home-despear/sacdupes/whash_sacdupes.json')

#Significant false positives. Very likely unusable.
...
duplicates = whasher.find_duplicates(image_dir='/fsx/home-despear/home/jdp/simulacra-aesthetic-captions', scores=False, max_distance_threshold=5, outfile='/fsx/home-despear/sacdupes/mdt5_whash_sacdupes.json')

#Usable, but with significant false positives
...
duplicates = whasher.find_duplicates(image_dir='/fsx/home-despear/home/jdp/simulacra-aesthetic-captions', scores=False, max_distance_threshold=1, outfile='/fsx/home-despear/sacdupes/mdt1_whash_sacdupes.json')


#A lot (a LOT) of false positives. Avoid.
from imagededup.methods import AHash
ahasher = AHash()
duplicates = ahasher.find_duplicates(image_dir='/fsx/home-despear/home/jdp/simulacra-aesthetic-captions', scores=False, outfile='/fsx/home-despear/sacdupes/ahash_sacdupes.json')

#Signicant false positives. Likely unusable.
...
duplicates = ahasher.find_duplicates(image_dir='/fsx/home-despear/home/jdp/simulacra-aesthetic-captions', scores=False, max_distance_threshold=5, outfile='/fsx/home-despear/sacdupes/mdt5_ahash_sacdupes.json')

#A lot of false positives but definitely usable. Good option if DHash MDT=1 is insufficently agressive.
...
duplicates = ahasher.find_duplicates(image_dir='/fsx/home-despear/home/jdp/simulacra-aesthetic-captions', scores=False, max_distance_threshold=1, outfile='/fsx/home-despear/sacdupes/mdt1_ahash_sacdupes.json')


#Detected few duplicates, but almost all were false positives. Avoid.
from imagededup.methods import PHash
phasher = PHash()
duplicates = phasher.find_duplicates(image_dir='/fsx/home-despear/home/jdp/simulacra-aesthetic-captions', scores=False, outfile='/fsx/home-despear/sacdupes/phash_sacdupes.json')

#Very, very few false positives. Likely significant false negatives. Avoid until further experimentation is done.
...
duplicates = phasher.find_duplicates(image_dir='/fsx/home-despear/home/jdp/simulacra-aesthetic-captions', scores=False, max_distance_threshold=5, outfile='/fsx/home-despear/sacdupes/mdt5_phash_sacdupes.json')

#No false positives. Likely significant false negatives. Avoid until further experimentation is done.
...
duplicates = phasher.find_duplicates(image_dir='/fsx/home-despear/home/jdp/simulacra-aesthetic-captions', scores=False, max_distance_threshold=1, outfile='/fsx/home-despear/sacdupes/mdt1_phash_sacdupes.json')
