import cognitive_face as CF
from global_variables import personGroupId

Key = '98f63b21d91d43129197a44e2e3e3ea5'
CF.Key.set(Key)
BASE_URL = 'https://centralus.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)

res = CF.person_group.train(personGroupId)
print (res)
