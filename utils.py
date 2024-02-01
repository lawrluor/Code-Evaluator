# truncate the content to the last suggestion
# this is the equivalent of rewinding back until we find the last closing bracket, removing everything after that, and adding a square bracket to close the list
# this assumes at least one suggestion was made. Otherwise, there will not be a closing bracket to find
def handleJSONDecodeError(content, e):
	content = content[:e.pos] # truncate the content to before an error, in case this was because of an actual invalid character
	index = content.rfind("}")  # index of last complete suggestion (its closing bracket)

	if index == -1:
		# no complete suggestion was made, simply return empty list of suggestions
		return "[]"
	content = content[:index+1] + "]"
	return content