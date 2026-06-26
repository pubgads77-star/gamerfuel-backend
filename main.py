from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {"message": "GamerFuel Server is Running!"}

@app.post("/adv-reward")
async def adsgram_reward(request: Request):
    # استقبال البيانات من AdsGram
    data = await request.json()
    user_id = data.get('user_id') 
    
    print(f"المستخدم {user_id} حصل على مكافأة!")
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)