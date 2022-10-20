Tl;dr: DHash with MDT=1-3 seems the most useful to me. Code to run DHash with MDT=1 can be found here: https://github.com/DESpear262/user-guide-for-imagededup/blob/main/example-code.py

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

The most useful setting I found during testing was DHash with MDT=1. This flagged a significant number of junk images in SAC. I did insufficent testing to determine whether there were significant numbers of unflagged-duplicates, but none of the flagged items I inspected were clear false positives. These are also the settings I used for the example code here: https://github.com/DESpear262/user-guide-for-imagededup/blob/main/example-code.py. That code can be copy/pasted into an instance of Python and should run without any problems. DHash with MDT=2 or 3 are usable if a modest number of false positives are acceptable in order to ensure that all duplicates are removed. With MDT>=5, it flags a considerable number of false positives and should be avoided.

WHash and AHash both generated a significant number of false positives, even on MDT=1. If extremely aggressive dupe flagging is necessary, AHash with MDT=1 or =2 may be usable. Above that, I would recommend avoiding them.

PHash had an extremely low duplicate detection rate, even at MDT=10, but even then the flagged images were all false positives. I don't understand what's going on with this algorithm but it seems like it's off the false-positive-avoidance/true-duplicate-identification Pareto frontier to me. If someone who understands what's going on under the hood here wants to explain what this algorithm is useful for, I'd love to know but for now it seems like a strictly worse option than the others, detecting fewer near-duplicates, and getting even those few wrong. Avoid.
