import asyncio
from aiohttp import web
import json
from db.db import DataBase

db = DataBase()


async def send(message):
    reader, writer = await asyncio.open_connection('calculator', 8888)
    message_len = len(message)
    writer.write(f'{message_len}\n{message}'.encode())
    data = await reader.read()
    writer.close()
    return data


async def calc(request):
    data = await request.json()
    answer = await send(json.dumps(data))
    answer = answer.decode()
    if answer:
        if answer != 'False':
            expression_id = db.save_result(float(answer))
            return web.json_response({'expression_id': expression_id})
        raise web.HTTPBadRequest()
    raise web.HTTPInternalServerError()


async def result(request):
    data = await request.json()
    try:
        result = db.get_result(data['id'])
        if result:
            return web.json_response({'result': result})
    except:
        raise web.HTTPBadRequest()


app = web.Application()
app.add_routes([
        web.post('/calc/', calc), web.post('/result/', result)
        ])

if __name__ == '__main__':
    web.run_app(app)
