from birdnetlib import Recording
from birdnetlib.analyzer import Analyzer
from datetime import datetime
from ChatModels import GOOGLE_PROMPT 
from ChatModels import META_PROMPT


analyzer = Analyzer()
recording = Recording(
    analyzer,
   "RTH.mp3",
    lat=35.4244,
    lon=-120.7463,
    date=datetime(year=2022, month=5, day=10), 
    min_conf=0.25,
)
recording.analyze()
print("<----------------------------------------------------BIRD ANALYSIS---------------------------------------------------->\n")
print(recording.detections)
print("<----------------------------------------------------GOOGLE DATA ON THE SPECIES---------------------------------------------------->\n")
if recording.detections:
    species_name = recording.detections[0]['common_name']
   # GOOGLE_PROMPT(str(species_name))
    META_PROMPT(str(species_name))