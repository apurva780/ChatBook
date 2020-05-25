import json
from chat.models import Chat

import os


def getData(username1,username2,id):
    instance  = Chat.objects.filter(id=id)
    print(instance[0].attach)
    with open(f"./media/{instance[0].attach}") as js_data:
        data=json.load(js_data)
    data_file = open("data.txt","w+")

    for x in data:
        data_file.write(f"{x}\n\n\n\n\n")   

    temmsg=open("message.txt","w+")

    usr1 = f'{username1}'#add username 1
    usr2 = f'{username2}'# add username 2

    for x in data:
        if x["participants"] == [usr1,usr2 ] or x["participants"] == [usr2,usr1 ]:
            conver = x["conversation"]
            
            for c in conver:
                if c["sender"] == usr1:
                    try:
                        
                        temmsg.write(f"{usr1} : {c['text']}")
                        temmsg.write("\n\n")
                    except:
                        try:
                            try:
                                temmsg.write(f"{usr1} : {c['media']}")
                                temmsg.write("\n\n")
                            
                            except:
                                temmsg.write(f"{usr1} : {c['animated_media_images']}")
                                temmsg.write("\n\n")

                        except:    
                            temmsg.write(f"{usr1} : the user have liked or he had made a video or voice call action")
                            temmsg.write("\n\n")

                if c["sender"] == usr2:
                    try:
                        
                        temmsg.write(f"{usr2} : {c['text']}")
                        temmsg.write("\n\n")
                    except:
                        try:
                            try:
                                temmsg.write(f"{usr2} : {c['media']}")
                                temmsg.write("\n\n")
                            
                            except:
                                temmsg.write(f"{usr2} : {c['animated_media_images']}")
                                temmsg.write("\n\n")

                        except:    
                            temmsg.write(f"{usr2} : the user have liked or he had made a video or voice call action")
                            temmsg.write("\n\n")

    return True