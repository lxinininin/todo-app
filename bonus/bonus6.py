contents = ["All carrots are to be sliced longitudinally.",
            "The carrots were reportedly sliced.",
            "The slicing process was well prepared."]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    # .. because we are in bonus directory
    file = open(f"../files/{filename}", 'w')
    file.write(content)