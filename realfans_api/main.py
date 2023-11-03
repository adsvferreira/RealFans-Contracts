import uvicorn
from typing import NoReturn
from fastapi import FastAPI

from utils.colors import bcolors
from utils.cleanup_server import cleanup_server
from routes.helloworld import router as hello_world_router

app = FastAPI()
app.include_router(hello_world_router)


def main() -> NoReturn:
    print(
        f"""
{bcolors.PURPLE}Loading API...{bcolors.END_COLOR}
Visit {bcolors.YELLOW}http://localhost:9000/docs{bcolors.END_COLOR} for documentation
"""
    )
    uvicorn.run(app, host="0.0.0.0", port=9000, reload=False, workers=1)
    cleanup_server()

if __name__ == "__main__":
    main()