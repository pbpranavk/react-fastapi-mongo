from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database import (
    add_obj,
    delete_obj,
    update_obj,
    retrieve_simple_objects,
    retrieve_obj,
)

from app.server.models.simple_model import (
    ErrorResponseModel,
    ResponseModel,
    SimpleModel,
)

router = APIRouter()


@router.post("/", response_description="Object data added into db")
async def add_obj_data(obj: SimpleModel = Body(...)):
    obj = jsonable_encoder(obj)
    new_obj = await add_obj(obj)
    return ResponseModel(new_obj, "Obj added succesfully")


@router.get("/", response_description="Obj retrieved")
async def get_objs():
    objs = await retrieve_simple_objects()
    if objs:
        return ResponseModel(objs, "objs retrieved successfully")
    return ResponseModel(objs, "Empty list returned")


@router.get("/{id}", response_description="Obj data retrieved")
async def get_obj_data(id):
    obj = await retrieve_obj(id)
    if obj:
        return ResponseModel(obj, "Obj data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Obj doesn't exist.")


@router.put("/{id}")
async def update_obj_data(id: str, req: SimpleModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_obj = await update_obj(id, req)
    if updated_obj:
        return ResponseModel(
            "Obj with ID: {} name update is successful".format(id),
            "Obj updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the obj data.",
    )


@router.delete("/{id}", response_description="Obj data deleted from the database")
async def delete_student_data(id: str):
    deleted_obj = await delete_obj(id)
    if deleted_obj:
        return ResponseModel(
            "Obj with ID: {} removed".format(id), "Obj deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Obj with id {0} doesn't exist".format(id)
    )
