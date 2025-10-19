from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from uuid import uuid4
from typing import Dict, List

app = FastAPI(title="BlinkTalk Signaling Server")

# Allow frontend origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For testing only — we’ll restrict this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Store active rooms
rooms: Dict[str, List[WebSocket]] = {}

@app.get("/")
def root():
    return {"message": "Ducx signaling ready!!"}

@app.post("/create-room")
def create_room():
    """Create a new unique room"""
    room_id = str(uuid4())[:8]
    rooms[room_id] = []
    return {"room_id": room_id}

@app.websocket("/ws/{room_id}")
async def websocket_endpoint(websocket: WebSocket, room_id: str):
    """WebSocket endpoint for signaling messages"""
    await websocket.accept()

    if room_id not in rooms:
        rooms[room_id] = []
    rooms[room_id].append(websocket)

    try:
        while True:
            message = await websocket.receive_text()

            # Relay message to all other participants in the same room
            for conn in list(rooms[room_id]):
                if conn != websocket:
                    try:
                        await conn.send_text(message)
                    except Exception:
                        # Clean up broken connections
                        rooms[room_id].remove(conn)
    except WebSocketDisconnect:
        rooms[room_id].remove(websocket)
        if not rooms[room_id]:
            del rooms[room_id]

