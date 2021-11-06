# pip install fastapi
# pip install uvicorn[standard]
# uvicorn api:app --reload


from fastapi import FastAPI
import tg_bot.modules.sql.antispam_sql as sql1
import tg_bot.modules.sql.blacklistusers_sql as sql2
from telegram import __version__ as v

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "online", "ptb_ver": v }


@app.get("/getuser/{user_id}")
def read_item(user_id: int):
    try:
        a = sql1.is_user_gbanned(user_id)
        if a:
            user = sql1.get_gbanned_user(user_id)
            areason = user.reason
        else:
            areason = None

        b = sql2.is_user_blacklisted(user_id)
        breason = sql2.get_reason(user_id) if b else None
        return {"status": "ok", "user_id": user_id, "gbanned": a, "gban_reason" : areason, "blacklisted" : b, "blacklist_reason" : breason}
    except Exception:
        a = None
        areason = None
        b = None
        breason = None
        return {"status": "ok", "user_id": user_id, "gbanned": a, "gban_reason" : areason, "blacklisted" : b, "blacklist_reason" : breason}
