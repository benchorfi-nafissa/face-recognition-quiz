import face_recognition
import numpy as np


hadil_image = face_recognition.load_image_file("C:\\Users\\hp\\Desktop\\DRNmem\\views\\hadil.jpg")# Charger l'image de visage connu
hadil_encodage = face_recognition.face_encodings(hadil_image)[0] #encoder le visage trouve dans l'image

nafissa_image = face_recognition.load_image_file("C:\\Users\\hp\\Desktop\\DRNmem\\views\\nafissa.jpeg")
nafissa_encodage = face_recognition.face_encodings(nafissa_image)[0]

said_image = face_recognition.load_image_file("C:\\Users\\hp\\Desktop\\DRNmem\\views\\said.jpeg")
said_encodage = face_recognition.face_encodings(said_image)[0]

#Creation une liste qui contient tous les encodages
encodages_visages_connus = [
    hadil_encodage,
    nafissa_encodage,
    said_encodage
]

#Creation une liste qui contient tous les noms des visages encodes dans le MEME ORDRE
noms_visages_connus = [
    "Hadil Amar bensaber",
    "Nafissa Benchorfi",
    "Said Benchorfi"
]