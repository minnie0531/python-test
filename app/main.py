from fastapi import FastAPI
import logging.config


import os

logger = logging.getLogger("productService")

# Set logger name to project

logger.info("START Application")


# Define Fast api and description
app = FastAPI(
    title="Product service for Instana",
    description="This is a template of python MSA used in Garage project.",
    version="0.0.1",
)



# This path is for health check or test
@app.get("/")
async def root():
    print("logging test is it infolog?")
    logger.info("hello world :D")
    logger.warning("hello world :(")
    logger.error("hello world :X")
    return {"Hello World :D"}


@app.get("/test")
async def test():
    return {"Test endpoint"}
