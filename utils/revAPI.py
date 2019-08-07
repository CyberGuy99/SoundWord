from rev_ai.speechrec import RevSpeechAPI
import time

# input: the uploaded file name
# output: a list of tuples (Speaker #, text)

file = "key.txt"

def audio_to_text(file_name):
	API_token = None

	with open(file) as f:
		API_token = f.read()

	if (API_token == None):
		print("Uploaded invalid file.\n")
		return

	client = RevSpeechAPI(API_token)

	result = client.submit_job_local_file(file_name)
	revID = result.get("id")

	while(client.view_job(revID).get("status") != "transcribed"):
		print(client.view_job(revID))
		time.sleep(2)

	transcript = client.get_transcript(revID, use_json = False)
	print(transcript)

	while not char in transcript == 

	return transcript

audio_to_text("TrumpFireFury.mp3")