"""
Script to build the metadataset from the 4 open source
benchmark datasets
"""
import pathlib
import os
import shutil

# Define the dataset using the following formatting:
#
# dataset = {
#     "dataset_class_name": [RSDPath, UCMPath, PNPath, R45Path]
# }


dataset = {
    "airplane": [None, "airplane", "airplane", "airplane"],
    "baseball_field": [None, "baseballdiamond", "baseball_field", "baseball_diamond"],
    "basketball_court": [None, None, "basketball_court", "basketball_court"],
    "bridge": [None, None, "bridge", "bridge"],
    "church": [None, None, None, "church"],
    "coastal_mansion": [None, None, "coastal_mansion", None],
    "crosswalk": [None, None, "crosswalk", None],
    "ferry_terminal": [None, None, "ferry_terminal", None],
    "football_field": ["footballfield", None, "football_field", None],
    "freeway": [None, "freeway", "freeway", "freeway"],
    "golf_course": [None, "golfcourse", "golf_course", "golf_course"],
    "intersection": [None, "intersection", "intersection", "intersection"],
    "mobile_home_park": [None, "mobilehomepark", "mobile_home_park", "mobile_home_park"],
    "nursing_home": [None, None, "nursing_home", None],
    "oil_well": [None, None, "oil_well", None],
    "overpass": ["viaduct", "overpass", "overpass", "overpass"],
    "palace": [None, None, None, "palace"],
    "parking_lot": ["parking", "parkinglot", "parking_lot", "parking_lot"],
    "parking_space": [None, None, "parking_space", None],
    "railway_station": ["railwaystation", None, "railway", "railway_station"],
    "roundabout": [None, None, None, "roundabout"],
    "runway": [None, "runway", "runway", "runway"],
    "runway_marker": [None, None, "runway_marking", None],
    "ship": [None, None, None, "ship"],
    "solar_panel": [None, None, "solar_panel", None],
    "stadium": [None, None, None, "stadium"],
    "storage_tanks": [None, "storagetanks", "storage_tank", "storage_tank"],
    "swimming_pool": [None, None, "swimming_pool", None],
    "tennis_court": [None, "tenniscourt", "tennis_court", "tennis_court"],
    "thermal_power_station": [None, None, None, "thermal_power_station"],
    "track": [None, None, None, "ground_track_field"], 
    "transformer_station": [None, None, "transformer_station", None],
    "wastewater_treatment": [None, None, "wastewater_treatment_plant", None]
}

##################
# Get roots
##################
rsd_root = input("Enter root of RSD: ")
ucm_root = input("Enter root of UC Merced: ")
pn_root = input("Enter root of PatternNet: ")
r45_root = input("Enter root of RESISC45: ")
#bring into array
root_dirs = [rsd_root, ucm_root, pn_root, r45_root]
# convert to absolute
root_dirs = list(map(lambda x: str(pathlib.Path(x).absolute()), root_dirs))
# check for existance
for root in root_dirs:
    if not pathlib.Path(root).is_dir():
        raise ValueError("Invalid Root! {} does not exist!".format(root))


####################
# Begin Building
####################
# get output dir
output_dir = input("Enter path to output directory: ")
# convert to absolute
output_dir = str(pathlib.Path(output_dir).absolute())
# create output dir if necessary
pathlib.Path(output_dir).mkdir(parents=True, exist_ok=True)

##################
# For each class in meta dataset
###################
for dataset_class in dataset:
    #create classs dir
    class_dir = os.path.join(output_dir, dataset_class)
    pathlib.Path(class_dir).mkdir()
    print("Creating class: `{}`".format(dataset_class))
    # for each existing
    img_index = 0
    for benchmark_dataset, root in zip(dataset[dataset_class], root_dirs):
        # check for none
        if benchmark_dataset is None:
            continue
        # begin copying images
        src_dir = os.path.join(root, benchmark_dataset)
        # for each image
        for img in os.listdir(src_dir):
            # get full path to source
            src_file = os.path.join(src_dir, img)
            # get full path to dest
            filename = dataset_class + str(img_index) + str(pathlib.Path(src_file).suffix)
            dest_file = os.path.join(class_dir, filename)
            # perform the copy
            shutil.copy(src_file, dest_file)
            img_index += 1
