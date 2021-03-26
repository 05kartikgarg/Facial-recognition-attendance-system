import cognitive_face as CF
from global_variables import personGroupId
import sys

Key = '98f63b21d91d43129197a44e2e3e3ea5'
CF.Key.set(Key)
BASE_URL = 'https://facial-attendance.cognitiveservices.azure.com/'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)

personGroups = CF.person_group.lists()
for personGroup in personGroups:
    if personGroupId == personGroup['personGroupId']:
        print (personGroupId + " already exists.")
        sys.exit()

res = CF.person_group.create(personGroupId)
print(res) 
