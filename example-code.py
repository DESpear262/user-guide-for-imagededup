from imagededup.methods import DHash
dhasher = DHash()
#duplicates = dhasher.find_duplicates(image_dir='/path/to/image_dir', scores=False, max_distance_threshold=1)
duplicates = dhasher.find_duplicates_to_remove(image_dir='/path/to/image_dir', scores=False, max_distance_threshold=1)
