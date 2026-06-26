from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def home():
    return {"message": "GamerFuel Server is LIVE"}

# هذا هو الرابط الذي وضعناه في AdsGram
@app.post("/adv-reward")
@app.get("/adv-reward") # أضفنا GET أيضاً للاحتياط
async def adsgram_reward(request: Request):
    # استقبال الـ user_id من الرابط
    user_id = request.query_params.get('user_id')
    
    if user_id:
        print(f"✅ عملية ناجحة! المستخدم رقم {user_id} شاهد الإعلان.")
        # هنا سنضع كود قاعدة البيانات في الخطوة القادمة
        return {"status": "success", "user_id": user_id}
    
    return {"status": "error", "message": "no user_id"}
