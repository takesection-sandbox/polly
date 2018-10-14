import boto3
from contextlib import closing

client = boto3.client('polly')

def _convert(line, path):
    response = client.synthesize_speech(
        OutputFormat='mp3',
        Text=line,
        TextType='text',
        VoiceId='Joanna'
    )

    if "AudioStream" in response:
        with closing(response["AudioStream"]) as stream:
            try:
                # Open a file for writing the output as a binary stream
                with open(path, "wb") as file:
                    file.write(stream.read())
            except IOError as error:
                # Could not write to file, exit gracefully
                print(error)
                sys.exit(-1)

n = 1
with open('text.txt', 'r') as txt:
    line = txt.readline()
    while line:
        _convert(line, "%i_2018rakuten.mp3" % n)
        line = txt.readline()
        n = n + 1
