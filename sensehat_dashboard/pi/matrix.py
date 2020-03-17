from sense_hat import SenseHat
import firebase_admin
from firebase_admin import credentials, firestore

# constants
COLLECTION = 'raspberry'
DOCUMENT = 'senne-pi'

# firebase
cred = credentials.Certificate("../app/config/iotlabosenne-firebase-adminsdk-yb6se-e6fe951921.json")
firebase_admin.initialize_app(cred)

# sensehat 
sense = SenseHat()
sense.set_imu_config(False, False, False)
sense.clear()

def hexToRgb(a):
    h = a.lstrip('#')
    rgb = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    return rgb

def update_sensehat(doc_snapshot, changes, read_time):
    for doc in doc_snapshot:
        doc_readable = doc.to_dict()
        print(doc_readable)
        # watching if the matrix 'isOn' and set the color to the sensehat
        if doc_readable.get('matrix').get('isOn'):
            newPixels = hexToRgb(doc_readable.get('matrix').get('color').get('value'))
            X = [newPixels[0], newPixels[1], newPixels[2]]
            print(X)
            sensehatmatrix = [
            X, X, X, X, X, X, X, X,
            X, X, X, X, X, X, X, X,
            X, X, X, X, X, X, X, X,
            X, X, X, X, X, X, X, X,
            X, X, X, X, X, X, X, X,
            X, X, X, X, X, X, X, X,
            X, X, X, X, X, X, X, X,
            X, X, X, X, X, X, X, X,
            ]

            sense.set_pixels(sensehatmatrix)
        else:
            sense.clear()

# connect firestore
db = firestore.client()
pi_ref = db.collection(COLLECTION).document(DOCUMENT)
pi_watch = pi_ref.on_snapshot(update_sensehat)

# app
while True:
    pass