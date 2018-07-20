API mockup serves files from local directory, this simulates a rest API by making directories as the actions, and the object as the file requested.

From the api directory:

python mockapi.py 

in a seperate window you can make a request

curl http://127.0.0.1:8000/check/T3ST
NODUPE

to sumulate checking for a duplicate log where T3ST is the call
