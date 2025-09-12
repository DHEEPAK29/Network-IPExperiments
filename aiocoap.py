import asyncio
from aiocoap import Context, Message, GET

async def main():
    # Create a protocol context
    context = await Context.create_client_context()

    # Build a GET request to a local CoAP server
    request = Message(code=GET, uri='coap://localhost/time')

    # Send request and wait for response
    response = await context.request(request).response
    print(f"Result: {response.code}\nPayload: {response.payload.decode('utf-8')}")

if __name__ == "__main__":
    asyncio.run(main())
