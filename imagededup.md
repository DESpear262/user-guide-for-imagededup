# All hash methods run in about 10 mins on SAC. The CNN method ran very slowly (an hour + on SAC as opposed to 10 mins) and crashed before it could save 
# its output. Not sure if that one has benefits the hash methods don't have, but use advisedly I suppose.

#Significant numbers of false-positive duplicates (non-duplicates flagged)
from imagededup.methods import DHash
dhasher = DHash()
duplicates = dhasher.find_duplicates(image_dir='/fsx/home-despear/home/jdp/simulacra-aesthetic-captions', scores=False, outfile='/fsx/home-despear/dhash_sacdupes.json')


# Not many false positives, but not 0 either. Usable but will eliminate some good data
from imagededup.methods import DHash
dhasher = DHash()
duplicates = dhasher.find_duplicates(image_dir='/fsx/home-despear/home/jdp/simulacra-aesthetic-captions', scores=False, max_distance_threshold=5, outfile='/fsx/home-despear/dhash_mdt5_sacdupes.json')


#No false positives, but all images flagged in SAC were soft gradients or something like that, so possible high rate of false negatives. Will need to test on a different dataset to be sure.
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


#Extremely time intensive, results unknown. Process failed before it finished. Only use if you know what you're doing.
from imagededup.methods import CNN
cnn_encoder = CNN()
duplicates = cnn_encoder.find_duplicates(image_dir='/fsx/home-despear/home/jdp/simulacra-aesthetic-captions', min_similarity_threshold=0.85, scores=False, outfile='/fsx/home-despear/CNN_sacdupes.json')
