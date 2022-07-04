from pyromod.helpers import kb
class menu:
    def __init__(self , func) -> None:
        self.func = func
        self.dict = {}
        self.markups = []
    def line(self , button , func):
        for i in range(len(button)):
            self.dict[button[i]] = func[i]
        self.markups.append(button)
    
    def markup(self):
        return kb(self.markups)
    
    async def catch(self , cl,message,):
        if message.text in self.dict:
            await self.dict[message.text](cl , message)
        else:
            await self.func(cl ,message)
