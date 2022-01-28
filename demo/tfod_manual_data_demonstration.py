import os, IPython, _pickle as pickle

# Few-shot object detection configuration.
k = 1 # 1, 2, or 4. Number of few-shot annotated examples per object.
tfod_directory = "./"

def load_tfod_data(tfod_directory, n_shots=1, benchmark=False):
	""" Load few-shot annotation or benchmark evaluation data.
		Few-shot annotation based on the number of examples per object. """

	# Load few-shot annotation or evaluation data.
	if benchmark: 
		print("Loading tfod benchmark data.")
		file_name = "tfod_benchmark.pk" # Challenging benchmark from paper.
	else: 
		print("Loading %s-shot annotation data." % n_shots)
		file_name = "tfod_%sshot.pk" % n_shots
	fewshot_file = os.path.join(tfod_directory, "data", file_name)
	fewshot_set = pickle.load(open(fewshot_file, "rb"))

	# Adjust image path based on data_directory.
	for f in fewshot_set: 
		f["file_name"] = os.path.join(tfod_directory, "data", f["file_name"])

	# Return annotation object detection categories.
	categories = ["background", "box of sugar", "tuna", "gelatin", "chips can",
		 	"potted meat", "plastic banana", "power drill", "marker", 
		 	"padlock", "wood", "spring clamp", "screwdriver"] 
			
	return fewshot_set, categories

# Load few-shot annotation data.
fewshot_data, categories = load_tfod_data(tfod_directory, n_shots=k)

# Manually load annotated data and use your few-shot detection model here.
print("\nExample few-shot annotation data details:\n\n%s\n" % fewshot_data[0])
print("\nObject categories are %s.\n" % categories)
print("Manually interpret the fewshot_data for your model here.")
IPython.embed()

# Use tfod benchmark for evaluation after using few-shot annotation with model.
benchmark_data, categories = load_tfod_data(tfod_directory, benchmark=True)
print("Manually evaluate your model using benchmark_data and MS-COCO AP metrics here.")
IPython.embed()

print("See other demonstrations to load and evaluate automatically using detectron2.")