import os, _pickle as pickle

def load_tfod_data(tfod_directory, n_shots=1, benchmark=False):
	""" Load few-shot annotation or benchmark evaluation data.
		Few-shot annotation based on the number of examples per object. """

	# Load few-shot annotation or evaluation data.
	if benchmark: 
		print("Loading tfod benchmark data.")
		file_name = "tfod_benchmark.pk" # Challenging benchmark from paper.
		#file_name = "tfod_eval_22.pk" # Adds easier examples with benchmark.
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