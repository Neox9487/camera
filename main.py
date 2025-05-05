import cv2 as cv
import threading as thread
import numpy as np
import logging as log

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

@app.get("/mask")
def get_mask():
    pass

@app.get("/frame")
def get_frame():
    pass

@app.get("/")
def read_root():
    pass