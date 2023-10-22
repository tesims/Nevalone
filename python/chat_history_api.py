import asyncio
from dotenv import load_dotenv
from api.upstash import MemoryManager
from companion import load_companions
from companion_app import guess_clerk_user_id

config = load_dotenv("../.env.local")

async def main():
    companion = load_companions()[1]
    companion.memory = MemoryManager(companion.name, companion.llm_name)
    companion.memory.user_id = await guess_clerk_user_id(companion)
    await companion.load()

    i = 0
    for c in ( await companion.memory.read_latest_history() ).split("\n"):
        if len(c.strip()) > 0:
            i += 1
            print(f'{i:2} {c.strip()}')

if __name__ == "__main__":
    asyncio.run(main())