from fastapi import FastAPI

app1 = FastAPI()


product = {
        1:{"name":"laptop","price":30000,"available_quantity":200},
        2:{"name":"computer","price":40000,"available_quantity":150},
        3:{"name":"earpods","price":7000,"available_quantity":300},
        4:{"name":"headphones","price":3000,"available_quantity":120},
        5:{"name":"type c chanrger","price":1250,"available_quantity":700},
        6:{"name":"mobile","price":20000,"available_quantity":1000},
        7:{"name":"ipod","price":60000,"available_quantity":190},
        8:{"name":"smartwatch","price":5000,"available_quantity":250},
        9:{"name":"Bluetooth speaker","price":2500,"available_quantity":400},
        10:{"name":"external hard drive","price":6000,"available_quantity":180},
        11:{"name":"printer","price":8000,"available_quantity":90},
        12:{"name":"wireless mouse","price":1000,"available_quantity":600},
        13:{"name":"keyboard","price":1500,"available_quantity":450},
        14:{"name":"portable SSD","price":7000,"available_quantity":350},
        15:{"name":"gaming console","price":25000,"available_quantity":80},
        16:{"name":"graphics card","price":15000,"available_quantity":200},
        17:{"name":"smartphone tripod","price":500,"available_quantity":800},
        18:{"name":"USB flash drive","price":500,"available_quantity":1000},
        19:{"name":"webcam","price":3000,"available_quantity":250},
        20:{"name":"Bluetooth earphones","price":2500,"available_quantity":500}
}
@app1.get("/")
def send():
      return product