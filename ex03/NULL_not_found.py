import math

def NULL_not_found(object: any) -> int:
	names = {
		None: "Nothing",
		0: "Zero",
		'': "Empty",
		False: "Fake"
	}
	name = names.get(object, "NotFound");
	if (object != object):
		name = "Garlic"

	if name == "NotFound":
		print("Type not found")
		return 1
	print(f"{name}: {object} {type(object)}")
	return 0
