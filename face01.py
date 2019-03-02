
import sys
import json
import urllib
import requests

from pprint import pprint

url1 ='http://asecuritysite.com/log/F52361.jpg'

if (len(sys.argv)>1):
        url1=str(sys.argv[1])

file='zzzz'

if (len(sys.argv)>2):
        file=str(sys.argv[2])


headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'KEY HERE',
}

params = urllib.urlencode({
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'true',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup',
})

body = {
    'url': url1
}

url = 'https://westeurope.api.cognitive.microsoft.com/face/v1.0/detect?%s' % params

resp = requests.post(url, data=json.dumps(body), headers=headers)

binary = resp.content
output = json.loads(binary)

print binary
age=str(output[0]['faceAttributes']['age'])
gender=str(output[0]['faceAttributes']['gender'])
smile=str(output[0]['faceAttributes']['smile'])
glasses=str(output[0]['faceAttributes']['glasses'])
sideburns=str(output[0]['faceAttributes']['facialHair']['sideburns'])
moustache=str(output[0]['faceAttributes']['facialHair']['moustache'])
beard=str(output[0]['faceAttributes']['facialHair']['beard'])
faceid=str(output[0]['faceId'])

sadness=str(output[0]['faceAttributes']['emotion']['sadness'])
neutral=str(output[0]['faceAttributes']['emotion']['neutral'])
contempt=str(output[0]['faceAttributes']['emotion']['contempt'])
disgust=str(output[0]['faceAttributes']['emotion']['disgust'])
anger=str(output[0]['faceAttributes']['emotion']['anger'])
surprise=str(output[0]['faceAttributes']['emotion']['surprise'])
fear=str(output[0]['faceAttributes']['emotion']['fear'])
happiness=str(output[0]['faceAttributes']['emotion']['happiness'])

disgust=str(output[0]['faceAttributes']['emotion']['disgust'])

lip=str(output[0]['faceAttributes']['makeup']['lipMakeup'])
eye=str(output[0]['faceAttributes']['makeup']['eyeMakeup'])


str=''
str = str+'Age: '+age+'\nGender: '+gender+'\nSmile: '+smile+'\nGlasses: '+glasses
str = str+'\nFacial Hair:'
str = str+'\n Sideburns: '+sideburns
str = str+'\n Moustache: '+moustache
str = str+'\n Beard: '+beard

str = str+'\nEmotion:'
str = str+'\n Saddness: '+sadness
str = str+'\n Neutral: '+neutral
str = str+'\n Contempt: '+contempt
str = str+'\n Anger: '+anger
str = str+'\n Surprise: '+surprise
str = str+'\n Fear: '+fear
str = str+'\n Happiness: '+happiness
str = str+'\n Disgust: '+disgust

str = str+'\nMakeup:'
str = str+'\n Lipmakeup: '+lip
str = str+'\n Eyemakeup: '+eye


print str

print '\nFace Rectangle: ',output[0]['faceRectangle']

print 'Head Pose: ',output[0]['faceAttributes']['headPose']
print
print 'Hair: ',output[0]['faceAttributes']['hair']





import numpy as np
import cv2
import matplotlib.pyplot as plot
import sys
import urllib


imfile = url

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import numpy as np


from PIL import Image
import requests
from StringIO import StringIO

response = requests.get(url1)
im = Image.open(StringIO(response.content))

width=int(output[0]['faceRectangle']['width'])
top=int(output[0]['faceRectangle']['top'])
height=int(output[0]['faceRectangle']['height'])
left=int(output[0]['faceRectangle']['left'])

ex1=int(output[0]['faceLandmarks']['eyeLeftBottom']['x'])
ey1=int(output[0]['faceLandmarks']['eyeLeftBottom']['y'])
ex2=int(output[0]['faceLandmarks']['eyeLeftTop']['x'])
ey2=int(output[0]['faceLandmarks']['eyeLeftTop']['y'])

ex3=int(output[0]['faceLandmarks']['eyeLeftInner']['x'])
ey3=int(output[0]['faceLandmarks']['eyeLeftInner']['y'])
ex4=int(output[0]['faceLandmarks']['eyeLeftOuter']['x'])
ey4=int(output[0]['faceLandmarks']['eyeLeftOuter']['y'])

ex5=int(output[0]['faceLandmarks']['eyeRightBottom']['x'])
ey5=int(output[0]['faceLandmarks']['eyeRightBottom']['y'])
ex6=int(output[0]['faceLandmarks']['eyeRightTop']['x'])
ey6=int(output[0]['faceLandmarks']['eyeRightTop']['y'])

ex7=int(output[0]['faceLandmarks']['eyeRightInner']['x'])
ey7=int(output[0]['faceLandmarks']['eyeRightInner']['y'])
ex8=int(output[0]['faceLandmarks']['eyeRightOuter']['x'])
ey8=int(output[0]['faceLandmarks']['eyeRightOuter']['y'])


mx1=int(output[0]['faceLandmarks']['mouthRight']['x'])
my1=int(output[0]['faceLandmarks']['mouthRight']['y'])
mx2=int(output[0]['faceLandmarks']['mouthLeft']['x'])
my2=int(output[0]['faceLandmarks']['mouthLeft']['y'])

mx3=int(output[0]['faceLandmarks']['underLipBottom']['x'])
my3=int(output[0]['faceLandmarks']['underLipBottom']['y'])
mx4=int(output[0]['faceLandmarks']['underLipTop']['x'])
my4=int(output[0]['faceLandmarks']['underLipTop']['y'])


mx5=int(output[0]['faceLandmarks']['upperLipBottom']['x'])
my5=int(output[0]['faceLandmarks']['upperLipBottom']['y'])
mx6=int(output[0]['faceLandmarks']['upperLipTop']['x'])
my6=int(output[0]['faceLandmarks']['upperLipTop']['y'])

mx7=int(output[0]['faceLandmarks']['eyebrowLeftInner']['x'])
my7=int(output[0]['faceLandmarks']['eyebrowLeftInner']['y'])
mx8=int(output[0]['faceLandmarks']['eyebrowLeftOuter']['x'])
my8=int(output[0]['faceLandmarks']['eyebrowLeftOuter']['y'])

mx9=int(output[0]['faceLandmarks']['eyebrowRightInner']['x'])
my9=int(output[0]['faceLandmarks']['eyebrowRightInner']['y'])
mx10=int(output[0]['faceLandmarks']['eyebrowRightOuter']['x'])
my10=int(output[0]['faceLandmarks']['eyebrowRightOuter']['y'])

mx11=int(output[0]['faceLandmarks']['noseLeftAlarOutTip']['x'])
my11=int(output[0]['faceLandmarks']['noseLeftAlarOutTip']['y'])
mx12=int(output[0]['faceLandmarks']['noseLeftAlarTop']['x'])
my12=int(output[0]['faceLandmarks']['noseLeftAlarTop']['y'])

mx13=int(output[0]['faceLandmarks']['noseRightAlarOutTip']['x'])
my13=int(output[0]['faceLandmarks']['noseRightAlarOutTip']['y'])
mx14=int(output[0]['faceLandmarks']['noseRightAlarTop']['x'])
my14=int(output[0]['faceLandmarks']['noseRightAlarTop']['y'])

mx15=int(output[0]['faceLandmarks']['noseRootLeft']['x'])
my15=int(output[0]['faceLandmarks']['noseRootLeft']['y'])
mx16=int(output[0]['faceLandmarks']['noseRootRight']['x'])
my16=int(output[0]['faceLandmarks']['noseRootRight']['y'])

mx17=int(output[0]['faceLandmarks']['noseTip']['x'])
my17=int(output[0]['faceLandmarks']['noseTip']['y'])

# Create figure and axes
fig,ax = plt.subplots(1)
f1=ax.imshow(im)
f1.axes.get_xaxis().set_visible(False)
f1.axes.get_yaxis().set_visible(False)

# Create a Rectangle patch
rect = patches.Rectangle((left,top),width,height,linewidth=2,edgecolor='r',facecolor='none')

e1 = patches.Rectangle((ex1,ey1),2,2,linewidth=3,edgecolor='green',facecolor='none')
e2 = patches.Rectangle((ex2,ey2),2,2,linewidth=3,edgecolor='green',facecolor='none')
e3 = patches.Rectangle((ex3,ey3),2,2,linewidth=3,edgecolor='green',facecolor='none')
e4 = patches.Rectangle((ex4,ey4),2,2,linewidth=3,edgecolor='green',facecolor='none')

e5 = patches.Rectangle((ex5,ey5),2,2,linewidth=3,edgecolor='green',facecolor='none')
e6 = patches.Rectangle((ex6,ey6),2,2,linewidth=3,edgecolor='green',facecolor='none')
e7 = patches.Rectangle((ex7,ey7),2,2,linewidth=3,edgecolor='green',facecolor='none')
e8 = patches.Rectangle((ex8,ey8),2,2,linewidth=3,edgecolor='green',facecolor='none')


m1 = patches.Rectangle((mx1,my1),2,2,linewidth=3,edgecolor='blue',facecolor='none')
m2 = patches.Rectangle((mx2,my2),2,2,linewidth=3,edgecolor='blue',facecolor='none')
m3 = patches.Rectangle((mx3,my3),2,2,linewidth=3,edgecolor='blue',facecolor='none')
m4 = patches.Rectangle((mx4,my4),2,2,linewidth=3,edgecolor='blue',facecolor='none')

m5 = patches.Rectangle((mx5,my5),2,2,linewidth=3,edgecolor='blue',facecolor='none')
m6 = patches.Rectangle((mx6,my6),2,2,linewidth=3,edgecolor='blue',facecolor='none')

m7 = patches.Rectangle((mx7,my7),2,2,linewidth=3,edgecolor='w',facecolor='none')
m8 = patches.Rectangle((mx8,my8),2,2,linewidth=3,edgecolor='w',facecolor='none')

m9 = patches.Rectangle((mx9,my9),2,2,linewidth=3,edgecolor='w',facecolor='none')
m10 = patches.Rectangle((mx10,my10),2,2,linewidth=3,edgecolor='w',facecolor='none')

m11 = patches.Rectangle((mx11,my11),2,2,linewidth=3,edgecolor='orange',facecolor='none')
m12 = patches.Rectangle((mx12,my12),2,2,linewidth=3,edgecolor='orange',facecolor='none')

m13 = patches.Rectangle((mx13,my13),2,2,linewidth=3,edgecolor='orange',facecolor='none')
m14 = patches.Rectangle((mx14,my14),2,2,linewidth=3,edgecolor='orange',facecolor='none')

m15 = patches.Rectangle((mx15,my15),2,2,linewidth=3,edgecolor='orange',facecolor='none')
m16 = patches.Rectangle((mx16,my16),2,2,linewidth=3,edgecolor='orange',facecolor='none')

m17 = patches.Rectangle((mx17,my17),1,1,linewidth=3,edgecolor='orange',facecolor='none')

# Add the patch to the Axes
ax.add_patch(rect)
ax.add_patch(e1)
ax.add_patch(e2)
ax.add_patch(e3)
ax.add_patch(e4)
ax.add_patch(e5)
ax.add_patch(e6)
ax.add_patch(e7)
ax.add_patch(e8)

ax.add_patch(m1)
ax.add_patch(m2)
ax.add_patch(m3)
ax.add_patch(m4)
ax.add_patch(m5)
ax.add_patch(m6)

ax.add_patch(m7)
ax.add_patch(m8)

ax.add_patch(m9)
ax.add_patch(m10)

ax.add_patch(m11)
ax.add_patch(m12)

ax.add_patch(m13)
ax.add_patch(m14)

ax.add_patch(m15)
ax.add_patch(m16)

ax.add_patch(m17)

ax.annotate(str, (0,10), color='b', weight='normal', fontsize=8, ha='left', va='top')

f2= "c:\\inetpub\\wwwroot\\log\\svg\\"+file

fig.savefig(f2,format='JPG',bbox_inches='tight')
