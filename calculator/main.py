import asyncio
import json
import concurrent.futures
import calculator


def calc_expression(message):
    data = json.loads(message)
    exp_calc = calculator.ExpressionCalculator(data['expression'],
                                               data['variables'])
    return exp_calc.calc() if exp_calc else False


async def handle(reader, writer):
    try:
        data_length = await reader.readline()
        data = await reader.read(int(data_length.decode()))
        message = data.decode()
        loop = asyncio.get_running_loop()
        with concurrent.futures.ProcessPoolExecutor() as pool:
            result = await loop.run_in_executor(pool, calc_expression, message)
        writer.write(str(result).encode())
        await writer.drain()
    finally:
        writer.close()


async def main():
    server = await asyncio.start_server(handle, None, 8888)
    async with server:
        await server.serve_forever()


if __name__ == '__main__':
    asyncio.run(main())
