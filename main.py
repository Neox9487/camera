import asyncio
from fastapi import FastAPI, WebSocket
from io import BytesIO
from modules import CameraManager
import cv2 as cv

app = FastAPI()
camera_manager = CameraManager()

async def send_frame(websocket, camera_id):
  camera = camera_manager.get_camera(camera_id)
  try:
    while True:
      frame = camera.get_frame()
      ret, jpeg_frame = cv.imencode('.jpg', frame)
      if not ret:
        raise RuntimeError("Failed to encode frame")
          
      jpeg_bytes = jpeg_frame.tobytes()
      await websocket.send_bytes(jpeg_bytes)  
      await asyncio.sleep(0.1)  
  except Exception as e:
    print(f"Error: {e}")
  finally:
    camera.release()

@app.websocket("/ws/{camera_id}")
async def websocket_endpoint(websocket: WebSocket, camera_id: int):
  await websocket.accept()
  await send_frame(websocket, camera_id)

if __name__ == "__main__":
  import uvicorn
  uvicorn.run(app, host="0.0.0.0", port=8000)
